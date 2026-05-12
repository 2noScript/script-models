# WILDLIFE PIPELINE MAPPING

[IDEA_GENERATOR]
# VIDEO IDEA GENERATOR.md
# Map keys from JSON response to global variables
MAPPINGS = {
  "TITLE": "niches[0].ideas[0].title",
  "C1": "niches[0].ideas[0].items[0]",
  "C2": "niches[0].ideas[0].items[1]",
  "C3": "niches[0].ideas[0].items[2]",
  "C4": "niches[0].ideas[0].items[3]",
  "C5": "niches[0].ideas[0].items[4]",
  "C6": "niches[0].ideas[0].items[5]",
  "C7": "niches[0].ideas[0].items[6]",
  "C8": "niches[0].ideas[0].items[7]"
}

[SCRIPT_WRITER]
# SCRIPT WRITER.md
# Map keys from JSON response to global variables
MAPPINGS = {
  "TITLE": "title",
  "SCRIPT_CONTENT": "segments[*].{creature, content}"
}

[THUMBNAIL_GENERATOR]
# THUMBNAIL GENERATOR.md
# Uses TITLE, C1, C2, C3, C4, C5, C6, C7, C8

[VISUAL_PROMPT_MAKER]
# VISUAL & IMAGE PROMPT MAKER.md
# Uses SCRIPT_CONTENT
