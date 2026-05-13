# WILDLIFE PIPELINE MAPPING

[IDEA_GENERATOR]
# IDEA_GENERATOR.md (Output: Title, Hook, Wow Factor, Items)
MAPPINGS = {
  "TITLE": "title",
  "C1": "items[0]",
  "C2": "items[1]",
  "C3": "items[2]",
  "C4": "items[3]",
  "C5": "items[4]",
  "C6": "items[5]",
  "C7": "items[6]",
  "C8": "items[7]"
}

[SCRIPT_WRITER]
# SCRIPT_WRITER.md (Output: Title, Script_Body)
MAPPINGS = {
  "TITLE": "title",
  "SCRIPT_BODY": "script_body"
}

[THUMBNAIL_GENERATOR]
# THUMBNAIL_GENERATOR.md (Output: Title, Visual, Text, Prompt)
MAPPINGS = {
  "PROMPT": "prompt"
}

[VISUAL_PROMPT_MAKER]
# VISUAL_PROMPT_MAKER.md (Output: Scene_Text, Image_Prompt, Video_Prompt, Stock_Query, Overlay_Text)
MAPPINGS = {
  "VISUAL_PLAN": "visual_plan[*]"
}
