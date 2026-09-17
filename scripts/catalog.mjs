import path from 'node:path';

// Validate editorial structure only. This does not validate mathematical claims.
export function checkCatalog(catalog, readSource) {
  const errors = [];
  const fail = (message) => errors.push(`catalog: ${message}`);
  if (!catalog || catalog.version !== 1) fail('expected version 1');
  const groups = ['parts', 'chapters', 'concepts'];
  for (const group of groups) {
    if (!Array.isArray(catalog?.[group])) fail(`${group} must be an array`);
  }
  if (errors.length) return errors;
  const records = new Map();
  for (const group of groups) {
    for (const entry of catalog[group]) {
      if (!entry || !/^[a-z][a-z0-9-]*$/.test(entry.id ?? '')) {
        fail(`${group} contains an invalid ID`);
        continue;
      }
      if (records.has(entry.id)) fail(`duplicate ID ${entry.id}`);
      if (typeof entry.title !== 'string' || !entry.title.trim()) fail(`${entry.id}: missing title`);
      records.set(entry.id, { ...entry, group });
    }
  }
  if (errors.length) return errors;
  const order = [];
  const owners = new Map();
  for (const part of catalog.parts) {
    if (!Array.isArray(part.chapters)) {
      fail(`${part.id}: chapters must be an array`);
      continue;
    }
    for (const id of part.chapters) {
      if (records.get(id)?.group !== 'chapters') fail(`${part.id}: unknown chapter ${id}`);
      if (owners.has(id)) fail(`${id}: chapter belongs to multiple positions or parts`);
      owners.set(id, part.id);
      order.push(id);
    }
  }
  const sources = new Set();
  for (const entry of records.values()) {
    if (entry.group === 'parts') continue;
    if (entry.group === 'chapters' && !owners.has(entry.id)) fail(`${entry.id}: no owning part`);
    if (!['planned', 'draft', 'ready'].includes(entry.status)) fail(`${entry.id}: invalid status`);
    if (!Array.isArray(entry.requires)) {
      fail(`${entry.id}: requires must be an array`);
      continue;
    }
    if (new Set(entry.requires).size !== entry.requires.length) fail(`${entry.id}: duplicate prerequisite`);
    const links = [...entry.requires];
    if (entry.group === 'chapters') {
      if (!Array.isArray(entry.concepts)) fail(`${entry.id}: concepts must be an array`);
      else {
        for (const id of entry.concepts) {
          if (records.get(id)?.group !== 'concepts') fail(`${entry.id}: unknown concept ${id}`);
        }
        links.push(...entry.concepts);
      }
    }
    for (const id of links) {
      const target = records.get(id);
      if (!target || target.group === 'parts') fail(`${entry.id}: unknown prerequisite/reference ${id}`);
      if (entry.status === 'ready' && target?.status !== 'ready') fail(`${entry.id}: ready content depends on unfinished ${id}`);
    }
    for (const id of entry.requires) {
      if (entry.group === 'chapters' && records.get(id)?.group === 'chapters' && order.indexOf(id) >= order.indexOf(entry.id)) {
        fail(`${entry.id}: prerequisite ${id} must appear earlier in reading order`);
      }
    }
    if (entry.status === 'planned') {
      if (entry.source !== null) fail(`${entry.id}: planned source must be null`);
      continue;
    }
    const expected = entry.group === 'chapters'
      ? `book/parts/${owners.get(entry.id)}/${entry.id}.md`
      : `concepts/${entry.id}.md`;
    if (entry.source !== expected || path.posix.normalize(entry.source ?? '') !== entry.source) {
      fail(`${entry.id}: source must be ${expected}`);
      continue;
    }
    if (sources.has(entry.source)) fail(`${entry.id}: duplicate source`);
    sources.add(entry.source);
    const source = readSource(entry.source);
    if (typeof source !== 'string' || !source.trim()) fail(`${entry.id}: source missing or empty`);
  }
  const active = new Set();
  const visited = new Set();
  function visit(id) {
    if (active.has(id)) { fail(`prerequisite cycle at ${id}`); return; }
    if (visited.has(id)) return;
    const entry = records.get(id);
    if (!entry || entry.group === 'parts') return;
    active.add(id);
    for (const dependency of Array.isArray(entry.requires) ? entry.requires : []) visit(dependency);
    active.delete(id);
    visited.add(id);
  }
  for (const id of records.keys()) visit(id);
  return errors;
}
