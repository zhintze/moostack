#!/usr/bin/env python3
"""
Repair unified Mekanism quest chapter after FTB Quests regenerated all IDs.

Strategy:
1. Import generate_mekanism.py to get original quest data (old IDs, positions, deps)
2. Parse regenerated SNBT file to get new IDs with positions
3. Match by (x, y) coordinates to build old->new ID mapping
4. Re-inject dependency lines into SNBT file
5. Rebuild lang file with new IDs (including new chapter ID)
"""

import os
import re
import sys
import importlib.util

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LANG_DIR = os.path.join(SCRIPT_DIR, "..", "lang", "en_us", "chapters")

SECTION_NAMES = {
    1: "Section 1: Foundation",
    2: "Section 2: Basic Machines",
    3: "Section 3: Advanced Tier",
    4: "Section 4: Elite Tier",
    5: "Section 5: Ultimate Tier & Transport",
    6: "Section 6: Power Branch",
    7: "Section 7: Logistics & Upgrades",
    8: "Section 8: Ore Processing Path",
    9: "Section 9: Nuclear Path",
    0x0A: "Section 10: Waste, SPS & Endgame",
}


def load_gen_module():
    """Import generate_mekanism.py as a module."""
    path = os.path.join(SCRIPT_DIR, "generate_mekanism.py")
    spec = importlib.util.spec_from_file_location("generate_mekanism", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def parse_snbt_quests(filepath):
    """Parse regenerated SNBT file, extract quest ID and (x, y) for each quest."""
    with open(filepath) as f:
        content = f.read()

    # Extract the chapter ID (top-level id field, not inside quests)
    chapter_id_match = re.search(r'^\tid: "([A-Fa-f0-9]+)"', content, re.MULTILINE)
    chapter_id = chapter_id_match.group(1) if chapter_id_match else None

    quests = []
    # Split into quest blocks by finding the quest-level pattern
    quest_blocks = re.split(r'\n\t\t\{', content)

    for block in quest_blocks[1:]:  # skip the header
        id_match = re.search(r'^\s*id: "([A-Fa-f0-9]+)"', block, re.MULTILINE)
        x_match = re.search(r'x: (-?[\d.]+)d', block)
        y_match = re.search(r'y: (-?[\d.]+)d', block)

        if id_match and x_match and y_match:
            quests.append({
                "id": id_match.group(1),
                "x": float(x_match.group(1)),
                "y": float(y_match.group(1)),
            })

    return chapter_id, quests


def build_id_mapping(gen_mod, snbt_quests):
    """Match generation script quests to SNBT quests by (x, y) position."""
    mapping = {}  # old_quest_id -> new_quest_id
    used = set()

    for orig_quest in gen_mod.QUESTS:
        old_id = gen_mod.quest_id(orig_quest["section"], orig_quest["num"])
        ox, oy = orig_quest["x"], orig_quest["y"]

        # Find matching SNBT quest by position
        matched = None
        for sq in snbt_quests:
            key = sq["id"]
            if key in used:
                continue
            if abs(sq["x"] - ox) < 0.01 and abs(sq["y"] - oy) < 0.01:
                matched = sq
                used.add(key)
                break

        if matched:
            mapping[old_id] = matched["id"]
        else:
            print(f"  WARNING: No match for quest {old_id} at ({ox}, {oy})")

    return mapping


def inject_dependencies(filepath, gen_mod, id_mapping):
    """Re-inject dependency lines into the SNBT file using new IDs."""
    with open(filepath) as f:
        content = f.read()

    # Build a map of new_quest_id -> list of new dependency IDs
    dep_map = {}
    for orig_quest in gen_mod.QUESTS:
        old_id = gen_mod.quest_id(orig_quest["section"], orig_quest["num"])
        new_id = id_mapping.get(old_id)
        if not new_id or not orig_quest["deps"]:
            continue

        new_deps = []
        for old_dep in orig_quest["deps"]:
            new_dep = id_mapping.get(old_dep)
            if new_dep:
                new_deps.append(new_dep)
            else:
                print(f"  WARNING: Dep {old_dep} not found in mapping for quest {old_id}")

        if new_deps:
            dep_map[new_id] = new_deps

    # Process line by line, inject dependencies before each matching quest id line
    lines = content.split('\n')
    output = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # Check if this is a quest ID line (tab-tab-tab-id pattern)
        id_match = re.match(r'^(\t\t\t)id: "([A-Fa-f0-9]+)"$', line)
        if id_match:
            indent = id_match.group(1)
            quest_id = id_match.group(2)

            if quest_id in dep_map:
                deps = dep_map[quest_id]
                if len(deps) == 1:
                    output.append(f'{indent}dependencies: ["{deps[0]}"]')
                else:
                    output.append(f'{indent}dependencies: [')
                    for d in deps:
                        output.append(f'{indent}\t"{d}"')
                    output.append(f'{indent}]')

        output.append(line)
        i += 1

    with open(filepath, "w") as f:
        f.write('\n'.join(output))

    return len(dep_map)


def rebuild_lang(gen_mod, id_mapping, new_chapter_id):
    """Rebuild the per-chapter lang file with new IDs."""
    lines = []
    lines.append("{")
    lines.append(f'\tchapter.{new_chapter_id}.title: "Mekanism"')
    lines.append("")

    current_section = 0
    for q in gen_mod.QUESTS:
        if q["section"] != current_section:
            current_section = q["section"]
            if current_section in SECTION_NAMES:
                lines.append(f"\t// {SECTION_NAMES[current_section]}")

        old_id = gen_mod.quest_id(q["section"], q["num"])
        new_id = id_mapping.get(old_id, old_id)

        lines.append(f'\tquest.{new_id}.title: "{q["title"]}"')

        if q.get("desc"):
            lines.append(f"\tquest.{new_id}.quest_desc: [")
            for d in q["desc"]:
                lines.append(f'\t\t"{d}"')
            lines.append("\t]")

    lines.append("}")
    lines.append("")

    lang_path = os.path.join(LANG_DIR, "mekanism.snbt")
    with open(lang_path, "w") as f:
        f.write("\n".join(lines))

    return len(gen_mod.QUESTS)


def update_main_lang(new_chapter_id):
    """Update the main en_us.snbt with new chapter ID."""
    main_lang = os.path.join(SCRIPT_DIR, "..", "lang", "en_us.snbt")
    with open(main_lang) as f:
        content = f.read()

    # Remove any old Mekanism chapter entries
    old_patterns = [
        r'\tchapter\.[A-Fa-f0-9]+\.title: "Mekanism"\n',
        r'\tchapter\.[A-Fa-f0-9]+\.title: "Mekanism: Ore Processing"\n',
        r'\tchapter\.[A-Fa-f0-9]+\.title: "Mekanism: Nuclear"\n',
        r'\tchapter\.[A-Fa-f0-9]+\.title: "Mekanism: Power"\n',
    ]
    for pat in old_patterns:
        content = re.sub(pat, '', content)

    # Insert new chapter entry after opening brace
    new_entry = f'\tchapter.{new_chapter_id}.title: "Mekanism"\n'
    content = content.replace("{\n", "{\n" + new_entry, 1)

    with open(main_lang, "w") as f:
        f.write(content)

    print(f"  Updated main lang file with chapter ID {new_chapter_id}")


def main():
    print("=" * 60)
    print("Repairing unified Mekanism chapter")
    print("=" * 60)

    # Load generation module
    gen_mod = load_gen_module()

    # Parse regenerated SNBT
    snbt_path = os.path.join(SCRIPT_DIR, "mekanism.snbt")
    new_chapter_id, snbt_quests = parse_snbt_quests(snbt_path)
    print(f"  Chapter ID: {gen_mod.chapter_id()} -> {new_chapter_id}")
    print(f"  Found {len(snbt_quests)} quests in SNBT")
    print(f"  Expected {len(gen_mod.QUESTS)} quests from generator")

    # Build mapping
    id_mapping = build_id_mapping(gen_mod, snbt_quests)
    print(f"  Mapped {len(id_mapping)}/{len(gen_mod.QUESTS)} quests")

    if len(id_mapping) != len(gen_mod.QUESTS):
        print("  ERROR: Not all quests matched!")
        for q in gen_mod.QUESTS:
            old_id = gen_mod.quest_id(q["section"], q["num"])
            if old_id not in id_mapping:
                print(f"    UNMATCHED: {old_id} '{q['title']}' at ({q['x']}, {q['y']})")
        sys.exit(1)

    # Inject dependencies
    dep_count = inject_dependencies(snbt_path, gen_mod, id_mapping)
    print(f"  Injected dependencies for {dep_count} quests")

    # Rebuild lang
    quest_count = rebuild_lang(gen_mod, id_mapping, new_chapter_id)
    print(f"  Rebuilt lang file with {quest_count} quest entries")

    # Update main lang file
    print(f"\n{'=' * 60}")
    print("Updating main lang file")
    print(f"{'=' * 60}")
    update_main_lang(new_chapter_id)

    print(f"\n{'=' * 60}")
    print("Mekanism chapter repaired!")
    print("Next: run merge_lang.py, then sync to defaultconfigs/ and config/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
