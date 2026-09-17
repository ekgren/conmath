# Book design

Status: agreed direction. The first chapter is the editorial test.

## Readers and purpose

Write for anyone interested in mathematics and science, including engineers and
mathematicians. Teach prerequisites in the content or linked supporting pages;
do not require prior proof-assistant or logic knowledge. Accessibility does not
mean avoiding precise definitions.

After the first substantial part, a reader should understand, implement, and
reason about foundational constructions, addition, and some of its properties.
The first review milestone is smaller: one complete opening chapter.

## Content organization

- Parts group a mathematical development.
- Chapters provide an ordered reading path on separate pages.
- Sections give stable, directly linkable steps within a chapter.
- Concept pages provide definitions, rules, and supporting explanations that
  readers may visit as needed.
- A book-wide index exposes the hierarchy and links the references.

The catalogue is [book/catalog.json](../../book/catalog.json). Keep draft roadmap
entries visibly planned. Do not publish empty pages that pretend to be chapters.
Stable IDs are independent of chapter numbering and display titles.

The reading path and references serve different purposes. Put each authoritative
formal definition in one reference location; explain and use it in chapters.
Cross-link prerequisites. Avoid forcing readers into a graph explorer to read.

## Writing

Use plain words and concrete mechanisms. Give each sentence a job. Define terms
when they become necessary. Formal language and notation must clarify a claim,
not signal sophistication. Precise statements and proofs still matter.

Begin in the spirit of a good foundations book: objects, equality, construction
rules, and successor. Introduce the computer model as needed to explain how those
constructions exist and execute. Do not start with transistors, CMOS, or a general
hardware survey. The precise opening is not yet written or approved.

A useful chapter progression is motivation → definition → representation → code
→ evidence → resource account. Treat it as a teaching aid, not a rigid template.
Tie explanations to the actual code. Distinguish a run, a test, a prose argument,
a conjecture, and a checked proof.

See the user's [writing and visual references](../references/influences.md).

## Appearance and interaction

Aim for the care of an early-20th-century mathematical book: excellent typography,
legible mathematics, deliberate spacing, and diagrams worth studying. Establish
basic typography early. Do not build elaborate layouts before the content works.

Code is visible and runnable, but not editable by the reader. Inputs and resource
controls may be adjustable where useful. The source shown must be the source run.
An interaction should explain a construction, reveal state, or inspect evidence.
It should not be decoration or a replacement for the explanation.

Reading, navigation, and notation should remain usable without JavaScript.
Execution progressively enhances the page. Preserve keyboard access, readable
contrast, small-screen layouts, and reduced-motion preferences.

## Delivery

Publish static assets. All reader computation occurs in the browser. No backend,
login, API key, or third-party execution service is required. A locally served copy
must work. Opening an HTML file through `file://` is not an acceptance requirement.
Bundle necessary fonts, notation resources, and execution code with the site.

Hosting provider, framework, fonts, math renderer, and publishing format are not
yet chosen. Choose the smallest suitable tools when building the first chapter.
