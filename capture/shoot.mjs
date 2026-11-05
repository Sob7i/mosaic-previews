import { createRequire } from 'node:module';
import { readdirSync, writeFileSync, mkdirSync, statSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';
const repo = '/Users/sobhialkhuder/Documents/sl/mosaic-pictures';
const out = process.env.OUT;
const FRAME = { w: 634, h: 600 };
const QUALITY = Number(process.env.Q ?? 80);
const require = createRequire(join(repo, '.tools', 'package.json'));
const { chromium } = require('playwright-core');
const sharp = createRequire(join(repo, 'node_modules/.pnpm/sharp@0.35.5_@types+node@26.6.5/node_modules/sharp/'))('sharp');
const cache = join(homedir(), 'Library/Caches/ms-playwright');
const build = readdirSync(cache).filter((d) => /^chromium-\d+$/.test(d)).sort().pop();
const executablePath = join(cache, build, 'chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');
const blocks = process.argv.slice(2);
mkdirSync(out, { recursive: true });
const b = await chromium.launch({ executablePath });
const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, colorScheme: 'light', deviceScaleFactor: 2 });
const p = await ctx.newPage();
await p.goto('http://localhost:5353/ar', { waitUntil: 'load', timeout: 60000 });
await p.waitForTimeout(3000);
await p.addStyleTag({ content: '*{animation-play-state:paused!important}' });
const ALIAS = { 'mosaic-flash-offers': 'flash' };
const selFor = (n) => `.s-block--${n}, .m-home-block--${ALIAS[n] ?? n.replace('mosaic-', '')}`;
for (const name of blocks) {
  const sel = selFor(name);
  const el = p.locator(sel).first();
  try { await el.waitFor({ timeout: 8000 }); } catch { console.log(name, 'NOT RENDERED'); continue; }
  await el.scrollIntoViewIfNeeded();
  await p.waitForTimeout(800);
  await p.evaluate((n) => {
    const section = document.querySelector(n);
    for (const e of document.body.querySelectorAll('*')) {
      if (section.contains(e) || e.contains(section)) continue;
      const pos = getComputedStyle(e).position;
      if (pos === 'fixed' || pos === 'sticky') e.style.visibility = 'hidden';
    }
  }, sel);
  const box = await p.evaluate((n) => { const r = document.querySelector(n).getBoundingClientRect(); return { x: Math.ceil(r.left), y: r.top + scrollY, width: Math.floor(r.width), height: Math.floor(r.height) }; }, sel);
  const png = await p.screenshot({ fullPage: true, clip: box, animations: 'disabled' });
  const corner = await sharp(png).extract({ left: 2, top: 2, width: 1, height: 1 }).raw().toBuffer();
  const BACKDROP = { r: corner[0], g: corner[1], b: corner[2] };
  const file = join(out, `${name}.webp`);
  const fitted = await sharp(png).resize(FRAME.w, FRAME.h, { fit: 'contain', background: BACKDROP, kernel: 'lanczos3' }).webp({ quality: QUALITY, effort: 6 }).toBuffer();
  writeFileSync(file, fitted);
  writeFileSync(join('/private/tmp/claude-502/-Users-sobhialkhuder-Documents-sl-mosaic/8c30d7b0-69ae-4fdb-a690-dbcd7ea10d98/scratchpad/full', `${name}.png`), png);
  console.log(name, statSync(file).size, 'bytes');
}
await b.close();
