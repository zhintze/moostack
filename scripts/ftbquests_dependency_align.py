#!/usr/bin/env python3
"""
FTB Quests Dependency Alignment Script

This script compares quest dependencies between a source modpack (e.g., ATM-10)
and mooStack, then generates fixes to align the dependencies.

Usage:
    python3 ftbquests_dependency_align.py <source_chapter> <target_chapter> [--mod-prefix MOD_PREFIX]

Example:
    python3 ftbquests_dependency_align.py \
        /path/to/atm10/chapters/applied_energistics_2.snbt \
        runs/client/config/ftbquests/quests/chapters/applied_energistics.snbt \
        --mod-prefix ae2: megacells: aeinfinitybooster:
"""

import re
import json
import argparse
import sys


def extract_quests_from_snbt(content):
    """Extract quests with their IDs, items, and dependencies from SNBT content."""
    quests = []
    lines = content.split('\n')

    current_quest_lines = []
    brace_depth = 0
    in_quests_array = False

    for line in lines:
        if 'quests: [' in line:
            in_quests_array = True
            continue

        if not in_quests_array:
            continue

        open_braces = line.count('{')
        close_braces = line.count('}')

        if brace_depth == 0 and open_braces > 0:
            current_quest_lines = [line]
            brace_depth = open_braces - close_braces
        elif brace_depth > 0:
            current_quest_lines.append(line)
            brace_depth += open_braces - close_braces

            if brace_depth == 0:
                quest_text = '\n'.join(current_quest_lines)

                id_match = re.search(r'^\s*id:\s*"([A-F0-9]{16})"', quest_text, re.MULTILINE)
                if id_match:
                    quest_id = id_match.group(1)

                    # Extract dependencies
                    deps = []
                    dep_match = re.search(r'dependencies:\s*\[(.*?)\]', quest_text, re.DOTALL)
                    if dep_match:
                        dep_content = dep_match.group(1)
                        deps = re.findall(r'"([A-F0-9]{16})"', dep_content)

                    # Extract ALL item IDs from task items
                    items = []
                    item_matches = re.findall(r'id:\s*"([a-z_]+:[a-z0-9_]+)"', quest_text)
                    items = list(dict.fromkeys(item_matches))

                    # Check for checkmark type
                    is_checkmark = 'type: "checkmark"' in quest_text

                    # Check for advancement
                    adv_match = re.search(r'advancement:\s*"([^"]+)"', quest_text)
                    advancement = adv_match.group(1) if adv_match else None

                    quests.append({
                        'id': quest_id,
                        'dependencies': deps,
                        'items': items,
                        'is_checkmark': is_checkmark,
                        'advancement': advancement
                    })

                current_quest_lines = []

    return quests


def get_quest_key(quest, mod_prefixes):
    """Generate a key to match quests between packs."""
    # Filter to mod-specific items (not generic rewards like minecraft:iron_ingot)
    mod_items = [i for i in quest['items'] if any(i.startswith(p) for p in mod_prefixes)]

    if quest['advancement']:
        return f"adv:{quest['advancement']}"
    if quest['is_checkmark']:
        return "checkmark"
    if mod_items:
        return mod_items[0]  # Use first mod item as key
    return None


def resolve_deps_to_keys(deps, id_to_quest_map, mod_prefixes):
    """Convert dependency IDs to quest keys."""
    keys = []
    for dep_id in deps:
        if dep_id in id_to_quest_map:
            dep_quest = id_to_quest_map[dep_id]
            key = get_quest_key(dep_quest, mod_prefixes)
            if key:
                keys.append(key)
    return sorted(keys)


