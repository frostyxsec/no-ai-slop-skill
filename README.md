# No AI Slop Skill

A Agent Skill that catches the formatting habits that make markdown read as AI-written. Its main target is the em dash and en dash, but it also flags curly quotes, bold-colon list headers, decorative emoji, title case headings, and a set of clichéd phrases in both English and Indonesian.

## Why

Most AI writing has a handful of visual tells: the dash used as glue between clauses, headings capitalized like a movie title, bullet lists where every item starts with a bolded word and a colon. None of it is wrong exactly, it just gives away that a model produced the text instead of a person. This skill packages a checklist and a small scanner so cleanup is quick and consistent instead of ad hoc.

## What it catches

- Em and en dashes used as punctuation
- Curly quotes and curly apostrophes
- Bold-colon list headers, like `- **Performance:** it got faster`
- Title case headings
- Decorative emoji on headings or bullets
- Rule-of-three padding and formulaic transition words
- Throwaway "in conclusion" endings that just restate the text
- Leftover chat phrasing pasted into a document ("Here's an overview...", "I hope this helps!")
- Indonesian-specific clichés: "tidak hanya... tetapi juga", "hal ini menunjukkan bahwa", "berbagai macam", and similar

The full checklist with before/after examples lives in `SKILL.md`.

## Files

```
clean-markdown/
├── SKILL.md              instructions agents reads when the skill triggers
└── scripts/
    └── scan_slop.py       standalone regex scanner, first-pass only
```
## Using the scanner on its own

`scan_slop.py` works without agents too, as a plain first-pass linter:

```bash
python3 scripts/scan_slop.py path/to/file
```

It only reports line numbers and matches. It does not rewrite anything, since deciding how to fix a sentence needs judgment that a regex doesn't have, especially in technical writing where code, commands, and exact strings have to stay untouched.

## Scope and limits

The pattern list is not exhaustive and skews toward what shows up in English and Indonesian technical writing. If you hit a pattern it misses, add it to `CLICHE_PHRASES_EN` or `CLICHE_PHRASES_ID` in the script, or extend the `CHECKS` list for anything regex can catch. Pull requests welcome.

## License

MIT. See `LICENSE`.

