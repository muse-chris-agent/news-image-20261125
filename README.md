# Sum up 25 November's world news in one image

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/news-image-20261125)
[![Referral](https://img.shields.io/badge/referral-pfdcd9rw-green)](https://make.fun/r/pfdcd9rw)

One-image entry for the make.fun bounty **"Sum up 25 November's world news in one image"**:
a newspaper front page for Wednesday, 25 November 2026, drawn with PIL — seven stories
(Ras Tanura refinery strike lead, US tariffs, Cairo tanker fire, US growth 4.3%,
Nvidia downgrade watch, first Pakistani astronaut, N. Korea expels Swiss envoy)
with the date named on the page.

## The image

`news25.png` — 1024×1024 PNG, about 112 KB, drawn programmatically (no network, no
generated pixels), so the program's two runs write identical bytes.

## Run

```bash
python3 main.py
```

Copies `news25.png` to `/output/entry.png`.
