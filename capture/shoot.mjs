import { createRequire } from 'node:module';
import { readdirSync, writeFileSync, mkdirSync, statSync } from 'node:fs';
import { homedir } from 'node:os';
import { join } from 'node:path';
const repo = process.env.THEME_DIR;
if (!repo) throw new Error('set THEME_DIR to a Mosaic theme worktree');
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
  await p.evaluate((n) => { const r = document.querySelector(n).getBoundingClientRect(); window.scrollTo(0, Math.max(0, r.top + scrollY - 300)); }, sel);
  await p.waitForTimeout(500);
  const box = await p.evaluate((n) => { const r = document.querySelector(n).getBoundingClientRect(); return { x: Math.ceil(r.left), y: r.top + scrollY, width: Math.floor(r.width), height: Math.floor(r.height) }; }, sel);
  const png = await p.screenshot({ fullPage: true, clip: box, animations: 'disabled' });
  const pageBackground = await p.evaluate(() => {
    for (const e of [document.body, document.documentElement]) {
      const m = getComputedStyle(e).backgroundColor.match(/[\d.]+/g).map(Number);
      if (m.length < 4 || m[3] > 0) return { r: m[0], g: m[1], b: m[2] };
    }
    return { r: 255, g: 255, b: 255 };
  });
  const meta = await sharp(png).metadata();
  const thin = box.height * Number(process.env.THIN_DEN ?? 4) < box.width;
  const cropWidth = Math.round((meta.width * 2) / 3);
  const headingCentre = await p.evaluate(({ n, left }) => {
    const heading = document.querySelector(n).querySelector('h1, h2, h3');
    if (!heading) return null;
    const range = document.createRange();
    range.selectNodeContents(heading);
    const r = range.getBoundingClientRect();
    return r.left + r.width / 2 - left;
  }, { n: sel, left: box.x });
  const wanted = headingCentre === null ? meta.width : Math.round(headingCentre * 2) + cropWidth / 2;
  const cropLeft = Math.round(Math.min(meta.width - cropWidth, Math.max(0, wanted - cropWidth)));
  const source = thin ? await sharp(png).extract({ left: cropLeft, top: 0, width: cropWidth, height: meta.height }).png().toBuffer() : png;
  console.log(name, thin ? 'thin: half, left ' + cropLeft : 'whole', box.width + 'x' + box.height, JSON.stringify(pageBackground));
  const file = join(out, `${name}.webp`);
  const fitted = await sharp(source).resize(FRAME.w, FRAME.h, { fit: 'contain', background: pageBackground, kernel: 'lanczos3' }).webp({ quality: QUALITY, effort: 6 }).toBuffer();
  writeFileSync(file, fitted);
  console.log(name, statSync(file).size, 'bytes');
}
await b.close();
