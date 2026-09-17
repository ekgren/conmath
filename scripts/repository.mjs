import fs from 'node:fs';
import path from 'node:path';

const ignored = new Set(['.git', 'node_modules', 'dist', 'artifacts']);

export function filesUnder(root, prefix = '') {
  return fs.readdirSync(path.join(root, prefix), { withFileTypes: true })
    .sort((a, b) => a.name.localeCompare(b.name))
    .flatMap((entry) => {
      if (ignored.has(entry.name)) return [];
      const relative = path.posix.join(prefix, entry.name);
      if (entry.isSymbolicLink()) throw new Error(`Repository source must not be a symlink: ${relative}`);
      return entry.isDirectory() ? filesUnder(root, relative) : [relative];
    });
}

export function stripCode(source) {
  return source.replace(/^\s*(`{3,}|~{3,})[^\n]*\n[\s\S]*?^\s*\1\s*$/gm, '')
    .replace(/`[^`\n]+`/g, '');
}

function headingIds(source) {
  const ids = new Set();
  const used = new Map();
  for (const match of stripCode(source).matchAll(/^#{1,6}\s+(.+)$/gm)) {
    const base = match[1].toLowerCase().replace(/[^\p{L}\p{N}_\-\s]/gu, '').trim().replace(/\s/g, '-');
    const occurrence = used.get(base) ?? 0;
    used.set(base, occurrence + 1);
    ids.add(occurrence ? `${base}-${occurrence}` : base);
  }
  for (const match of source.matchAll(/\bid=["']([^"']+)["']/g)) ids.add(match[1]);
  return ids;
}

export function checkMarkdown(root, name) {
  const source = fs.readFileSync(path.join(root, name), 'utf8');
  const errors = [];
  for (const match of stripCode(source).matchAll(/!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)/g)) {
    const target = match[1].replace(/^<|>$/g, '');
    if (/^https?:\/\/|^mailto:/.test(target)) continue;
    if (/^[a-z][a-z0-9+.-]*:/i.test(target) || target.startsWith('/')) {
      errors.push(`${name}: use a repository-relative local link: ${target}`);
      continue;
    }
    let decoded;
    try { decoded = decodeURIComponent(target); }
    catch { errors.push(`${name}: malformed link ${target}`); continue; }
    const [pathname, fragment] = decoded.split('#');
    const resolved = pathname ? path.resolve(root, path.dirname(name), pathname) : path.resolve(root, name);
    if (!resolved.startsWith(`${path.resolve(root)}${path.sep}`)) {
      errors.push(`${name}: link escapes repository: ${target}`);
      continue;
    }
    if (!fs.existsSync(resolved)) {
      errors.push(`${name}: missing link target ${target}`);
      continue;
    }
    if (fragment && resolved.endsWith('.md') && !headingIds(fs.readFileSync(resolved, 'utf8')).has(fragment)) {
      errors.push(`${name}: missing anchor ${target}`);
    }
  }
  return errors;
}

// Intentionally conservative lint, not a parser, sandbox, or proof of purity.
export function checkEngineSource(name, source) {
  const errors = [];
  const reject = (message) => errors.push(`${name}: ${message}`);
  if (/\b(?:window|document|navigator|fetch|XMLHttpRequest|WebSocket|localStorage|sessionStorage|indexedDB|performance|Date|crypto|process|globalThis|setTimeout|setInterval|requestAnimationFrame|Worker|SharedArrayBuffer|Atomics)\b|Math\s*\.\s*random\b/.test(source)) {
    reject('engine contains a forbidden host API');
  }
  if (/\b(?:import\s*\(|require\s*\(|eval\s*\(|Function\s*\()/.test(source)) reject('dynamic code or imports are forbidden in engine modules');
  const imports = /\b(?:import|export)\s+(?:(?:[^;\n]*?)\s+from\s*)?["']([^"']+)["']/g;
  for (const match of source.matchAll(imports)) {
    const specifier = match[1];
    const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(name), specifier));
    if (!specifier.startsWith('.') || !resolved.startsWith('engine/')) reject(`import crosses engine boundary: ${specifier}`);
  }
  return errors;
}
