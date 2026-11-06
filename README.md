# mosaic-previews

Preview pictures for the Mosaic Salla theme's home blocks, served through jsDelivr:
`https://cdn.jsdelivr.net/gh/Sob7i/mosaic-previews@v1/<file>`

The benefits bar, products slider and products grid pictures are added after v1 and ship under `@v2` (v2 also holds every v1 file).

## Frame

- 634 x 600 px, webp quality 80, 30 KB or less each.
- Each picture is the block's own section at 1440 px wide, Arabic, light mode, captured at device scale factor 2, then scaled whole into the frame ("contain"). The letterbox colour is the page background computed on `body` at capture time (light mode, `#eeeef6`).
- Thin sections (height under a quarter of the width: ticker, newsletter, benefits bar, campaign benefits, reviews, faq and closing) are cropped to a window two thirds of the section's width, full height, centred on the section's heading text (right edge when the section has no heading), then scaled into the frame. Everything else is shown whole.
- Content is the Mosaic demo store's real products, categories and photos.
- `mosaic-promo` is the popup card, captured after its delay.

## Pictures

| Block | File | Bytes |
|---|---|---|
| home.mosaic-benefits | mosaic-benefits.webp | 3,778 |
| home.mosaic-campaign-benefits | mosaic-campaign-benefits.webp | 2,214 |
| home.mosaic-campaign-closing | mosaic-campaign-closing.webp | 5,440 |
| home.mosaic-campaign-faq | mosaic-campaign-faq.webp | 4,560 |
| home.mosaic-campaign-hero | mosaic-campaign-hero.webp | 9,966 |
| home.mosaic-campaign-reviews | mosaic-campaign-reviews.webp | 5,988 |
| home.mosaic-campaign-sets | mosaic-campaign-sets.webp | 10,966 |
| home.mosaic-campaign-steps | mosaic-campaign-steps.webp | 5,520 |
| home.mosaic-collection | mosaic-collection.webp | 11,542 |
| home.mosaic-compare | mosaic-compare.webp | 10,678 |
| home.mosaic-fan | mosaic-fan.webp | 11,658 |
| home.mosaic-faq | mosaic-faq.webp | 5,210 |
| home.mosaic-finder | mosaic-finder.webp | 7,626 |
| home.mosaic-flash-offers | mosaic-flash-offers.webp | 13,046 |
| home.mosaic-gift-set | mosaic-gift-set.webp | 11,028 |
| home.mosaic-grid | mosaic-grid.webp | 12,988 |
| home.mosaic-newsletter | mosaic-newsletter.webp | 3,964 |
| home.mosaic-notes | mosaic-notes.webp | 8,968 |
| home.mosaic-offer | mosaic-offer.webp | 7,090 |
| home.mosaic-products-grid | mosaic-products-grid.webp | 8,020 |
| home.mosaic-products-slider | mosaic-products-slider.webp | 9,682 |
| home.mosaic-promo | mosaic-promo.webp | 12,672 |
| home.mosaic-shorts | mosaic-shorts.webp | 17,584 |
| home.mosaic-slideshow | mosaic-slideshow.webp | 14,132 |
| home.mosaic-ticker | mosaic-ticker.webp | 4,222 |
| home.mosaic-video | mosaic-video.webp | 4,182 |

`home.mosaic-blog` has no picture yet: the demo store's blog is switched off, so the block renders nothing.
`home.mosaic-highlights` is not here yet.

## How they were made

`capture/` holds the scripts (set `THEME_DIR` to a Mosaic theme worktree whose `twilight.preview.json` carries demo-store content): `shoot.mjs` captures each section and encodes the webp with sharp, `shoot-promo.mjs` captures the popup card (run with only the promo block in the preview, otherwise the engine leaves it as a skeleton).
