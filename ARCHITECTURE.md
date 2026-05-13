# Script Pro: Data Flow Architecture

This document describes the standardized architecture for the AI-powered content generation pipeline in Script Pro.

## 1. Core Principles

- **Standardization**: All script models (`.md` files) follow a strict 3-section structure.
- **Explicit Schema**: Every model defines an `[OUTPUT SCHEMA]` to guide AI responses.
- **Zero-Config Mapping**: Data propagation between steps is handled by an AI Mapper using `MAP.md` as a guide.
- **User Agency**: When AI produces multiple options, the user must explicitly select one to proceed.

## 2. File Structure

Each script plugin folder (e.g., `wildlife/`) contains:

| File | Role |
| :--- | :--- |
| `plugin.json` | Manifest linking tabs (Idea, Script, etc.) to filenames. |
| `MAP.md` | Defines explicit mapping paths (e.g., `TITLE = niches[0].ideas[0].title`). |
| `IDEA_GENERATOR.md` | Phase 1: High-level ideation (usually multi-result). |
| `SCRIPT_WRITER.md` | Phase 2: Detailed content generation based on an idea. |
| `...` | Subsequent phases (Thumbnail, Visuals, etc.). |

## 3. Data Pipeline Lifecycle

### Phase 1: Generation & Detection
1. The user triggers an AI generation in a tab (e.g., `Idea`).
2. The AI returns a JSON response following the `[OUTPUT SCHEMA]`.
3. The system automatically detects if the JSON contains multiple selectable items (e.g., a list of ideas).

### Phase 2: Interactive Selection
1. If multiple results are found, the UI renders **Selection Cards**.
2. The user clicks "Chọn ý tưởng này" on a specific card.
3. This action isolates the JSON data for **only** that selected item.

### Phase 4: AI-Powered Mapping
1. The `mapVariablesWithAI` server action is called with:
   - The selected item's JSON.
   - The list of **all variables** needed by all other tabs in the plugin.
   - The rules defined in `MAP.md`.
   - The `sourceContext` (current tab key).
2. The AI Mapper extracts the values and updates the **Shared Context** (`sharedData`).

### Phase 5: Variable Consumption
1. When the user switches to a subsequent tab (e.g., `Script`), the component detects matching keys in `sharedData`.
2. The input form is **automatically populated** with the mapped values.

## 4. Mapping Rule Syntax (`MAP.md`)

The `MAP.md` file uses a simple INI-like section format with `KEY = PATH` rules:

```markdown
[IDEA_GENERATOR]
# Simple path extraction
TITLE = niches[0].ideas[0].title
# Sequential item extraction
C1 = niches[0].ideas[0].items[0]

[SCRIPT_WRITER]
# Joining array fields with wildcards
SCRIPT_BODY = segments[*].{creature, content}
```

## 5. Standardized Variables (Hard Interface)

To ensure consistency across different niches, all video plugins should map their outputs to these **Reserved Standard Variables**:

| Variable | Description |
| :--- | :--- |
| `TITLE` | The subject or main title of the content. |
| `HOOK` | The opening attention-grabbing sentence. |
| `C1` - `C8` | Core content points (Facts, Ingredients, Steps, etc.). |
| `SCRIPT_BODY` | The primary generated text/script. |
| `VISUAL_PLAN` | The final structured production/visual plan. |

### The "Soft-Hard" Hybrid Principle:
- **Soft**: The AI prompts use niche-specific terminology (e.g., `dish_name`, `animal_fact`).
- **Hard**: `MAP.md` acts as a translator, mapping these "Soft" fields into the "Hard" reserved variables.
- **Result**: Downstream steps can be standardized because they only need to know about the "Hard" variables.

- **ItemDetail.tsx**: Manages the `sharedData` state and aggregates `allVariables` from all tab templates.
- **ChatTester.tsx**: 
  - Handles the conversation and JSON detection.
  - Renders the selection UI.
  - Triggers the `mapVariablesWithAI` action.
  - Syncs its local `formValues` with the global `sharedData`.

---

> [!NOTE]
> This architecture ensures that even if the underlying AI prompts change, the data flow remains stable as long as the `MAP.md` and `[OUTPUT SCHEMA]` are updated to match.
