---
name: no-ai-slop
description: Use this skill whenever writing, formatting, or reviewing markdown output (reports, documentation, write-ups, README files, articles, or any text destined for a document) to strip out "AI slop" formatting tells. Enforces zero em/en dashes (replaced with real punctuation), straight quotes, no decorative emoji, sentence-case headings, no bold-colon list headers, no mechanical rule-of-three, no filler intros/outros, and natural heading/list density instead of over-structured output. Also covers Indonesian-language AI tells (frasa klise seperti "tidak hanya... tetapi juga", "hal ini menunjukkan bahwa", kata formal berlebihan). Trigger this any time the user asks to remove long dashes / tanda pisah panjang, make markdown look more human, clean up AI-sounding formatting, or mentions "ai slop", "ciri khas AI", "biar gak kelihatan AI", in either English or Indonesian.
---

# Clean Markdown: Eliminate AI Slop

Goal: markdown that reads like a careful human wrote it directly in a text editor, not like a chatbot dumped a formatted answer. This applies to the final document, not to conversational chat replies.

## Rule 1: No long dashes, ever

Never output an em dash (—) or en dash (–) as punctuation. This is the single most common AI tell and the one to check first.

Replace it depending on what job the dash was doing:

| Dash was doing this | Replace with |
|---|---|
| Joining two independent clauses | Split into two sentences, or use a comma + conjunction |
| Adding a parenthetical aside | Use parentheses, or a comma pair |
| Introducing a summary/definition | Use a colon |
| Standing in for "to" in a range (2020—2023) | Use an en-less hyphen or the word "to": 2020-2023 / 2020 to 2023 |

Before: `The exploit works — but only on unpatched versions — and requires local access.`
After: `The exploit works, but only on unpatched versions. It also requires local access.`

Before (Indonesian): `Tools ini efektif — namun hanya untuk skenario tertentu — dan tetap butuh akses fisik.`
After: `Tools ini efektif untuk skenario tertentu, tapi tetap butuh akses fisik.`

A plain hyphen used correctly (compound words: state-of-the-art, or an actual bullet marker `- like this`) is fine. What is banned is the dash-as-punctuation habit, not the character itself.

Also flag: a markdown horizontal rule (`---`) dropped between every section as a fake divider. Reserve it for genuine top-level breaks, not decoration after each paragraph.

## Rule 2: other formatting slop to hunt down

1. **Bold-colon list headers.** `- **Performance:** it got faster` for every bullet. Rewrite as prose, or drop the bold if a list genuinely helps.
2. **Title Case Headings.** `## Strategic Negotiations And Global Partnerships` → `## Strategic negotiations and global partnerships`.
3. **Decorative emoji** on headings or bullets (🚀, ✅, 💡). Remove unless the user's own style uses them.
4. **Curly quotes and ellipsis glyphs** (" " ' ' …). Use straight quotes and three literal periods.
5. **Rule-of-three padding.** Reaching for exactly three adjectives or three examples every single time. Vary the count, or cut to what's actually needed.
6. **Everything-is-a-bulleted-list.** Narrative or explanatory content forced into bullets. Use prose for reasoning and narrative; reserve lists for things that are genuinely enumerable (steps, items, options).
7. **Throwaway "conclusion" section** that just restates what was already said. Cut it, or replace with one concrete next step if one exists.
8. **Heading inflation.** H1 → H2 → H3 → H4 nesting for a two-page document. Flatten to what the content actually needs.
9. **Numbered steps where order doesn't matter.** Use bullets or prose instead of implying a sequence that isn't real.
10. **Bolding whole sentences.** Bold sparingly, on the two or three words that are actually the key term.
11. **Formulaic transition words** at the start of consecutive paragraphs (Additionally, Moreover, Furthermore). Vary the opener or delete it.
12. **Leftover chat residue** in a document body: "Here's an overview...", "I hope this helps!", "Berikut adalah...", "Semoga membantu!". A document should read as if it was authored directly, not pasted from a conversation.

## Rule 3: Indonesian-specific tells

Bahasa Indonesia formal AI-generated text has its own fingerprints, separate from English ones:

- Frasa klise berulang: "tidak hanya... tetapi juga", "hal ini menunjukkan bahwa", "secara keseluruhan", "dalam rangka untuk", "berbagai macam", "memainkan peran penting/krusial".
- Kata formal yang dijejalkan berlebihan: signifikan, esensial, krusial, komprehensif, optimal, muncul di hampir tiap paragraf.
- Em dash sama sekali tidak natural dalam tulisan formal Indonesia. Tulisan manusia Indonesia memakai tanda kurung, titik dua, atau kalimat baru, bukan tanda pisah panjang.

Before: `Penelitian ini tidak hanya menunjukkan hasil yang signifikan, tetapi juga membuka berbagai macam peluang riset lanjutan — sebuah langkah krusial bagi perkembangan bidang ini.`
After: `Penelitian ini menunjukkan hasil yang kuat dan membuka beberapa peluang riset lanjutan.`

## Process for cleaning a document

1. Read the whole file first before touching anything.
2. Optionally run `scripts/scan_slop.py <file>` as a fast first pass. It only reports line numbers and matches, it does not auto-edit, because a real fix needs judgment.
3. Rewrite section by section against Rules 1-3. Preserve meaning and technical accuracy exactly: never alter code, commands, flag values, numbers, or proper nouns while cleaning the prose around them. This matters especially for CTF write-ups, technical reports, or anything with exact strings that must stay byte-for-byte correct.
4. Do a final pass specifically searching for the — and – characters and curly quotes; these are the easiest to miss by eye.
5. Report back briefly what categories were fixed. Don't produce a line-by-line diff essay unless asked.

## Delivery checklist

- [ ] No — or – anywhere in the text
- [ ] No curly quotes or curly apostrophes
- [ ] No decorative emoji
- [ ] Headings are sentence case
- [ ] No bold-colon list-header pattern repeated throughout
- [ ] No throwaway "in conclusion" / "kesimpulan" ending
- [ ] Lists used only where content is genuinely list-shaped
- [ ] Code, commands, flags, and exact technical strings are untouched
