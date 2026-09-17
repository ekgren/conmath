import { createReadStream, statSync, watch } from "node:fs";
import { buildBook } from './build-book.mjs';
import { createServer } from "node:http";
import { extname, join, normalize } from "node:path";

const root = join(process.cwd(), "site");
const host = "127.0.0.1";
const port = Number(process.env.CONMATH_PORT ?? 4173);

await buildBook();
let rebuildTimer;
watch(new URL('../book/parts/', import.meta.url), () => {
  clearTimeout(rebuildTimer);
  rebuildTimer = setTimeout(() => buildBook().catch(error => console.error(error)), 80);
});

const types = {
  ".css": "text/css; charset=utf-8",
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml"
};

createServer((request, response) => {
  const urlPath = decodeURIComponent(new URL(request.url, `http://${host}`).pathname);
  const safePath = normalize(urlPath).replace(/^(\.\.[/\\])+/, "");
  let filePath = join(root, safePath);

  try {
    if (statSync(filePath).isDirectory()) filePath = join(filePath, "index.html");
    if (!filePath.startsWith(root) || !statSync(filePath).isFile()) throw new Error("not found");
    response.writeHead(200, {
      "Content-Type": types[extname(filePath)] ?? "application/octet-stream",
      "Cache-Control": "no-store"
    });
    createReadStream(filePath).pipe(response);
  } catch {
    response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
    response.end("Not found");
  }
}).listen(port, host, () => {
  console.log(`Conmath available at http://${host}:${port}`);
});
