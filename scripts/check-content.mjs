import { readFile, readdir } from "node:fs/promises";
import { dirname, join, normalize, relative } from "node:path";
import process from "node:process";

const root = join(process.cwd(), "site");
const required = [
  "index.html",
  "book/01-first-distinction/index.html",
  "reference/index.html",
  "assets/styles.css",
  "assets/book.js",
  "assets/engine/computer.js",
  "assets/engine/approximation.js",
  "assets/engine/bit-machine.js",
  "assets/engine/bit-proof.js"
];

async function filesBelow(directory) {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const path = join(directory, entry.name);
    files.push(...(entry.isDirectory() ? await filesBelow(path) : [path]));
  }
  return files;
}

const allFiles = await filesBelow(root);
const relativeFiles = new Set(allFiles.map((file) => relative(root, file)));
const errors = [];

for (const file of required) {
  if (!relativeFiles.has(file)) errors.push(`missing required file: ${file}`);
}

for (const file of allFiles.filter((path) => path.endsWith(".html"))) {
  const html = await readFile(file, "utf8");
  if (!html.includes("data-conmath-page=")) {
    errors.push(`missing page metadata: ${relative(root, file)}`);
  }

  const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
  if (new Set(ids).size !== ids.length) errors.push(`duplicate IDs: ${relative(root, file)}`);
  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const href = match[1];
    if (/^(https?:|mailto:)/.test(href)) continue;
    const withoutHash = href.split("#")[0];
    if (!withoutHash) {
      if (!ids.includes(href.slice(1))) errors.push(`broken anchor in ${relative(root, file)}: ${href}`);
      continue;
    }
    const target = normalize(join(dirname(file), withoutHash));
    const candidates = [target, join(target, "index.html")];
    if (!candidates.some((candidate) => allFiles.includes(candidate))) {
      errors.push(`broken link in ${relative(root, file)}: ${href}`);
    } else if (href.includes('#')) {
      const destination = candidates.find(candidate => allFiles.includes(candidate));
      const destinationHtml = await readFile(destination, 'utf8');
      if (!destinationHtml.includes(`id="${href.split('#')[1]}"`)) errors.push(`broken destination anchor in ${relative(root, file)}: ${href}`);
    }
  }
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}

console.log(
  `Content check passed: ${allFiles.length} files, ${allFiles.filter((file) => file.endsWith(".html")).length} pages.`
);
