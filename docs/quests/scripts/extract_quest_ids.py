#!/usr/bin/env python3
"""
Extract quest IDs with positions from an FTB Quests chapter file.

Usage:
    python extract_quest_ids.py path/to/chapter.snbt

Output:
    Sorted list of quests with their IDs and positions for mapping.
"""

import re
import sys

def extract_quests(content):
    """Extract quests with their IDs and positions."""
    quests = []
    lines = content.split('\n')

    current_quest = {}
    in_quest = False
    brace_depth = 0

    for line in lines:
        # Track brace depth to know when we're in a quest block
        open_braces = line.count('{')
        close_braces = line.count('}')
        brace_depth += open_braces - close_braces

        # Quest ID at quest level (3 tabs of indent)
        id_match = re.match(r'^\t\t\tid: "([A-F0-9]{16})"', line)
        if id_match:
            current_quest['id'] = id_match.group(1)
            in_quest = True

        # Icon (for context)
        icon_match = re.match(r'^\t\t\ticon: \{ id: "([^"]+)"', line)
        if icon_match and in_quest:
            current_quest['icon'] = icon_match.group(1)

        # X position
        x_match = re.match(r'^\t\t\tx: (-?[\d.]+)d', line)
        if x_match and in_quest:
            current_quest['x'] = float(x_match.group(1))

        # Y position
        y_match = re.match(r'^\t\t\ty: (-?[\d.]+)d', line)
        if y_match and in_quest:
            current_quest['y'] = float(y_match.group(1))

        # Dependencies
        dep_match = re.match(r'^\t\t\tdependencies: \[(.+)\]', line)
        if dep_match and in_quest:
            deps = re.findall(r'"([A-F0-9]{16})"', dep_match.group(1))
            current_quest['dependencies'] = deps

        # End of quest block (back to quests array level)
        if in_quest and brace_depth == 2 and close_braces > 0:
            if 'id' in current_quest:
                quests.append(current_quest.copy())
            current_quest = {}
            in_quest = False

    return quests

def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_quest_ids.py path/to/chapter.snbt")
        sys.exit(1)

    chapter_file = sys.argv[1]

    with open(chapter_file, 'r') as f:
        content = f.read()

    # Extract chapter ID
    chapter_id_match = re.search(r'^\tid: "([A-F0-9]{16})"', content, re.MULTILINE)
    if chapter_id_match:
        print(f"Chapter ID: {chapter_id_match.group(1)}\n")

    quests = extract_quests(content)

    # Sort by position (y then x - reading order)
    quests.sort(key=lambda q: (q.get('y', 0), q.get('x', 0)))

    print(f"Found {len(quests)} quests:\n")
    print("-" * 80)

    for i, q in enumerate(quests, 1):
        pos = f"({q.get('x', '?'):>6.1f}, {q.get('y', '?'):>6.1f})"
        icon = q.get('icon', 'unknown')[:40]
        deps = len(q.get('dependencies', []))
        print(f"{i:3}. ID: {q['id']}  Pos: {pos}  Deps: {deps}  Icon: {icon}")

    print("-" * 80)
    print("\nID Mapping Template (copy and edit):\n")
    print("ID_MAP = {")
    for i, q in enumerate(quests, 1):
        print(f'    "{i}": "{q["id"]}",  # {q.get("icon", "unknown").split(":")[-1]}')
    print("}")

if __name__ == "__main__":
    main()
