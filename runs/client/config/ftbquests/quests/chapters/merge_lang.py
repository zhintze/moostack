#!/usr/bin/env python3
"""
Merge per-chapter Mekanism lang entries into the main en_us.snbt file.
FTB Quests reads from the main file, not per-chapter files.

Removes ALL old Mekanism entries (both our A1xx IDs and stale FTB Quests
random IDs from old chapter files), then appends fresh entries once.
"""

import os
import re
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_LANG = os.path.join(SCRIPT_DIR, "..", "lang", "en_us.snbt")
CHAPTER_LANG_DIR = os.path.join(SCRIPT_DIR, "..", "lang", "en_us", "chapters")

MEKANISM_LANGS = [
    "mekanism.snbt",
]

# Old Mekanism chapter IDs that FTB Quests assigned (from previous restructures).
# Any lang entries referencing these should be removed.
OLD_MEKANISM_CHAPTER_IDS = {
    "0A093D8C4429B627",  # old "Mekanism: Power"
    "23983F4DC524B14B",  # old "Mekanism"
    "7A93B67A6A329F70",  # runtime-assigned "Mekanism"
}


def extract_entries(filepath):
    """Extract all quest.* and chapter.* entries from a per-chapter lang file."""
    with open(filepath) as f:
        content = f.read()

    entries = []
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Skip braces, comments, empty lines
        if stripped in ('{', '}', '') or stripped.startswith('//'):
            i += 1
            continue

        # Check for multi-line array (quest_desc)
        if 'quest_desc: [' in line and not line.rstrip().endswith(']'):
            block = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(']'):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                block.append(lines[i])  # the closing ]
            entries.append('\n'.join(block))
        else:
            entries.append(line)

        i += 1

    return entries


def collect_old_chapter_ids():
    """Collect all IDs from old Mekanism chapter SNBT files via git history."""
    old_ids = set()
    # Old chapter filenames that existed before the unified chapter
    old_files = [
        "config/ftbquests/quests/chapters/mekanism_reactors.snbt",
        "config/ftbquests/quests/chapters/mekanism_nuclear.snbt",
        "config/ftbquests/quests/chapters/mekanism_ore_processing.snbt",
    ]
    for f in old_files:
        try:
            result = subprocess.run(
                ["git", "show", f"HEAD:{f}"],
                capture_output=True, text=True, cwd=SCRIPT_DIR
            )
            if result.returncode == 0:
                for m in re.finditer(r'id: "([A-Fa-f0-9]+)"', result.stdout):
                    old_ids.add(m.group(1))
        except Exception:
            pass

    # Also grab IDs from old committed mekanism.snbt that used random FTB IDs
    # We look for the last commit that had random (non-A1xx) IDs
    try:
        result = subprocess.run(
            ["git", "show", "93f94c0:config/ftbquests/quests/chapters/mekanism.snbt"],
            capture_output=True, text=True, cwd=SCRIPT_DIR
        )
        if result.returncode == 0:
            for m in re.finditer(r'id: "([A-Fa-f0-9]+)"', result.stdout):
                mid = m.group(1)
                if not mid.startswith("A1"):  # skip our own IDs
                    old_ids.add(mid)
    except Exception:
        pass

    return old_ids


def main():
    with open(MAIN_LANG) as f:
        main_content = f.read()

    # Collect all IDs to remove: our new A1xx IDs + old random FTB IDs
    ids_to_remove = set()

    # 1. New quest/chapter IDs from our per-chapter lang files
    for lang_file in MEKANISM_LANGS:
        path = os.path.join(CHAPTER_LANG_DIR, lang_file)
        with open(path) as f:
            content = f.read()
        for m in re.finditer(r'(?:quest|chapter|task|reward)\.([A-Fa-f0-9]+)\.', content):
            ids_to_remove.add(m.group(1))

    # 2. Old chapter IDs from git history
    old_ids = collect_old_chapter_ids()
    ids_to_remove.update(old_ids)

    # 3. Hardcoded old chapter IDs
    ids_to_remove.update(OLD_MEKANISM_CHAPTER_IDS)

    print(f"Found {len(ids_to_remove)} IDs to clean (new + old Mekanism)")

    # Collect entries to add
    all_entries = []
    for lang_file in MEKANISM_LANGS:
        path = os.path.join(CHAPTER_LANG_DIR, lang_file)
        entries = extract_entries(path)
        all_entries.extend(entries)
        print(f"  {lang_file}: {len(entries)} entries")

    # Remove existing entries for any of these IDs, plus old section comments
    lines = main_content.split('\n')
    filtered = []
    i = 0
    removed = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Remove old "// ── Mekanism ──" section comments
        if stripped == '// ── Mekanism ──':
            i += 1
            removed += 1
            continue

        # Check if this line references any ID we need to remove
        skip = False
        # Extract ID from line if it matches quest.XXX. / chapter.XXX. / task.XXX. / reward.XXX.
        id_match = re.search(r'(?:quest|chapter|task|reward)\.([A-Fa-f0-9]+)\.', line)
        if id_match and id_match.group(1) in ids_to_remove:
            skip = True
            # If it's a multi-line quest_desc, skip until closing ]
            if 'quest_desc: [' in line and not line.rstrip().endswith(']'):
                i += 1
                while i < len(lines) and not lines[i].strip().startswith(']'):
                    i += 1
                # skip the closing ] too
            removed += 1

        if not skip:
            filtered.append(line)
        i += 1

    print(f"Removed {removed} existing entries/comments")

    # Strip trailing blank lines before the closing brace
    result = '\n'.join(filtered)

    # Insert entries before the final closing brace
    last_brace = result.rfind('}')
    if last_brace == -1:
        print("ERROR: No closing brace found in main lang file!")
        return

    # Build the block to insert (single section, no duplicates)
    insert_block = "\n\t// ── Mekanism ──\n"
    for entry in all_entries:
        insert_block += entry + "\n"

    result = result[:last_brace] + insert_block + result[last_brace:]

    with open(MAIN_LANG, 'w') as f:
        f.write(result)

    print(f"\nMerged {len(all_entries)} entries into main en_us.snbt")


if __name__ == "__main__":
    main()
