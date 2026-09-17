import { defineConfig } from '@playwright/test';
const port = Number(process.env.TEST_PORT ?? 4174);
export default defineConfig({
  testDir: './tests/browser',
  outputDir: 'artifacts/browser-results',
  reporter: [['list'], ['json', { outputFile: 'artifacts/browser-report.json' }]],
  use: { baseURL: `http://127.0.0.1:${port}`, trace: 'retain-on-failure', screenshot: 'only-on-failure' },
  webServer: { command: 'node scripts/serve.mjs', env: { PORT: String(port) }, url: `http://127.0.0.1:${port}`, reuseExistingServer: false },
});
