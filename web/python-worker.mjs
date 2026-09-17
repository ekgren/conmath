import { loadPyodide } from './python/pyodide.mjs';

let python;
try {
  python = await loadPyodide({ indexURL: new URL('./python/', import.meta.url).href });
  for (const name of ['successor.py', 'memory.py', 'evidence.py']) {
    const response = await fetch(new URL(`./engine/${name}`, import.meta.url));
    if (!response.ok) throw new Error(`Cannot load ${name}`);
    python.runPython(await response.text());
  }
  python.runPython('import json');
  postMessage({ type: 'ready' });
} catch (error) {
  postMessage({ type: 'error', message: String(error) });
}
self.onmessage = ({ data }) => {
  try {
    if (!python) throw new Error('Python is not ready');
    if (data.type === 'run') {
      python.globals.set('input_length', data.length);
      python.globals.set('step_limit', data.limit);
      const result = JSON.parse(python.runPython('json.dumps(run_example(input_length, step_limit))'));
      postMessage({ type: 'result', id: data.id, result });
    } else if (data.type === 'check') {
      python.globals.set('evidence_json', JSON.stringify(data.result));
      const proof = JSON.parse(python.runPython('json.dumps(check_execution(json.loads(evidence_json)))'));
      postMessage({ type: 'proof', id: data.id, proof });
    }
  } catch (error) {
    postMessage({ type: 'error', id: data.id, message: String(error) });
  }
};
