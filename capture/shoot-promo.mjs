import { createRequire } from 'node:module';
import { readdirSync, writeFileSync, statSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';
const repo = process.env.THEME_DIR;
if (!repo) throw new Error('set THEME_DIR to a Mosaic theme worktree');
const out = process.env.OUT;
const require = createRequire(join(repo, '.tools', 'package.json'));
const { chromium } = require('playwright-core');
const sharp = createRequire(join(repo, 'node_modules/.pnpm/sharp@0.35.5_@types+node@26.6.5/node_modules/sharp/'))('sharp');
const cache = join(homedir(), 'Library/Caches/ms-playwright');
const build = readdirSync(cache).filter((d) => /^chromium-\d+$/.test(d)).sort().pop();
const executablePath = join(cache, build, 'chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');
const b = await chromium.launch({ executablePath });
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, colorScheme: 'light', deviceScaleFactor: 2 });
const p = await ctx.newPage();
await p.goto('http://localhost:5353/ar', { waitUntil: 'load', timeout: 60000 });
await p.evaluate(() => document.querySelector('.m-home-block--promo').scrollIntoView());
await p.waitForTimeout(1500);
const card = p.locator('.m-modal__card').first();
await card.waitFor({ timeout: 20000 });
await p.waitForTimeout(2500);
const bg = await p.evaluate(() => getComputedStyle(document.body).backgroundColor);
await p.evaluate(() => {
  const root = document.querySelector('.m-modal');
  for (const e of document.body.children) if (!e.contains(root) && e !== root) e.style.visibility = 'hidden';
  document.querySelector('.m-modal__scrim').style.display = 'none';
  document.body.style.background = getComputedStyle(document.body).backgroundColor;
  
  for (const e of document.body.querySelectorAll('*')) {
    if (root.contains(e) || e.contains(root)) continue;
    const pos = getComputedStyle(e).position;
    if (pos === 'fixed' || pos === 'sticky') e.style.visibility = 'hidden';
  }
});
await p.evaluate(() => document.activeElement && document.activeElement.blur());
const r = await card.boundingBox();
const pad = 16;
const png = await p.screenshot({ clip: { x: Math.max(0, r.x - pad), y: Math.max(0, r.y - pad), width: r.width + 2 * pad, height: r.height + 2 * pad }, animations: 'disabled' });
const m = (await (async () => bg)()).match(/[\d.]+/g).map(Number);
const fitted = await sharp(png).resize(634, 600, { fit: 'contain', background: { r: m[0], g: m[1], b: m[2] }, kernel: 'lanczos3' }).webp({ quality: 80, effort: 6 }).toBuffer();
writeFileSync(join(out, 'mosaic-promo.webp'), fitted);
console.log('mosaic-promo', statSync(join(out, 'mosaic-promo.webp')).size, 'bytes', r.width, r.height);
await b.close();