def main():
    parser = argparse.ArgumentParser(
        description='Compare and align FTB Quest dependencies between packs'
    )
    parser.add_argument('source', help='Path to source chapter file (e.g., ATM-10)')
    parser.add_argument('target', help='Path to target chapter file (e.g., mooStack)')
    parser.add_argument('--mod-prefix', nargs='+', default=['ae2:', 'megacells:', 'aeinfinitybooster:'],
                        help='Mod prefixes to use for quest matching (default: ae2: megacells: aeinfinitybooster:)')
    parser.add_argument('--output', '-o', help='Output JSON file for fixes (optional)')
    parser.add_argument('--apply', action='store_true', help='Apply fixes to target file')

    args = parser.parse_args()

    # Read both files
    try:
        with open(args.source, 'r') as f:
            source_content = f.read()
    except FileNotFoundError:
        print(f"Error: Source file not found: {args.source}")
        sys.exit(1)

    try:
        with open(args.target, 'r') as f:
            target_content = f.read()
    except FileNotFoundError:
        print(f"Error: Target file not found: {args.target}")
        sys.exit(1)

    # Extract quests
    source_quests = extract_quests_from_snbt(source_content)
    target_quests = extract_quests_from_snbt(target_content)

    print(f"Source quests: {len(source_quests)}")
    print(f"Target quests: {len(target_quests)}")

    # Build ID -> quest maps
    source_by_id = {q['id']: q for q in source_quests}
    target_by_id = {q['id']: q for q in target_quests}

    # Build key -> quest mappings
    mod_prefixes = args.mod_prefix

    source_by_key = {}
    for q in source_quests:
        key = get_quest_key(q, mod_prefixes)
        if key and key != "checkmark":
            source_by_key[key] = q

    target_by_key = {}
    for q in target_quests:
        key = get_quest_key(q, mod_prefixes)
        if key and key != "checkmark":
            target_by_key[key] = q

    # Build key -> target ID mapping
    target_key_to_id = {}
    for q in target_quests:
        key = get_quest_key(q, mod_prefixes)
        if key and key != "checkmark":
            target_key_to_id[key] = q['id']

    # Build source ID -> key mapping
    source_id_to_key = {}
    for q in source_quests:
        key = get_quest_key(q, mod_prefixes)
        if key:
            source_id_to_key[q['id']] = key

    # Find missing quests
    print("\n=== QUEST COVERAGE ===\n")
    missing_in_target = []
    for key in source_by_key:
        if key not in target_by_key:
            missing_in_target.append(key)

    if missing_in_target:
        print("Quests in source but not in target:")
        for key in missing_in_target:
            print(f"  - {key}")
    else:
        print("All source quests have matching quests in target.")

    # Generate fixes
    fixes = []
    all_keys = set(source_by_key.keys()) | set(target_by_key.keys())

    for key in sorted(all_keys):
        source_quest = source_by_key.get(key)
        target_quest = target_by_key.get(key)

        if source_quest and target_quest:
            # Translate source dependencies to target IDs
            target_dep_ids = []
            for source_dep_id in source_quest['dependencies']:
                dep_key = source_id_to_key.get(source_dep_id)
                if dep_key and dep_key in target_key_to_id:
                    target_dep_ids.append(target_key_to_id[dep_key])
                # Skip dependencies that don't exist in target

            current_deps = target_quest['dependencies']

            # Check if deps need updating
            if sorted(current_deps) != sorted(target_dep_ids):
                fixes.append({
                    'quest_id': target_quest['id'],
                    'quest_key': key,
                    'current_deps': current_deps,
                    'target_deps': target_dep_ids
                })

    # Report fixes
    print(f"\n=== DEPENDENCY FIXES ({len(fixes)} needed) ===\n")

    if not fixes:
        print("All dependencies match! No fixes needed.")
    else:
        add_fixes = []
        replace_fixes = []
        remove_fixes = []

        for fix in fixes:
            if not fix['target_deps'] and fix['current_deps']:
                remove_fixes.append(fix)
            elif not fix['current_deps'] and fix['target_deps']:
                add_fixes.append(fix)
            else:
                replace_fixes.append(fix)

        if add_fixes:
            print("ADD dependencies:")
            for fix in add_fixes:
                deps_str = '", "'.join(fix['target_deps'])
                print(f"  {fix['quest_key']}: dependencies: [\"{deps_str}\"]")

        if replace_fixes:
            print("\nREPLACE dependencies:")
            for fix in replace_fixes:
                deps_str = '", "'.join(fix['target_deps'])
                print(f"  {fix['quest_key']}: dependencies: [\"{deps_str}\"]")

        if remove_fixes:
            print("\nREMOVE dependencies:")
            for fix in remove_fixes:
                print(f"  {fix['quest_key']}")

    # Output fixes to JSON if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(fixes, f, indent=2)
        print(f"\nFixes written to: {args.output}")

    # Apply fixes if requested
    if args.apply and fixes:
        print("\n=== APPLYING FIXES ===\n")
        modified_content = target_content

        for fix in fixes:
            quest_id = fix['quest_id']
            target_deps = fix['target_deps']
            current_deps = fix['current_deps']

            if not target_deps:
                # Remove dependencies line
                if current_deps:
                    # Find and remove dependencies line
                    pattern = r'\s*dependencies:\s*\[.*?\]\n'
                    quest_start = modified_content.find(f'id: "{quest_id}"')
                    if quest_start != -1:
                        block_start = modified_content.rfind('{', 0, quest_start)
                        depth = 1
                        pos = block_start + 1
                        while depth > 0 and pos < len(modified_content):
                            if modified_content[pos] == '{':
                                depth += 1
                            elif modified_content[pos] == '}':
                                depth -= 1
                            pos += 1
                        block_end = pos

                        quest_block = modified_content[block_start:block_end]
                        new_block = re.sub(r'\s*dependencies:\s*\[.*?\]\n', '\n', quest_block, count=1)

                        if new_block != quest_block:
                            modified_content = modified_content[:block_start] + new_block + modified_content[block_end:]
                            print(f"Removed dependencies from {fix['quest_key']}")
            else:
                deps_str = '", "'.join(target_deps)
                new_deps_line = f'dependencies: ["{deps_str}"]'

                quest_start = modified_content.find(f'id: "{quest_id}"')
                if quest_start != -1:
                    block_start = modified_content.rfind('{', 0, quest_start)
                    depth = 1
                    pos = block_start + 1
                    while depth > 0 and pos < len(modified_content):
                        if modified_content[pos] == '{':
                            depth += 1
                        elif modified_content[pos] == '}':
                            depth -= 1
                        pos += 1
                    block_end = pos

                    quest_block = modified_content[block_start:block_end]

                    if current_deps:
                        # Replace existing dependencies
                        new_block = re.sub(
                            r'dependencies:\s*\[.*?\]',
                            new_deps_line,
                            quest_block,
                            count=1
                        )
                        if new_block != quest_block:
                            modified_content = modified_content[:block_start] + new_block + modified_content[block_end:]
                            print(f"Replaced dependencies in {fix['quest_key']}")
                    else:
                        # Add new dependencies line
                        first_newline = quest_block.find('\n')
                        if first_newline != -1:
                            new_block = quest_block[:first_newline+1] + '\t\t\t' + new_deps_line + '\n' + quest_block[first_newline+1:]
                            modified_content = modified_content[:block_start] + new_block + modified_content[block_end:]
                            print(f"Added dependencies to {fix['quest_key']}")

        # Write modified content
        with open(args.target, 'w') as f:
            f.write(modified_content)
        print(f"\nModified file written: {args.target}")

    return 0 if not fixes else 1


if __name__ == '__main__':
    sys.exit(main())
