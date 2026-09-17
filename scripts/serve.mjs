import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('../dist/', import.meta.url));
const port = Number(process.env.PORT ?? 4173);
const types = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.mjs': 'text/javascript', '.json': 'application/json', '.svg': 'image/svg+xml', '.wasm': 'application/wasm', '.py': 'text/plain; charset=utf-8', '.zip': 'application/zip' };
const server = http.createServer((request, response) => {
  let relative;
  try { relative = decodeURIComponent(new URL(request.url, 'http://localhost').pathname); }
  catch { response.writeHead(400).end('Bad request'); return; }
  if (relative.endsWith('/')) relative += 'index.html';
  const filename = path.resolve(root, `.${relative}`);
  if (!filename.startsWith(root) || !fs.existsSync(filename) || !fs.statSync(filename).isFile()) {
    response.writeHead(404).end('Not found'); return;
  }
  response.writeHead(200, { 'Content-Type': types[path.extname(filename)] ?? 'application/octet-stream', 'Cache-Control': 'no-store' });
  if (request.method === 'HEAD') response.end(); else fs.createReadStream(filename).pipe(response);
});
server.listen(port, '127.0.0.1', () => console.log(`Conmath: http://127.0.0.1:${server.address().port}`));
