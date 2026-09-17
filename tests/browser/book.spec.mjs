import { test, expect } from '@playwright/test';
const chapter = '/book/objects-and-constructions.html';
test.setTimeout(60000);
const run = page => page.getByRole('button', { name: 'Run program', exact: true });
async function execute(page) {
  await expect(run(page)).toBeEnabled({ timeout: 30000 });
  await run(page).click();
  await expect(page.locator('#run-status')).not.toHaveText('Running…');
}

test('runs displayed Python, checks and exports evidence without external requests', async ({ page, context }, testInfo) => {
  const faults = [], external = [];
  page.on('pageerror', error => faults.push(error.message));
  context.on('request', request => { if (!request.url().startsWith('http://127.0.0.1:')) external.push(request.url()); });
  await page.goto('/');
  await page.getByRole('link', { name: 'Begin with objects and constructions' }).click();
  await expect(page.locator('code[data-source="engine/successor.py"]')).toContainText('mark = memory.read(source + i)');
  await execute(page);
  await expect(page.locator('#run-status')).toContainText('Copied 3 marks and added one in 4 steps');
  await expect(page.locator('#source-cells .marked')).toHaveCount(3);
  await expect(page.locator('#cells .marked')).toHaveCount(4);
  await page.getByText('Inspect reads, writes, and evidence', { exact: true }).click();
  await expect(page.locator('#trace li')).toHaveCount(11);
  await page.getByRole('button', { name: 'Check this execution' }).click();
  await expect(page.locator('#proof-status')).toContainText('13 checks');
  const downloadEvent = page.waitForEvent('download');
  await page.getByRole('button', { name: 'Download evidence' }).click();
  await (await downloadEvent).saveAs(testInfo.outputPath('evidence.json'));
  await page.getByRole('button', { name: 'Reset', exact: true }).click();
  await expect(page.locator('#cells .marked')).toHaveCount(0);
  await expect(page.locator('#proof-status')).not.toContainText('Checked:');
  expect(faults).toEqual([]); expect(external).toEqual([]);
});

test('finite step and memory failures, empty input, invalid budget and recovery', async ({ page }) => {
  await page.goto(chapter);
  await page.getByLabel('Step budget').fill('3');
  await execute(page);
  await expect(page.locator('#run-status')).toContainText('Failure: step budget exhausted');
  await expect(page.locator('#cells .marked')).toHaveCount(3);
  await page.getByLabel('Input length').selectOption('8');
  await page.getByLabel('Step budget').fill('9');
  await execute(page);
  await expect(page.locator('#run-status')).toContainText('target has no room');
  await page.getByLabel('Input length').selectOption('0');
  await page.getByLabel('Step budget').fill('1');
  await execute(page);
  await expect(page.locator('#cells .marked')).toHaveCount(1);
  await page.getByLabel('Step budget').fill('10');
  await expect(run(page)).toBeDisabled();
  await page.getByLabel('Step budget').fill('4');
  await expect(run(page)).toBeEnabled();
});

for (const width of [390, 1280]) test(`reading and interactions fit ${width}px`, async ({ page }, testInfo) => {
  await page.setViewportSize({ width, height: 900 });
  await page.goto(chapter);
  await page.screenshot({ path: testInfo.outputPath('opening.png') });
  await page.locator('code[data-source="engine/successor.py"]').scrollIntoViewIfNeeded();
  await page.screenshot({ path: testInfo.outputPath('program.png') });
  await execute(page);
  await page.getByText('Inspect reads, writes, and evidence', { exact: true }).click();
  await page.getByRole('button', { name: 'Check this execution' }).click();
  await expect(page.locator('#proof-status')).toContainText('Checked:');
  await page.locator('#row-experiment').scrollIntoViewIfNeeded();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  await page.screenshot({ path: testInfo.outputPath('checked.png') });
  await page.getByRole('link', { name: 'resource bounds', exact: true }).click();
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Resource bounds');
});

test('static prose and source remain readable without JavaScript', async ({ browser }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  await page.goto(`http://127.0.0.1:${process.env.TEST_PORT ?? 4174}${chapter}`);
  await expect(page.getByRole('heading', { name: 'A row and its successor' })).toBeVisible();
  await expect(page.locator('math')).toBeVisible();
  await expect(page.locator('code[data-source="engine/successor.py"]')).toContainText('def successor');
  await page.getByRole('link', { name: 'proof and evidence', exact: true }).click();
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Proof and evidence');
  await context.close();
});

test('runtime loading failure is visible and leaves prose readable', async ({ page, context }) => {
  await context.route('**/assets/python-worker.mjs', route => route.abort());
  await page.goto(chapter);
  await expect(page.locator('#run-status')).toContainText('Python could not run', { timeout: 30000 });
  await expect(run(page)).toBeDisabled();
  await expect(page.locator('code[data-source="engine/successor.py"]')).toContainText('def successor');
});

test('keyboard access reaches the book and runs the program', async ({ page }) => {
  await page.goto(chapter);
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link', { name: 'Skip to content' })).toBeFocused();
  await page.keyboard.press('Enter');
  await expect(page.locator('main')).toBeFocused();
  await expect(run(page)).toBeEnabled({ timeout: 30000 });
  await run(page).focus();
  await page.keyboard.press('Enter');
  await expect(page.locator('#run-status')).toContainText('Success.');
});
