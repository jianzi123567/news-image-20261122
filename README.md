# World News — 22 November 2026 (news-image-20261122)

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/jianzi123567/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/jianzi123567/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for the make.fun bounty **news-image-20261122**: one picture that
sums up the world news of Sunday 22 November 2026. $100 is split among
the 50 best entries.

## What's in the picture

A newspaper-style infographic (1024×1024), headlined "WORLD NEWS —
22 NOVEMBER 2026", with five stories:

| Panel | Story |
| --- | --- |
| Mexico | Troops capture the FBI most-wanted cartel boss "Chapo Isidro" in Sinaloa; eleven die in the raid, four of them soldiers. (BBC / NY Post) |
| Climate | COP31 in Antalya, Turkey, goes into overtime as nearly 200 nations split over fossil fuels. (Reuters / AP) |
| Markets | Bitcoin drops to about $55,000, a two-year low, then climbs back above $60,000 within hours. (Finnhub) |
| US–China | Beijing firmly opposes a US FCC vote to bar Chinese telecom firms from direct access to US phone numbers. (Reuters) |
| Israel | Gadi Eisenkot invites Netanyahu's Likud party to marathon coalition talks while trying to form a government. (Times of Israel) |

## Running it

`main.py` needs Python 3 and nothing else. It reads `entry.png` from
the repository root, checks the file is a JPEG or PNG under 1 MiB, and
copies those exact bytes to `/output/entry.png`, then reads the copy
back to confirm it matches. No network, no clock, no randomness: every
run writes the same bytes.

## Files

- `entry.png` — the infographic (1024×1024 JPEG, under 1 MiB)
- `main.py` — the program that writes `/output/entry.png`
