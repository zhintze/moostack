#!/usr/bin/env python3
"""
Add dependencies to quests in an FTB Quests chapter file.

This is a TEMPLATE script. Copy it and edit the DEPENDENCIES dictionary
for your specific chapter.

Usage:
    1. Copy this file to your working directory
    2. Edit CHAPTER_FILE path
    3. Edit DEPENDENCIES dictionary with your quest IDs
    4. Run: python add_dependencies.py

The script inserts dependencies lines before the id: line for each quest.
"""

import re

# ============================================================================
# CONFIGURATION - EDIT THESE VALUES
# ============================================================================

CHAPTER_FILE = "runs/client/config/ftbquests/quests/chapters/YOUR_CHAPTER.snbt"

# Dependency mapping: quest_id -> [list of dependency quest_ids]
# Format: The quest with the key ID will depend on all quests in the value list
#
# Example:
# DEPENDENCIES = {
#     "3A1FEE9C61BF949E": ["1DBD815EB154939D"],  # Quest 2 depends on Quest 1
#     "1E4474DDD71EB046": ["3A1FEE9C61BF949E"],  # Quest 3 depends on Quest 2
# }

DEPENDENCIES = {
    # Edit this section with your quest dependencies
    # "QUEST_ID": ["DEPENDENCY_ID_1", "DEPENDENCY_ID_2"],
}

# ============================================================================
# SCRIPT LOGIC - DO NOT EDIT BELOW
# ============================================================================

def add_dependencies(content):
    """Add dependencies to quest entries in the SNBT content."""
    if not DEPENDENCIES:
        print("WARNING: No dependencies configured. Edit the DEPENDENCIES dictionary.")
        return content

    lines = content.split('\n')
    result = []
    added_count = 0

    for line in lines:
        # Check if this line contains a quest id (at quest level - 3 tabs)
        id_match = re.match(r'^(\t\t\t)id: "([A-F0-9]{16})"', line)
        if id_match:
            indent = id_match.group(1)
            quest_id = id_match.group(2)

            if quest_id in DEPENDENCIES:
                deps = DEPENDENCIES[quest_id]
                deps_str = ", ".join([f'"{d}"' for d in deps])
                # Insert dependencies line BEFORE the id line
                result.append(f'{indent}dependencies: [{deps_str}]')
                added_count += 1

        result.append(line)

    print(f"Added dependencies to {added_count} quests")
    return '\n'.join(result)

def main():
    print(f"Reading: {CHAPTER_FILE}")

    try:
        with open(CHAPTER_FILE, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"ERROR: File not found: {CHAPTER_FILE}")
        print("Edit the CHAPTER_FILE variable to point to your chapter file.")
        return

    # Check if dependencies already exist
    existing_deps = content.count("dependencies:")
    if existing_deps > 0:
        print(f"WARNING: File already contains {existing_deps} dependencies entries.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            return

    new_content = add_dependencies(content)

    with open(CHAPTER_FILE, 'w') as f:
        f.write(new_content)

    print(f"Updated: {CHAPTER_FILE}")

    # Verify
    new_deps = new_content.count("dependencies:")
    print(f"Total dependencies entries in file: {new_deps}")

if __name__ == "__main__":
    main()
