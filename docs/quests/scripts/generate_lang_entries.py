#!/usr/bin/env python3
"""
Generate lang entries for a chapter after ID regeneration.

This is a TEMPLATE script. Copy it and edit the configuration for your
specific chapter.

Usage:
    1. Copy this file to your working directory
    2. Edit CHAPTER_NAME and CHAPTER_ID
    3. Edit QUESTS list with your quest data and new IDs
    4. Run: python generate_lang_entries.py > new_lang_entries.txt
    5. Append the output to en_us.snbt

IMPORTANT: APPEND the output to the lang file. Do NOT replace existing content.
"""

# ============================================================================
# CONFIGURATION - EDIT THESE VALUES
# ============================================================================

CHAPTER_NAME = "Your Chapter Name"
CHAPTER_ID = "XXXXXXXXXXXXXXXX"  # 16-char hex ID from regenerated chapter file

# Quest data with regenerated IDs
# Format: (quest_id, title, description_lines, optional_task_titles)
#
# description_lines is a list where each element is a paragraph
# Empty string "" creates a paragraph break
#
# task_titles is a dict of {task_id: task_title} for checkmark tasks only

QUESTS = [
    # Section 1: Introduction
    {
        "id": "1DBD815EB154939D",  # Replace with actual regenerated ID
        "title": "First Quest Title",
        "desc": [
            "First paragraph of the description.",
            "",
            "Second paragraph after a blank line."
        ],
        "tasks": {}  # No checkmark tasks
    },
    {
        "id": "3A1FEE9C61BF949E",  # Replace with actual regenerated ID
        "title": "Second Quest Title",
        "desc": ["Single paragraph description."],
        "tasks": {
            "TASK_ID_HERE": "Complete this checkmark task"
        }
    },
    # Add more quests...
]

# ============================================================================
# SCRIPT LOGIC - DO NOT EDIT BELOW
# ============================================================================

def format_desc(desc_lines):
    """Format description lines for SNBT."""
    if len(desc_lines) == 1:
        return f'["{desc_lines[0]}"]'
    else:
        formatted = []
        for line in desc_lines:
            formatted.append(f'\t\t"{line}"')
        return '[\n' + '\n'.join(formatted) + '\n\t]'

def generate_lang_entries():
    """Generate lang entries for all quests."""
    lines = []

    # Chapter title
    lines.append(f"\n\t// ==================== {CHAPTER_NAME} ====================")
    lines.append(f'\tchapter.{CHAPTER_ID}.title: "{CHAPTER_NAME}"')
    lines.append("")

    current_section = None

    for quest in QUESTS:
        # Quest title
        lines.append(f'\tquest.{quest["id"]}.title: "{quest["title"]}"')

        # Quest description
        desc = format_desc(quest["desc"])
        lines.append(f'\tquest.{quest["id"]}.quest_desc: {desc}')

        # Task titles (for checkmark tasks)
        for task_id, task_title in quest.get("tasks", {}).items():
            lines.append(f'\ttask.{task_id}.title: "{task_title}"')

        lines.append("")

    return '\n'.join(lines)

def main():
    output = generate_lang_entries()
    print(output)

    print("\n// ========================================", file=__import__('sys').stderr)
    print("// INSTRUCTIONS:", file=__import__('sys').stderr)
    print("// 1. Review the output above", file=__import__('sys').stderr)
    print("// 2. APPEND to runs/client/config/ftbquests/quests/lang/en_us.snbt", file=__import__('sys').stderr)
    print("// 3. Do NOT delete existing entries", file=__import__('sys').stderr)
    print("// ========================================", file=__import__('sys').stderr)

if __name__ == "__main__":
    main()
