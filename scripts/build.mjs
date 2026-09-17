import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { build } from './publish.mjs';
const root = fileURLToPath(new URL('../', import.meta.url));
const output = path.join(root, 'dist');
// Only generated output is replaced; manuscript and engine sources are untouched.
fs.rmSync(output, { recursive: true, force: true });
for (const [name, body] of build(root)) {
  fs.mkdirSync(path.dirname(path.join(output, name)), { recursive: true });
  fs.writeFileSync(path.join(output, name), body);
}
console.log('Built static book in dist/');
