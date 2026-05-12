# Script Models

Registry containing prompt/model collections for **Script Pro**.

**👉 Download models:** Use the `plugin.json` link below in your tool/extension:

```
https://raw.githubusercontent.com/2noScript/script-models/main/plugin.json
```

## Structure

```
script-models/
├── plugin.json              # 🔸 Main file — load into tool to receive model list
├── core/
│   └── wildlife/            # Model: Wildlife & Science Creators
│       ├── manifest.json    # Metadata + mapping script files
│       ├── icon.png         # 128×128 PNG Icon
│       ├── SCRIPT WRITER.md
│       ├── THUMBNAIL GENERATOR.md
│       ├── VIDEO IDEA GENERATOR.md
│       └── VISUAL & IMAGE PROMPT MAKER.md
└── helper/                  # Helper tools (Python)
    ├── convert.py           # Automatic icon processing
    ├── pyproject.toml
    ├── uv.lock
    └── README.md
```

## plugin.json — Registry

The **only** file users need to load. Contains the complete list of models:

```json
{
  "metadata": {
    "author": "2noScript",
    "description": "Gen Script Pro"
  },
  "data": [
    {
      "name": "Wildlife & Science Creators",
      "author": "2noScript",
      "path": "https://raw.githubusercontent.com/2noScript/script-models/main/core/wildlife/manifest.json",
      "version": 1,
      "icon": "https://raw.githubusercontent.com/2noScript/script-models/main/core/wildlife/icon.png",
      "description": "Ready-to-Use Prompts for Wildlife & Science Creators",
      "tags": ["Youtube"]
    }
  ]
}
```

## Model Structure

Each model is a subdirectory in `core/` (example: `core/wildlife/`).

### manifest.json

```json
{
  "metadata": {
    "name": "<model>",
    "author": "2noScript",
    "version": 1,
    "description": "..."
  },
  "script": {
    "idea": "<file>.md",
    "script": "<file>.md",
    "thumbnail": "<file>.md",
    "visuals": "<file>.md"
  }
}
```

### Script Files (`.md`)

Each Markdown file contains prompts for a step in the content production workflow:

- **SCRIPT WRITER.md** — write script
- **THUMBNAIL GENERATOR.md** — create thumbnail
- **VIDEO IDEA GENERATOR.md** — video ideas
- **VISUAL & IMAGE PROMPT MAKER.md** — create image prompts

### icon.png

Icon representing the model, standard **128×128 PNG**.

## helper/ — Icon Tool

Used to automatically standardize icons for all models.

### convert_first_images_to_icons()

Automatically finds the first image file (alphabetically sorted) in each subdirectory of `core/` and standardizes it to `icon.png`:

- Size → `(128, 128)` if not already correct
- Format → PNG if not already PNG
- Name → `icon.png` if not already named correctly

If the image already meets all 3 conditions → skipped.

### convert_all_to_png(input_folder, size=None)

Batch convert images in a folder to PNG, saving to `converted/` directory.

### Usage

```bash
cd helper
uv run python convert.py
```

Requirements: Python ≥ 3.12, Pillow.

## Adding a New Model

1. Create directory: `mkdir core/<model>`
2. Create `manifest.json` and `.md` files
3. Add images to the directory (any format/size)
4. Run `uv run python convert.py` to automatically create standardized `icon.png`
5. Add entry to `plugin.json`