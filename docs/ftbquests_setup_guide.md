# FTB Quests Setup Guide for mooStack

This document captures learnings from setting up FTB Quests localization. Use this as a reference for future quest development.

---

## CRITICAL: The Three Directories and Data Flow

**This section documents hard-learned lessons. Read this FIRST before doing ANY quest work.**

### The Three Directories

There are THREE directories involved in FTB Quests. Understanding their relationship is critical:

```
runs/client/config/ftbquests/    <-- RUNTIME (game reads from here)
         |
         | (manual copy when chapter is COMPLETE and TESTED)
         v
defaultconfigs/ftbquests/        <-- DISTRIBUTION (template for new worlds)
         |
         | (keep in sync)
         v
config/ftbquests/                <-- GIT TRACKED (mirrors defaultconfigs)
```

### Directory Purposes

| Directory | Purpose | Git Tracked? | Game Reads? |
|-----------|---------|--------------|-------------|
| `runs/client/config/ftbquests/` | **Active development & runtime** | NO | **YES** |
| `defaultconfigs/ftbquests/` | Distribution template for new worlds | YES | No (copied once) |
| `config/ftbquests/` | Git-tracked mirror of defaultconfigs | YES | No |

### The Golden Rules

1. **DEVELOP in `runs/client/config/ftbquests/`** - This is where the game actually reads quests
2. **TEST in-game** - The game loads from runs/client, so test there
3. **COPY to `defaultconfigs/` ONLY when a chapter is 100% complete and tested**
4. **SYNC `config/` to match `defaultconfigs/`** - These two should always be identical
5. **NEVER edit `config/` or `defaultconfigs/` directly** - Always copy FROM runs/client

### Data Flow (ONE DIRECTION ONLY)

```
SOURCE OF TRUTH: runs/client/config/ftbquests/
                           |
                           | Copy chapter when COMPLETE
                           v
DISTRIBUTION:    defaultconfigs/ftbquests/
                           |
                           | Keep in sync (copy or symlink)
                           v
GIT TRACKED:     config/ftbquests/
```

**NEVER reverse this flow.** Do not copy from config/ or defaultconfigs/ back to runs/client/.

### What Happens When You Break the Rules

| Mistake | Consequence |
|---------|-------------|
| Edit config/ directly | Changes don't appear in-game; work is wasted |
| Edit defaultconfigs/ directly | Changes don't appear until new world; may overwrite good work |
| Copy from config/ to runs/client/ | May overwrite newer/better work in runs/client/ |
| Forget to copy finished work to defaultconfigs/ | Work exists only in runs/ which isn't git-tracked |

### Step-by-Step: Adding a New Quest Chapter

```bash
# 1. DEVELOP: Create/edit quests in runs/client (use in-game editor or edit files)
runs/client/config/ftbquests/quests/chapters/my_chapter.snbt
runs/client/config/ftbquests/quests/lang/en_us.snbt  # Add localizations here

# 2. TEST: Run the game, verify everything works
./gradlew runClient

# 3. BACKUP: Save a golden copy before any more changes
cp runs/client/config/ftbquests/quests/chapters/my_chapter.snbt \
   runs/client/config/ftbquests/quests/chapters/my_chapter.snbt.golden

# 4. FINALIZE: When 100% complete, copy to defaultconfigs
cp runs/client/config/ftbquests/quests/chapters/my_chapter.snbt \
   defaultconfigs/ftbquests/quests/chapters/
cp runs/client/config/ftbquests/quests/lang/en_us.snbt \
   defaultconfigs/ftbquests/quests/lang/  # Or merge relevant entries

# 5. SYNC: Mirror to config/ for git tracking
cp defaultconfigs/ftbquests/quests/chapters/my_chapter.snbt \
   config/ftbquests/quests/chapters/

# 6. COMMIT: Now it's safe to commit
git add config/ftbquests/ defaultconfigs/ftbquests/
git commit -m "Add my_chapter quest chapter"
```

### Before Starting ANY Quest Work

1. **CHECK runs/client/ first** - This is where the real work lives
2. **BACKUP any existing work** in runs/client/ before making changes
3. **NEVER assume** config/ or defaultconfigs/ has the correct/latest version
4. **ASK yourself**: "Am I editing the right directory?"

