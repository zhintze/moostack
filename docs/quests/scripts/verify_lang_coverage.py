#!/usr/bin/env python3
"""
Verify that all quest IDs in a chapter file have corresponding lang entries.

Usage:
    python verify_lang_coverage.py path/to/chapter.snbt path/to/en_us.snbt

Output:
    List of missing lang entries and coverage summary.
"""

import re
import sys

def extract_quest_ids(chapter_content):
    """Extract all quest IDs from chapter file."""
    # Quest IDs at the quest level (3 tabs indent)
    return re.findall(r'^\t\t\tid: "([A-F0-9]{16})"', chapter_content, re.MULTILINE)

def extract_task_ids(chapter_content):
    """Extract all task IDs from chapter file (for checkmark tasks)."""
    # Task IDs at the task level (5 tabs indent within tasks array)
    return re.findall(r'^\t\t\t\t\tid: "([A-F0-9]{16})"', chapter_content, re.MULTILINE)

def extract_chapter_id(chapter_content):
    """Extract chapter ID."""
    match = re.search(r'^\tid: "([A-F0-9]{16})"', chapter_content, re.MULTILINE)
    return match.group(1) if match else None

def check_lang_entry(lang_content, entry_type, entry_id, field):
    """Check if a specific lang entry exists."""
    pattern = f'{entry_type}\\.{entry_id}\\.{field}:'
    return bool(re.search(pattern, lang_content))

def main():
    if len(sys.argv) < 3:
        print("Usage: python verify_lang_coverage.py path/to/chapter.snbt path/to/en_us.snbt")
        sys.exit(1)

    chapter_file = sys.argv[1]
    lang_file = sys.argv[2]

    with open(chapter_file, 'r') as f:
        chapter_content = f.read()

    with open(lang_file, 'r') as f:
        lang_content = f.read()

    # Check chapter title
    chapter_id = extract_chapter_id(chapter_content)
    missing = []
    found = []

    print("=" * 70)
    print("LANG COVERAGE VERIFICATION")
    print("=" * 70)
    print(f"\nChapter file: {chapter_file}")
    print(f"Lang file: {lang_file}\n")

    if chapter_id:
        if check_lang_entry(lang_content, 'chapter', chapter_id, 'title'):
            found.append(f"chapter.{chapter_id}.title")
        else:
            missing.append(f"chapter.{chapter_id}.title")

    # Check quests
    quest_ids = extract_quest_ids(chapter_content)
    print(f"Found {len(quest_ids)} quests in chapter file\n")

    print("-" * 70)
    print("CHECKING QUEST ENTRIES")
    print("-" * 70)

    for qid in quest_ids:
        # Check title
        if check_lang_entry(lang_content, 'quest', qid, 'title'):
            found.append(f"quest.{qid}.title")
        else:
            missing.append(f"quest.{qid}.title")
            print(f"MISSING: quest.{qid}.title")

        # Check description
        if check_lang_entry(lang_content, 'quest', qid, 'quest_desc'):
            found.append(f"quest.{qid}.quest_desc")
        else:
            missing.append(f"quest.{qid}.quest_desc")
            print(f"MISSING: quest.{qid}.quest_desc")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"\nTotal entries checked: {len(found) + len(missing)}")
    print(f"Found: {len(found)}")
    print(f"Missing: {len(missing)}")

    if missing:
        print(f"\nRESULT: FAIL - {len(missing)} missing entries")
        print("\nMissing entries:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    else:
        print("\nRESULT: PASS - All entries present")
        sys.exit(0)

if __name__ == "__main__":
    main()
