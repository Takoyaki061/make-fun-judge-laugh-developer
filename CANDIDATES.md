# Candidates — Make the AI Judge Laugh: Developer Excuses

Bounty: `u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`
Gate: one line, 1–200 characters, written to `/output/entry.txt`.

DeepSeek (via 100milionseek) was down for the whole build window — HTTP 503
on 7 attempts across 3 calls (2 candidate-generation calls, 1 critique call),
so the candidates below were brainstormed and critique-picked by the builder
instead. Never let a dead provider block the build.

## Candidates (all under 200 chars)

1. It worked on my machine, so we promoted my machine to production. (65)
2. The rollback worked — it rolled us back to the bug we fixed last Tuesday. (73)
3. The outage was caused by one missing character; I've since apologised to the semicolon personally. (106)
4. All the tests passed, which is how I know they were testing nothing. (69)
5. It worked in staging — staging has never met a real user. (58)
6. Someone deployed on a Friday. That someone was me. I have no further comment. (79)
7. The hotfix fixed the bug and introduced three new ones, so technically we're ahead on features. (101)
8. The logs said everything was fine, which is exactly what they said right before everything broke. (103)
9. I wrote that code at 3am, and 3am me is not someone I trust with production. (80)
10. We didn't lose the data, we just relocated it to a table nobody can find. (75)

## Critique against the judge criteria

Judge criteria, most important first: (1) funny single-line excuse a dev
gives when code breaks in production; (2) twist a developer recognises,
revealing what really happened; (3) sounds like something a dev would
actually say, jargon right; (4) lands fast, every word earns its place;
(5) fresh — avoids worn excuses or turns one in a way nobody has before.

- #1 — Best on (5): it takes the single most worn excuse in the field
  ("works on my machine") and turns it into the punchline instead of
  repeating it — exactly what criterion 5 rewards. Twist on (2): the cliché
  excuse becomes the "fix", revealing the real story (dev env ≠ prod).
  Clean jargon on (3) ("promoted ... to production"), nothing to trim on
  (4), unmistakably an excuse on (1).
- #2 — Good twist (rollback resurrecting an old bug) and recognisable, but
  the shape is a known joke and it reads more like an observation than an
  excuse the dev gives.
- #3 — Specific and funny, but "one missing character / semicolon" is a
  known trope; the twist states the cause plainly rather than revealing
  something hidden.
- #4 — Strong twist, very recognisable, fast — but "tests passed yet tested
  nothing" is a fairly common dev joke; less fresh than #1.
- #5 — Fast and true, but a close cousin of "works on my machine"; less
  fresh than #1.
- #6 — The confessional "no further comment" button is fun, but the Friday
  deploy is a well-worn trope and the line leans on delivery over twist.
- #7 — "Fixed one bug, introduced three" is a known shape; decent but not
  the freshest.
- #8 — Good turn on logs that lie; fresh-ish, but the setup takes a beat
  longer to land than #1.
- #9 — Relatable self-deprecation, but more confession than excuse and the
  twist is thin.
- #10 — Cute euphemism ("relocated"), but "we didn't lose the data" is a
  known shape.

## Pick

**#1: "It worked on my machine, so we promoted my machine to production."**

Highest on freshness (the explicit tiebreaker direction in criterion 5),
clearest twist, fastest landing, correct jargon throughout. 65 characters.