### Disaster Recovery

If you've lost quest work:
1. **Check runs/client/config/** - The game may have preserved it
2. **Check for .golden files** - We save backups with .golden extension
3. **Check git stash**: `git stash list`
4. **Check world save**: `runs/client/saves/WORLDNAME/serverconfig/ftbquests/`

### Example of Properly Implemented Chapter: Occultism

The `occultism` chapter in this project serves as the reference implementation. Study its structure:
- Chapter file: `runs/client/config/ftbquests/quests/chapters/occultism.snbt`
- Lang entries in: `runs/client/config/ftbquests/quests/lang/en_us.snbt`
- Backup: `runs/client/config/ftbquests/quests/chapters/occultism.snbt.golden`

---

## Directory Structure

There are THREE locations for FTB Quests configs:

### 1. Source Location (defaultconfigs)
```
defaultconfigs/ftbquests/quests/
├── data.snbt                    # Global quest settings
├── chapter_groups.snbt          # Chapter group definitions
├── chapters/                    # Chapter definition files
│   ├── welcome.snbt
│   ├── survival_basics.snbt
│   └── ... (one file per chapter)
└── lang/
    └── en_us/
        ├── chapter.snbt         # NOT USED - see below
        └── chapters/            # NOT USED - see below
```

### 2. Runtime Location (runs/client/config)
```
runs/client/config/ftbquests/quests/
├── data.snbt
├── chapter_groups.snbt
├── chapters/
│   └── *.snbt
└── lang/
    ├── en_us.snbt               # THE MAIN LOCALIZATION FILE
    └── en_us/
        ├── chapter.snbt         # May or may not be read
        └── chapters/            # NOT USED by FTB Quests
```

**CRITICAL**: The game reads from `runs/client/config/` at runtime. The `defaultconfigs/` is only copied on first world creation.

### 3. Project Root config/ (DO NOT USE)
```
config/ftbquests/quests/          # NOT USED AT RUNTIME
├── chapters/                      # These files are NOT read by the game
└── lang/en_us/chapters/          # These files are NOT read by the game
```

**WARNING**: The `config/ftbquests/` directory at the project root is NOT used during gameplay. All quest chapters and localizations MUST be placed in `runs/client/config/ftbquests/` for the game to see them.

## Localization - THE MOST IMPORTANT PART

### The Main Localization File

**ALL localizations go in ONE file**: `lang/en_us.snbt`

This includes:
- Chapter titles
- Quest titles
- Quest subtitles
- Quest descriptions
- Task titles

### Localization Format

```snbt
{
    // Chapter Titles
    chapter.HEXID.title: "Chapter Name"

    // Quest Localizations
    quest.HEXID.title: "Quest Title"
    quest.HEXID.quest_subtitle: "Optional Subtitle"
    quest.HEXID.quest_desc: ["Description line 1\\n\\nDescription line 2"]

    // Task Titles (optional - only for checkmark tasks)
    task.HEXID.title: "Task Display Name"
}
```

### Key Format Rules

1. **IDs are 16-character hex strings** (e.g., `02FF33D22B10EA88`)
2. **Subtitle field is `quest_subtitle`** - NOT just `subtitle`
3. **Description field is `quest_desc`** - array format (see description format section below)
4. **Minecraft formatting codes work**: `&6` for gold, `&a` for green, `&b` for aqua, `&e` for yellow, `&o` for italic, `&l` for bold, `&r` to reset

### ID Format (CRITICAL)

**All IDs (quest, task, reward) MUST be exactly 16-character uppercase hex strings.**

Valid examples:
- `796C5F40115A5AE3`
- `02FF33D22B10EA88`
- `A4B61F409A13ECDB`

Invalid examples:
- `AE2001000000001` (only 15 characters)
- `quest_intro_1` (not hex)
- `1234567890abcdef` (lowercase - may work but uppercase preferred)

**When porting quests from other packs or creating quests manually:**
1. Do NOT use human-readable ID patterns like `AE2001000000001`
2. Generate random 16-character hex IDs using Python:
   ```python
   import random
   hex_id = ''.join(random.choices('0123456789ABCDEF', k=16))
   ```
3. Or let FTB Quests generate IDs by creating quests in-game

**If localizations are not showing (titles/descriptions display as blank or show the key):**
1. First check that the ID in the lang file matches the ID in the chapter file exactly
2. Verify the ID is exactly 16 characters long
3. Verify the ID contains only hex characters (0-9, A-F)

### Description Format (CRITICAL)

FTB Quests supports TWO formats for `quest_desc`. Use the **multi-line array format** for reliability:

**PREFERRED - Multi-line array format (for multi-paragraph descriptions):**
```snbt
quest.HEXID.quest_desc: [
    "First paragraph of text here."
    ""
    "Second paragraph here. The empty string above creates a paragraph break."
    ""
    "Third paragraph with &bformatting&f codes."
]
```

**Alternative - Single-line format (for short single-paragraph descriptions):**
```snbt
quest.HEXID.quest_desc: ["Short description on one line."]
```

**Key Points:**
- Use empty string `""` as array element for paragraph breaks
- Do NOT use `\\n\\n` for paragraph breaks (unreliable rendering)
- Each paragraph is a separate array element
- Formatting codes (`&b`, `&e`, etc.) work within any element

### What Does NOT Work

- `lang/en_us/chapters/*.snbt` - Individual chapter localization files are NOT read
- `lang/en_us/chapter.snbt` - Separate chapter file may not be reliably read
- Using `subtitle` instead of `quest_subtitle`

## Finding Correct IDs

### Chapter IDs
Each chapter file has an `id` field near the top:
```snbt
{
    filename: "welcome"
    id: "02FF33D22B10EA88"    // <-- This is the chapter ID
    ...
}
```

### Quest IDs
Each quest within a chapter has its own `id`:
```snbt
quests: [
    {
        id: "796C5F40115A5AE3"    // <-- Quest ID
        tasks: [{
            id: "016347000C29BEA0"   // <-- Task ID
            type: "checkmark"
        }]
    }
]
```

### Verification Process
1. Read the chapter file from `runs/client/config/ftbquests/quests/chapters/`
2. Extract the chapter `id` field
3. Extract each quest's `id` field
4. Extract task `id` fields for checkmark tasks
5. Use these exact IDs in `en_us.snbt`

**WARNING**: IDs in `defaultconfigs/` may differ from `runs/client/config/`. Always use the runtime IDs.

## Complete Example

### Chapter File (chapters/welcome.snbt)
```snbt
{
    filename: "welcome"
    id: "02FF33D22B10EA88"
    quests: [
        {
            id: "796C5F40115A5AE3"
            tasks: [{
                id: "016347000C29BEA0"
                type: "dimension"
            }]
        }
        {
            id: "4209DDD97D1E5861"
            tasks: [{
                id: "4D9A09E80739F58C"
                type: "checkmark"
            }]
        }
    ]
}
```

### Localization File (lang/en_us.snbt)
```snbt
{
    // Chapter title
    chapter.02FF33D22B10EA88.title: "Welcome"

    // First quest
    quest.796C5F40115A5AE3.title: "Welcome to mooStack!"
    quest.796C5F40115A5AE3.quest_desc: ["This is the description.\\n\\nSecond paragraph here."]

    // Second quest with checkmark task
    quest.4209DDD97D1E5861.title: "Pack Philosophy"
    quest.4209DDD97D1E5861.quest_subtitle: "Understanding the design"
    quest.4209DDD97D1E5861.quest_desc: ["Learn about the pack's design philosophy."]
    task.4D9A09E80739F58C.title: "I understand the philosophy"
}
```

## Workflow for Adding Quests

### Recommended Approach
1. **Create quests in-game** using FTB Quests edit mode
2. **Exit the game** to ensure files are saved
3. **Read the chapter files** from `runs/client/config/ftbquests/quests/chapters/`
4. **Extract all IDs** (chapter, quest, task)
5. **Add localizations** to `runs/client/config/ftbquests/quests/lang/en_us.snbt`
6. **Test in-game** - use `/reload` or reopen quest book

### Do NOT
- Write chapter files from scratch (IDs will mismatch)
- Use placeholder IDs and expect them to work
- Put localizations in `lang/en_us/chapters/` subdirectory
- Forget to include chapter titles in the main `en_us.snbt`

## Quest Task Types

Common task types and their requirements:
- `checkmark` - Manual completion, benefits from task title localization
- `item` - Collect/craft items, no title needed (shows item name)
- `dimension` - Visit a dimension, no title needed
- `kill` - Kill entities
- `location` - Visit coordinates
- `observation` - Look at something
- `xp` - Gain XP levels

## Troubleshooting

### "Unnamed" Chapters
- Chapter ID in localization doesn't match actual chapter file ID
- Chapter title not in main `en_us.snbt` file

### Quest Title/Description Not Showing
- Quest ID mismatch between localization and chapter file
- Wrong field name (e.g., `subtitle` instead of `quest_subtitle`)
- Localizations in wrong file (not main `en_us.snbt`)

### Changes Not Appearing
- Try `/reload` command
- Close and reopen quest book
- Restart client if needed
- Verify you edited the runtime config, not defaultconfigs

## File Locations Quick Reference

| Purpose | File Path |
|---------|-----------|
| Main localization | `runs/client/config/ftbquests/quests/lang/en_us.snbt` |
| Chapter definitions | `runs/client/config/ftbquests/quests/chapters/*.snbt` |
| Global settings | `runs/client/config/ftbquests/quests/data.snbt` |
| Chapter groups | `runs/client/config/ftbquests/quests/chapter_groups.snbt` |

## mooStack-Specific Notes

### Current Chapter IDs (Runtime)
These are the actual IDs from `runs/client/config/`:
- Welcome: `02FF33D22B10EA88`
- Applied Energistics 2: `4614511FF43DF71B`
- Create: `066DA60724499F83`
- Industrial Foregoing: `193F91842D2ED7D9`

**Note**: These IDs may change if chapters are recreated. Always verify against actual chapter files.

### Combined Lang File Structure
The main `runs/client/config/ftbquests/quests/lang/en_us.snbt` file contains ALL localizations for ALL chapters. When adding a new chapter:

1. Add a comment line to separate chapter sections: `// Chapter Name Chapter`
2. Add `chapter.HEXID.title: "Chapter Name"`
3. Add all `quest.*` entries for that chapter
4. Add all `task.*` entries for checkmark tasks

**DO NOT** create per-chapter lang files in `lang/en_us/chapters/` - these are NOT read by FTB Quests.

---

## Porting Quest Chapters from Other Modpacks

This section documents the complete process for porting FTB Quest chapters from reference modpacks (like ATM-10) to mooStack.

### Overview

Porting involves three main phases:
1. **Initial Port** - Copy/adapt quest structure and content
2. **ID Regeneration** - Generate valid 16-char hex IDs
3. **Dependency Alignment** - Ensure quest prerequisites match the source

### Phase 1: Initial Port

#### Step 1: Identify Source Chapter
```
Source: /path/to/reference/config/ftbquests/quests/chapters/chapter_name.snbt
Target: runs/client/config/ftbquests/quests/chapters/chapter_name.snbt
```

#### Step 2: Adapt Content
When copying from another modpack:
- Remove pack-specific reward tables (e.g., ATM loot tables)
- Replace with XP rewards and thematic item rewards
- Remove references to mods not in mooStack
- Adapt `ftbfiltersystem:smart_filter` tasks to regular `item` tasks if the mod isn't present

#### Step 3: Create Localizations
Extract all quest text and add to `lang/en_us.snbt`:
- Quest titles
- Quest subtitles
- Quest descriptions (use multi-line array format)
- Checkmark task titles

### Phase 2: ID Regeneration

**CRITICAL**: All IDs must be exactly 16 uppercase hex characters.

#### Generate New IDs
Use this Python script to regenerate all IDs in a chapter file:

```python
import re
import random

def generate_hex_id():
    return ''.join(random.choices('0123456789ABCDEF', k=16))

def regenerate_ids(content):
    # Find all 16-char hex IDs and replace with new ones
    id_map = {}

    def replace_id(match):
        old_id = match.group(1)
        if old_id not in id_map:
            id_map[old_id] = generate_hex_id()
        return f'"{id_map[old_id]}"'

    # Replace IDs in id: "..." patterns
    new_content = re.sub(r'"([A-F0-9]{16})"', replace_id, content)

    return new_content, id_map

# Usage:
with open('chapter.snbt', 'r') as f:
    content = f.read()

new_content, id_map = regenerate_ids(content)

with open('chapter.snbt', 'w') as f:
    f.write(new_content)

# Print mapping for updating lang file
for old_id, new_id in id_map.items():
    print(f"{old_id} -> {new_id}")
```

#### Update Lang File IDs
After regenerating chapter IDs, update the corresponding IDs in `lang/en_us.snbt` to match.

**IMPORTANT**: Run the ID regeneration on BOTH the chapter file and lang file together, or manually update the lang file to match the new chapter IDs.

### Phase 3: Dependency Alignment

This is the most important step to ensure quest flow matches the reference pack.

#### Step 1: Parse Both Chapter Files
Use this Python script to extract quest data:

```python
import re

def extract_quests_from_snbt(content):
    """Extract quests with their IDs, items, and dependencies."""
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

                    # Extract item IDs from tasks
                    items = []
                    item_matches = re.findall(r'id:\s*"(ae2:[^"]+|megacells:[^"]+|minecraft:[^"]+)"', quest_text)
                    items = list(dict.fromkeys(item_matches))

                    quests.append({
                        'id': quest_id,
                        'dependencies': deps,
                        'items': items
                    })

                current_quest_lines = []

    return quests
```

#### Step 2: Match Quests by Content
Since IDs differ between packs, match quests by their primary task item:

```python
def get_quest_key(quest):
    """Generate a key to match quests between packs."""
    # Filter to mod-specific items (not generic rewards)
    mod_items = [i for i in quest['items'] if i.startswith('ae2:') or i.startswith('megacells:')]
    if mod_items:
        return mod_items[0]  # Use first mod item as key
    return None

# Build key -> quest mappings for both packs
source_by_key = {get_quest_key(q): q for q in source_quests if get_quest_key(q)}
target_by_key = {get_quest_key(q): q for q in target_quests if get_quest_key(q)}
```

#### Step 3: Compare Dependencies
Convert dependency IDs to quest keys for comparison:

```python
def resolve_deps_to_keys(deps, id_to_quest_map):
    """Convert dependency IDs to quest keys."""
    keys = []
    for dep_id in deps:
        if dep_id in id_to_quest_map:
            dep_quest = id_to_quest_map[dep_id]
            key = get_quest_key(dep_quest)
            if key:
                keys.append(key)
    return sorted(keys)

# Find differences
differences = []
for key in source_by_key:
    if key in target_by_key:
        source_deps = resolve_deps_to_keys(source_by_key[key]['dependencies'], source_by_id)
        target_deps = resolve_deps_to_keys(target_by_key[key]['dependencies'], target_by_id)

        if source_deps != target_deps:
            differences.append({
                'key': key,
                'source_deps': source_deps,
                'target_deps': target_deps,
                'target_id': target_by_key[key]['id']
            })
```

#### Step 4: Generate Fixes
For each difference, determine the correct dependency IDs in the target pack:

```python
# Build key -> target ID mapping
target_key_to_id = {get_quest_key(q): q['id'] for q in target_quests if get_quest_key(q)}

fixes = []
for diff in differences:
    target_dep_ids = []
    for dep_key in diff['source_deps']:
        if dep_key in target_key_to_id:
            target_dep_ids.append(target_key_to_id[dep_key])

    fixes.append({
        'quest_id': diff['target_id'],
        'quest_key': diff['key'],
        'current_deps': diff['target_deps'],
        'target_deps': target_dep_ids
    })
```

#### Step 5: Apply Fixes
Apply each fix to the chapter file:

**Adding dependencies** (quest has no dependencies but should):
```snbt
// Before
{
    id: "QUESTID123456789"
    rewards: [...]

// After
{
    dependencies: ["DEPID1234567890"]
    id: "QUESTID123456789"
    rewards: [...]
```

**Replacing dependencies** (quest has wrong dependencies):
```snbt
// Before
dependencies: ["WRONGID12345678"]

// After
dependencies: ["CORRECTID123456"]
```

**Removing dependencies** (quest shouldn't have dependencies):
Simply delete the `dependencies: [...]` line.

### Handling Pack-Specific Differences

Some differences are expected when mods differ between packs:

#### Combined Quests
If the source pack has two separate quests but your pack combines them:
- Set dependencies to point to the combined quest
- Document this as an expected difference

Example: ATM-10 has separate "Pattern Provider" and "Pattern Access Terminal" quests, but mooStack combines them. Quests that depend on Pattern Access Terminal should depend on the combined Pattern Provider quest in mooStack.

#### Missing Mods
If a dependency quest uses a mod not in your pack:
- Find the closest equivalent quest in your pack
- Or make the quest a ROOT quest (no dependencies)
- Document the adaptation

### Verification

After applying fixes, run the comparison script again to verify:

```python
# Should output:
# Remaining differences: 0
# or
# Remaining differences: N (expected - combined quests, missing mods, etc.)
```

### CRITICAL: Game Will Regenerate IDs

**WARNING**: FTB Quests will regenerate ALL IDs when loading a chapter file for the first time. This will:
1. Replace your carefully generated IDs with new random ones
2. Break all dependency references (they still point to old IDs)
3. Break all lang file references (they still use old IDs)

### Golden Rule: Never Trust FTB Quests to Preserve IDs on First Load

This is the most important lesson for FTB Quests development. **Accept that FTB Quests will regenerate IDs** and work WITH this behavior rather than fighting it.

#### Safe Workflow (Strongly Recommended)

1. **Create chapter structure** (file + quests with any placeholder IDs)
2. **Load world once** - let FTB Quests process the file
3. **Let FTB Quests generate IDs** - it will assign stable IDs to everything
4. **Immediately back up the transformed file**:
   ```bash
   cp runs/client/config/ftbquests/quests/chapters/your_chapter.snbt \
      runs/client/config/ftbquests/quests/chapters/your_chapter.snbt.golden
   ```
5. **Extract the stable IDs** from the game-generated file
6. **Update lang file** to match the stable IDs
7. **Test** - localizations should now work

#### From That Point On

- **Treat IDs as immutable** - never change them
- **Only edit content, not structure** - titles, descriptions, rewards are safe
- **Never delete/recreate chapters casually** - this triggers ID regeneration

#### For Cross-Chapter Dependencies

When wiring dependencies between chapters:
1. Finish both chapters first
2. Let IDs stabilize (load world once per chapter)
3. Then wire cross-chapter dependencies using the stable IDs
4. Back up again

#### Recovery Strategies

**If you still need to fight ID regeneration (not recommended):**
1. **Do NOT run the game** after copying the chapter file until all verification is complete
2. **Copy the file immediately** before testing - have a backup ready
3. **Verify immediately after game launch** - if IDs changed, restore from backup
4. **Consider disabling FTB Quests** during initial setup (rename jar temporarily)

**If the game regenerates your IDs (and you want to restore):**
1. Close the game
2. Restore the chapter file from your backup (temp file or source)
3. Do NOT let the game load with the old chapter again
4. Compare files to verify restoration: `diff backup.snbt current.snbt`

**Recommended: Just work with the new IDs** - extract them and update your lang file instead of fighting the regeneration.

### Complete Porting Checklist

- [ ] Copy source chapter file
- [ ] Remove pack-specific content (reward tables, unavailable mods)
- [ ] Adapt task items (smart_filter -> item if needed)
- [ ] Generate new 16-char hex IDs for all quests, tasks, rewards
- [ ] Create localizations in lang/en_us.snbt with matching IDs
- [ ] **BACKUP the transformed chapter file before testing**
- [ ] Run dependency comparison script
- [ ] Apply dependency fixes
- [ ] Verify all dependencies match (or document expected differences)
- [ ] Test in-game:
  - [ ] All quests visible
  - [ ] All titles/descriptions display
  - [ ] Dependency lines show correctly
  - [ ] Quest completion works
- [ ] Create port notes document (see `docs/quests/ae2_port_notes.md` for example)

### Example Port Notes Document

Create a document at `docs/quests/MODNAME_port_notes.md` with:
- Source pack and chapter
- Quest count comparison
- What was removed/changed
- Dependency adaptations made
- Expected differences
- Testing recommendations

### Final Verification: Lang Entry Analysis

After porting a chapter, run this verification script to ensure all descriptions and subtitles from the source pack were copied correctly:

```python
import re

# Paths - adjust as needed
ATM_LANG = '/path/to/ATM-10/config/ftbquests/quests/lang/en_us/chapters/CHAPTER.snbt'
MOO_LANG = 'runs/client/config/ftbquests/quests/lang/en_us.snbt'
MOO_CHAPTER = 'runs/client/config/ftbquests/quests/chapters/CHAPTER.snbt'

# Read files
with open(ATM_LANG, 'r') as f:
    atm_content = f.read()
with open(MOO_LANG, 'r') as f:
    moo_content = f.read()
with open(MOO_CHAPTER, 'r') as f:
    chapter_content = f.read()

# Known removed content (ATM copyright notices, etc.)
removed_quests = {'2F69010E1FA2787D'}  # AllRightsReserved
removed_tasks = {'6B17A0D9906E8C90', '7058D3373DA87B34'}

# Extract entries from ATM
atm_subtitles = set(re.findall(r'quest\.([A-F0-9]{16})\.quest_subtitle:', atm_content))
atm_descs = set(re.findall(r'quest\.([A-F0-9]{16})\.quest_desc:', atm_content))
atm_task_titles = set(re.findall(r'task\.([A-F0-9]{16})\.title:', atm_content))

# Extract entries from mooStack
moo_subtitles = set(re.findall(r'quest\.([A-F0-9]{16})\.quest_subtitle:', moo_content))
moo_descs = set(re.findall(r'quest\.([A-F0-9]{16})\.quest_desc:', moo_content))
moo_task_titles = set(re.findall(r'task\.([A-F0-9]{16})\.title:', moo_content))

# Count quests in chapter
quest_ids = re.findall(r'^\t\t\tid:\s*"([A-F0-9]{16})"', chapter_content, re.MULTILINE)

print("=" * 60)
print("LANG ENTRY VERIFICATION")
print("=" * 60)

# Check subtitles
atm_subtitles_excl = atm_subtitles - removed_quests
missing_subtitles = atm_subtitles_excl - moo_subtitles
print(f"\nSubtitles: {len(atm_subtitles_excl)} in ATM, {len(moo_subtitles & atm_subtitles_excl)} in mooStack")
if missing_subtitles:
    print(f"  MISSING: {missing_subtitles}")
else:
    print("  All present!")

# Check descriptions
atm_descs_excl = atm_descs - removed_quests
missing_descs = atm_descs_excl - moo_descs
print(f"\nDescriptions: {len(atm_descs_excl)} in ATM, {len(moo_descs & atm_descs_excl)} in mooStack")
if missing_descs:
    print(f"  MISSING: {missing_descs}")
else:
    print("  All present!")

# Check task titles
atm_tasks_excl = atm_task_titles - removed_tasks
missing_tasks = atm_tasks_excl - moo_task_titles
print(f"\nTask titles: {len(atm_tasks_excl)} in ATM, {len(moo_task_titles & atm_tasks_excl)} in mooStack")
if missing_tasks:
    print(f"  MISSING: {missing_tasks}")
else:
    print("  All present!")

# Summary
print(f"\nTotal quests in chapter: {len(quest_ids)}")
all_good = not missing_subtitles and not missing_descs and not missing_tasks
print(f"\nRESULT: {'PASS' if all_good else 'FAIL'}")
```

#### What to Verify

| Category | Description |
|----------|-------------|
| **Subtitles** | All `quest.HEXID.quest_subtitle` entries from ATM are in mooStack |
| **Descriptions** | All `quest.HEXID.quest_desc` entries from ATM are in mooStack |
| **Task Titles** | All `task.HEXID.title` entries (for checkmark tasks) are in mooStack |
| **Quest Titles** | All quests have explicit titles (mooStack should have MORE than ATM since ATM relies on item names for some) |

#### Expected Exclusions

When comparing against ATM, these entries should be intentionally excluded:
- `quest.2F69010E1FA2787D` - ATM AllRightsReserved copyright notice
- `task.6B17A0D9906E8C90` - ATM AllRightsReserved task
- `task.7058D3373DA87B34` - ATM AllRightsReserved task

#### Success Criteria

A successful port should show:
- All ATM subtitles present (minus copyright)
- All ATM descriptions present (minus copyright)
- All ATM task titles present (minus copyright)
- mooStack has MORE quest titles than ATM (all 70 vs ATM's ~20 explicit titles)
