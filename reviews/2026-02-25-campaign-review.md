# CURA Campaign Review — 2026-02-25

**Customer ID:** 4611756192
**Reviewer:** Claude (automated via MCP)
**Review context:** Post-optimization check, 1 day after major changes made on 2026-02-24

---

## Summary

This review assessed the health of all CURA campaigns following the optimization pass on 2026-02-24. Both 7-day and 30-day windows were examined — the 7-day window still includes pre-optimization spend. Three small changes were made during this review. The account's two established campaigns (Appointment Bookings, NCS) are performing well. The four new headache campaigns are in learning phase with insufficient data for decisions.

**30-day totals (all campaigns):** $1,259.45 spent, 112 conversions
**30-day totals (enabled only):** $558.32 spent, 109 conversions, $5.12 avg CPA
**Active daily budget:** $75/day (6 enabled campaigns)

---

## 1. Full Campaign Performance

### 30-Day Performance (primary reference)

| Campaign | ID | Status | Budget | Clicks | Cost | Conv | CPA | CTR | Conv Rate |
|---|---|---|---|---|---|---|---|---|---|
| Appointment Bookings | 22432832085 | ENABLED | $25/day | 225 | $302.09 | 86.08 | $3.51 | 4.99% | 38.26% |
| NCS Sydney | 23016371425 | ENABLED | $15/day | 161 | $121.99 | 23.0 | $5.30 | 1.93% | 14.29% |
| Near Me | 23578008459 | ENABLED | $5/day | 5 | $58.59 | 0 | — | 6.58% | 0% |
| Migraine | 23578226562 | ENABLED | $15/day | 9 | $39.89 | 0 | — | 5.29% | 0% |
| Tension Cluster | 23583571415 | ENABLED | $10/day | 6 | $24.80 | 0 | — | 3.51% | 0% |
| Cervicogenic | 23588213188 | ENABLED | $5/day | 2 | $10.97 | 0 | — | 4.76% | 0% |
| **Enabled total** | | | **$75/day** | **408** | **$558.33** | **109.08** | **$5.12** | | |
| Emma Harrison | 22644007845 | PAUSED | $3/day | 133 | $301.98 | 2.0 | $151.00 | 6.65% | 1.50% |
| Migraine Ads | 23081715570 | PAUSED | $3/day | 116 | $399.15 | 1.0 | $399.15 | 1.73% | 0.86% |
| Local Near Me | 23588589252 | PAUSED | $10/day | 0 | $0 | 0 | — | 0% | 0% |

> Note: Appointment Bookings shows 86.08 conversions with fractional counts — this indicates Google's data-driven attribution model splitting credit across touchpoints. The conversion rate of 38.26% includes view-through and cross-device conversions.

### 7-Day Performance (post-optimization snapshot)

> The 7-day window (approx Feb 18–25) includes ~5 days of pre-optimization data. It will not reflect the true post-change baseline until ~March 1.

| Campaign | Clicks | Cost | Conv | CPA | Notes |
|---|---|---|---|---|---|
| Appointment Bookings | 52 | $59.24 | 2 | $29.62 | Only converter in 7d window |
| NCS Sydney | 87 | $59.05 | 0 | — | 0 conv in 7d but 23 in 30d |
| Near Me | 5 | $58.59 | 0 | — | Inflated by pre-change spend |
| Migraine | 9 | $39.89 | 0 | — | Learning phase |
| Tension Cluster | 6 | $24.80 | 0 | — | Learning phase |
| Cervicogenic | 2 | $10.97 | 0 | — | Learning phase |
| Migraine Ads (paused) | 43 | $204.57 | 0 | — | Pre-pause residual |
| Emma Harrison (paused) | 25 | $50.94 | 0 | — | Pre-pause residual |

---

## 2. Appointment Bookings Deep Dive

**Campaign ID:** 22432832085 | **Budget:** $25/day | **Bidding:** TARGET_CPA $5 | **Negatives:** 78

### Assessment: Strong performer, some Quality Score concerns

The account's best campaign by volume: 86 conversions at $3.51 CPA over 30 days. The TARGET_CPA $5 bid is working — the algorithm is delivering well below target.

### Keyword Performance (30 days)

| Keyword | Match | Clicks | Cost | Conv | CPA | QS |
|---|---|---|---|---|---|---|
| neurologist Sydney | BROAD | 164 | $241.67 | 63.08 | $3.83 | 5 |
| cura drummoyne | PHRASE | 15 | $19.36 | 10.0 | $1.94 | 6 |
| best neurologist sydney | EXACT | 8 | $11.56 | 2.5 | $4.62 | **1** |
| neurologist drummoyne | PHRASE | 7 | $7.64 | 1.5 | $5.10 | 7 |
| top neurologist in sydney | PHRASE | 2 | $3.27 | 0 | — | **1** |
| neurologist Sydney | PHRASE | 1 | $2.10 | 0 | — | 5 |
| neurologists in sydney | PHRASE | 0 | $0 | 0 | — | 4 |
| best neurologist Sydney | PHRASE | 0 | $0 | 0 | — | **1** |
| neurologist inner west sydney | PHRASE | 0 | $0 | 0 | — | **1** |

**Quality Score flags:**
- 4 keywords with QS:1 — "best neurologist sydney" (EXACT & PHRASE), "top neurologist in sydney", "neurologist inner west sydney"
- The BROAD "neurologist Sydney" (QS:5) carries 80% of the campaign's spend and 73% of conversions
- "cura drummoyne" (QS:6) is the best brand keyword: 10 conversions at $1.94 CPA
- QS:1 keywords are not spending heavily (Google suppresses them) but they drag down ad group quality signals

**Interpretation:** The campaign is heavily reliant on a single BROAD keyword. This is working well under MAXIMIZE_CONVERSIONS / TARGET_CPA $5 (Google's Smart Bidding manages the broad matching), but if that keyword's performance degrades the whole campaign suffers. The QS:1 keywords aren't costing money but indicate ad relevance issues for "best" and "top" queries — likely the ad copy doesn't match the "best/top" framing.

### Top Search Terms (30 days)

| Search Term | Clicks | Cost | Conv | CPA |
|---|---|---|---|---|
| neurologist near me | 20 | $23.52 | 6.08 | $3.87 |
| neurologist sydney | 7 | $14.07 | 2.0 | $7.04 |
| neurologist | 10 | $10.94 | 3.0 | $3.65 |
| best neurologist in sydney | 7 | $9.74 | 0.5 | $19.48 |
| neurologist drummoyne | 8 | $9.17 | 2.0 | $4.59 |
| cura drummoyne | 7 | $7.69 | 5.0 | $1.54 |
| neurology near me | 6 | $6.59 | 3.0 | $2.20 |
| neurologist rouse hill | 4 | $6.38 | 0 | — |

**Star performers:** "cura drummoyne" ($1.54 CPA), "neurology near me" ($2.20 CPA), "neurologist" ($3.65 CPA)
**Watch:** "best neurologist in sydney" (7 clicks, $9.74, only 0.5 conv — $19.48 CPA)

---

## 3. NCS Sydney Deep Dive

**Campaign ID:** 23016371425 | **Budget:** $15/day | **Bidding:** MAX_CONV | **Negatives:** 53 (post-review)

### Assessment: Account's strongest campaign by CPA

23 conversions at $5.30 CPA over 30 days — excellent for a medical specialist. The campaign targets a specific diagnostic procedure (nerve conduction studies) with clear booking intent.

### Critical Audit Correction

Initially, the 7-day data suggested "nerve specialist sydney" should be paused (16 clicks, $14.49, 0 conversions in 7d). The 30-day data revealed it has **8 conversions at $4.25 CPA** — responsible for ~35% of the campaign's total conversions. The 7-day window caught a conversion dry spell. **Pausing it would have been a significant mistake.**

### Keyword Performance by Ad Group (30 days)

**Ad Group 1 (Core NCS)** — $50.21 cost, 56 clicks

| Keyword | Match | Clicks | Cost | Conv | CPA | QS |
|---|---|---|---|---|---|---|
| nerve study | PHRASE | 11 | $16.82 | 4 | $4.20 | 7 |
| nerve conduction study near me | PHRASE | 5 | $8.51 | 4 | $2.13 | 6 |
| nerve conduction studies sydney | EXACT | 3 | $6.49 | 0 | — | 7 |
| neurophysiology sydney | PHRASE/EXACT | 0 | $0 | 0 | — | **3** |

**Specialist Names & Local** — $41.41 cost, 40 clicks

| Keyword | Match | Clicks | Cost | Conv | CPA | Status |
|---|---|---|---|---|---|---|
| nerve specialist sydney | PHRASE | 29 | $34.00 | 8 | $4.25 | ENABLED |
| cura medical specialists | PHRASE | 6 | $5.71 | 0 | — | **PAUSED today** |

**EMG Testing** — $3.21 cost, 4 clicks, 0 conversions (low volume, terms relevant)

**Condition-Specific NCS** — $27.16 cost, 61 clicks (search terms mostly below reporting threshold)

### Top Search Terms (30 days)

| Search Term | Ad Group | Clicks | Cost | Conv | CPA |
|---|---|---|---|---|---|
| nerve conduction study near me | Ad group 1 | 4 | $7.52 | 4 | $1.88 |
| cura drummoyne | Specialist Names | 5 | $5.32 | 0 | — |
| nerve conduction study | Ad group 1 | 2 | $2.16 | 1 | $2.16 |
| neurologists sydney | Specialist Names | 2 | $2.13 | 0 | — |
| neurologist gregory hills | Specialist Names | 1 | $1.80 | 1 | $1.80 |
| nerve conduction study sydney | Ad group 1 | 1 | $1.71 | 0 | — |
| diagnosis of peripheral neuropathy | Ad group 1 | 1 | $1.22 | 1 | $1.22 |

**Irrelevant matches blocked today:** cranial nerve exam, biopsy, brain surgeon, facial nerve (all added as campaign negatives, see Changes section)

---

## 4. Near Me Campaign Deep Dive

**Campaign ID:** 23578008459 | **Budget:** $5/day (reduced from $20 on Feb 24) | **Bidding:** MAX_CONV | **Negatives:** 64

### Assessment: On watch — excessive CPC, 0 conversions

$58.59 total spend over 30 days, 0 conversions. The 30-day data equals the 7-day data because this campaign only launched ~7 days ago. Average CPC is $11.72 — extremely high.

### Key issues:
1. **Budget was $20/day** until reduced to $5/day on Feb 24
2. **"neurologist headache near me" (BROAD)** was paused Feb 24 — consumed $39.95+ before pause
3. **"mri scan"** appeared as search term ($15.80) — now EXCLUDED via negative keyword
4. **"cervicogenic headaches"** matched for $24.15 — should be handled by Cervicogenic campaign. "cervicogenic" is already a campaign-level negative, but this was a pre-negative match

### Top Search Terms (30 days)

| Search Term | Clicks | Cost | Status |
|---|---|---|---|
| cervicogenic headaches | 1 | $24.15 | Pre-negative match |
| mri scan | 1 | $15.80 | EXCLUDED |
| ron granot | 1 | $8.30 | Competitor neurologist |
| neurologist liverpool nsw | 1 | $1.74 | Not CURA's area |

**Decision at 14-day mark (March 8):** If still 0 conversions at $5/day, recommend pausing.

---

## 5. Migraine Campaign Deep Dive

**Campaign ID:** 23578226562 | **Budget:** $15/day | **Bidding:** MAX_CONV | **Negatives:** 67 (post-review)

### Assessment: Learning phase, heavily informational search terms

9 clicks, $39.89, 0 conversions. Average CPC of $4.43 is high. Only 170 impressions suggests low volume for these keywords in Sydney.

### Search Terms (30 days — all data since launch)

| Search Term | Clicks | Cost | Conv | Intent |
|---|---|---|---|---|
| migraine australia | 2 | $8.19 | 0 | Informational — **"australia" negative added today** |
| chronic migraine treatments | 1 | $2.38 | 0 | Mixed — treatment-seeking |
| abdominal migraine treatment | 1 | $2.21 | 0 | Irrelevant condition subtype |
| migraine | 0 | $0 | 0 | Too broad (5 imp) |
| migraine symptoms | 0 | $0 | 0 | Informational (5 imp) |
| vestibular migraine | 0 | $0 | 0 | Condition subtype (3 imp) |

**Concern:** The search terms are heavily informational (symptoms, medication names, "what to do") rather than booking-intent. This is a structural challenge with headache/migraine keywords — the search volume is dominated by people seeking information, not appointments. Conversion potential may be inherently limited.

**Notable competitor/doctor name impressions:** "bronwyn jenkins" (1 imp), "prof nimeshan geevasinga" (2 imp), "angelo jayamanne" (1 imp), "ashraf dower" (1 imp) — suggests Google is showing the ad for neurologist-related queries in the migraine space.

**Decision at 14-day mark:** If 0 conversions, reduce budget from $15 to $7.50/day.

---

## 6. Tension Cluster Campaign Deep Dive

**Campaign ID:** 23583571415 | **Budget:** $10/day | **Bidding:** MAX_CONV | **Negatives:** 62

### Assessment: Learning phase, informational queries, pre-negative spend leaking through

6 clicks, $24.80, 0 conversions. Average CPC of $4.13.

### Search Terms (30 days)

| Search Term | Clicks | Cost | Conv | Notes |
|---|---|---|---|---|
| what causes headaches everyday in females | 1 | $7.23 | 0 | Informational |
| headaches | 1 | $5.16 | 0 | EXCLUDED — pre-negative match |
| what does a neurologist treat | 1 | $3.67 | 0 | Informational |
| tension headache symptoms and causes | 1 | $0.70 | 0 | Informational |
| cluster headaches | 0 | $0 | 0 | Relevant (4 imp) |
| tension headache | 0 | $0 | 0 | Relevant (3 imp) |

**Observation:** The "headaches" search term ($5.16) was already EXCLUDED — this is pre-negative spend. "bronwyn jenkins neurologist" also appears (EXCLUDED, 0 cost). The negatives are working.

Same structural concern as Migraine: search volume dominated by informational intent rather than booking intent.

**Decision at 14-day mark:** If 0 conversions, reduce budget from $10 to $5/day.

---

## 7. Cervicogenic Campaign Deep Dive

**Campaign ID:** 23588213188 | **Budget:** $5/day | **Bidding:** MAX_CONV | **Negatives:** 62

### Assessment: Lowest volume, niche condition, too early to judge

2 clicks, $10.97, 0 conversions. Only 42 impressions in 30 days.

### Search Terms (30 days)

| Search Term | Clicks | Cost | Conv |
|---|---|---|---|
| permanent headache | 1 | $2.14 | 0 |
| (all others) | 0 | $0 | 0 |

Search terms are mostly relevant: "cervicogenic headaches", "cervicogenic", "treat cervicogenic headache", "occipital neuralgia", "neck headache treatment". The negative keywords appear to be working — no obviously wasteful matches.

**Assessment:** Volume is very low. This is expected for a niche condition keyword in a single metro area. The $5/day budget is appropriate. Give it more time.

**Decision at 14-day mark:** If 0 conversions AND <50 impressions, consider merging keywords into the Tension Cluster campaign to consolidate learning signals.

---

## 8. Paused Campaigns — Why They Were Paused

### Migraine Ads (23081715570) — Paused Feb 24
- **30 days:** 116 clicks, $399.15, 1 conversion, **$399.15 CPA**
- The single worst-performing campaign in the account
- Top keyword "migraine treatment" (PHRASE) had QS:2
- Replaced by the new Migraine campaign (23578226562) with better-structured ad groups

### Emma Harrison Penrith (22644007845) — Paused Feb 24
- **30 days:** 133 clicks, $301.98, 2 conversions, **$151.00 CPA**
- Search Partners were still enabled (now disabled, but moot since paused)
- Top search term "neurologist penrith" accounted for most spend
- Low conversion volume makes Penrith unviable as a standalone campaign

### Local Near Me - High Intent (23588589252) — Paused Feb 24
- **30 days:** 0 impressions, 0 clicks, $0 — campaign never gained traction
- Hyper-specific location keywords with no campaign history = no Quality Score data
- Keywords recommended for migration to Appointment Bookings

---

## 9. Changes Made During This Review

### Change 1: Added "australia" as negative — Migraine campaign
- **Campaign:** CURA Headache Specialist - Migraine (23578226562)
- **Action:** Campaign-level negative keyword: "australia" (BROAD)
- **Reason:** Blocking informational queries like "migraine australia", "cgrp migraine australia", "ocular migraine australia", "migraine treatment australia"
- **Resource:** `customers/4611756192/campaignCriteria/23578226562~10076141`

### Change 2: Paused "cura medical specialists" keyword — NCS campaign
- **Campaign:** CURA Nerve Conduction Studies - Sydney (23016371425)
- **Ad Group:** Specialist Names & Local (180514159130)
- **Keyword ID:** 2276727398866
- **Action:** Paused
- **Reason:** 0 conversions in 30 days ($5.71 spend). Brand queries should route to Appointment Bookings where ad copy matches general neurologist intent.

### Change 3: Added 4 NCS-specific negative keywords
- **Campaign:** CURA Nerve Conduction Studies - Sydney (23016371425)
- **Keywords added:** cranial, biopsy, brain surgeon, facial nerve (all BROAD, campaign-level)
- **Reason:** Blocking irrelevant medical/educational searches matching to NCS keywords
- **NCS negative count:** 49 → 53

---

## 10. Account-Wide Status

### Bidding Strategies
| Campaign | Strategy | Notes |
|---|---|---|
| Appointment Bookings | TARGET_CPA $5 | API may report as MAX_CONV (known discrepancy) |
| NCS Sydney | MAXIMIZE_CONVERSIONS | Performing well, $5.30 CPA |
| Near Me | MAXIMIZE_CONVERSIONS | Budget-constrained at $5/day |
| Migraine | MAXIMIZE_CONVERSIONS | Learning phase |
| Tension Cluster | MAXIMIZE_CONVERSIONS | Learning phase |
| Cervicogenic | MAXIMIZE_CONVERSIONS | Learning phase |

### Negative Keyword Counts (post-review)
| Campaign | Negatives | Notes |
|---|---|---|
| Appointment Bookings | 78 | |
| NCS Sydney | 53 | +4 added today |
| Near Me | 64 | |
| Migraine | 67 | +1 added today |
| Tension Cluster | 62 | |
| Cervicogenic | 62 | |

### Search Partners
All enabled campaigns have Search Partners disabled (confirmed 2026-02-24).

### Call Extensions
Phone number 0279068356 (AU) active on all 9 campaigns (confirmed 2026-02-24).

### Audience Signals (OBSERVATION mode)
All campaigns: 90400 (Affinity), 80144 (In-Market)
NCS additionally has 8 user interests configured.

---

## 11. Key Observations & Lessons

### 1. Never make pause decisions on less than 30 days of data
The 7-day window created a false picture for "nerve specialist sydney" (0 conversions in 7d, 8 conversions in 30d at $4.25 CPA). Pausing it would have cost ~35% of NCS campaign conversions. **Minimum 30 days of data for keyword-level pause decisions.**

### 2. The account is a two-campaign engine
Appointment Bookings (86 conv) and NCS Sydney (23 conv) deliver 100% of conversions. The four headache campaigns are experimental and may not reach profitability given the informational nature of headache search queries.

### 3. Informational search terms dominate headache queries
Migraine, Tension Cluster, and Cervicogenic campaigns are matching heavily to "what is", "symptoms", "causes", "medication" queries. These searchers are unlikely to book a neurologist appointment. This is a structural challenge — the high-intent headache queries (e.g. "headache specialist near me") are low volume.

### 4. Appointment Bookings Quality Score needs attention
Four keywords with QS:1 (all "best/top neurologist" variants). Not spending much, but improving ad relevance for these queries could unlock additional conversion volume.

### 5. Fractional conversions indicate attribution model
The 86.08 conversions in Appointment Bookings (not a round number) means Google is using data-driven attribution, splitting conversion credit. The real number of unique conversions is likely lower, but the attribution model is correctly distributing credit across the conversion path.

---

## 12. Next Review Checkpoint — March 4, 2026

**What to check at the 14-day mark (March 4-8):**

1. **Near Me:** If 0 conversions at $5/day → pause
2. **Migraine:** If CPA > $20 or 0 conversions → reduce budget $15 → $7.50/day
3. **Tension Cluster:** If CPA > $20 or 0 conversions → reduce budget $10 → $5/day
4. **Cervicogenic:** If 0 conversions AND <50 impressions → consider merging into Tension Cluster
5. **Appointment Bookings:** Check if 7-day CPA has improved from $29.62 toward TARGET_CPA $5
6. **NCS "nerve specialist sydney":** Verify continued conversions (~2-3 expected by then)
7. **Search terms:** Full audit across all 6 campaigns for new negative keyword opportunities
8. **Paused keywords residual:** Confirm "mri scan", "headaches", "neurologist headache near me" have stopped matching

**Decision criteria:**
- Pause campaign if CPA > $20 after 14 days
- Reduce budget 50% if 0 conversions after 14 days
- Star search term benchmark: "private neurologist sydney" at $0.93 CPA

---

## Appendix A: Full Search Terms by Campaign (30 Days)

### Appointment Bookings — Top 15 Search Terms
| Search Term | Clicks | Cost | Conv | CPA |
|---|---|---|---|---|
| neurologist near me | 20 | $23.52 | 6.08 | $3.87 |
| neurologist sydney | 7 | $14.07 | 2.0 | $7.04 |
| neurologist | 10 | $10.94 | 3.0 | $3.65 |
| best neurologist in sydney | 7 | $9.74 | 0.5 | $19.48 |
| neurologist drummoyne | 8 | $9.17 | 2.0 | $4.59 |
| cura drummoyne | 7 | $7.69 | 5.0 | $1.54 |
| neurology near me | 6 | $6.59 | 3.0 | $2.20 |
| neurologist rouse hill | 4 | $6.38 | 0 | — |

### NCS Sydney — Top Search Terms
| Search Term | Clicks | Cost | Conv | CPA |
|---|---|---|---|---|
| nerve conduction study near me | 4 | $7.52 | 4 | $1.88 |
| cura drummoyne | 5 | $5.32 | 0 | — |
| nerve conduction study | 2 | $2.16 | 1 | $2.16 |
| neurologists sydney | 2 | $2.13 | 0 | — |
| neurologist gregory hills | 1 | $1.80 | 1 | $1.80 |
| nerve conduction study sydney | 1 | $1.71 | 0 | — |
| diagnosis of peripheral neuropathy | 1 | $1.22 | 1 | $1.22 |

### Near Me — All Paid Search Terms
| Search Term | Clicks | Cost | Notes |
|---|---|---|---|
| cervicogenic headaches | 1 | $24.15 | Pre-negative |
| mri scan | 1 | $15.80 | EXCLUDED |
| ron granot | 1 | $8.30 | Competitor name |
| neurologist liverpool nsw | 1 | $1.74 | Out-of-area |

### Migraine — All Paid Search Terms
| Search Term | Clicks | Cost | Notes |
|---|---|---|---|
| migraine australia | 2 | $8.19 | **Negative added today** |
| chronic migraine treatments | 1 | $2.38 | Treatment-seeking |
| abdominal migraine treatment | 1 | $2.21 | Niche subtype |

### Tension Cluster — All Paid Search Terms
| Search Term | Clicks | Cost | Notes |
|---|---|---|---|
| what causes headaches everyday in females | 1 | $7.23 | Informational |
| headaches | 1 | $5.16 | EXCLUDED (pre-negative) |
| what does a neurologist treat | 1 | $3.67 | Informational |
| tension headache symptoms and causes | 1 | $0.70 | Informational |

### Cervicogenic — All Paid Search Terms
| Search Term | Clicks | Cost | Notes |
|---|---|---|---|
| permanent headache | 1 | $2.14 | Loosely relevant |
| (16 others) | 0 | $0 | Impression-only, mostly relevant |

---

## Appendix B: Keyword Quality Score Summary

| Keyword | Campaign | QS | Status | 30d Conv |
|---|---|---|---|---|
| neurologist drummoyne | Appt Bookings | 7 | ENABLED | 1.5 |
| nerve conduction studies sydney | NCS | 7 | ENABLED | 0 |
| nerve study | NCS | 7 | ENABLED | 4 |
| cura drummoyne | Appt Bookings | 6 | ENABLED | 10 |
| nerve conduction study near me | NCS | 6 | ENABLED | 4 |
| neurologist Sydney (BROAD) | Appt Bookings | 5 | ENABLED | 63.08 |
| neurologist Sydney (PHRASE) | Appt Bookings | 5 | ENABLED | 0 |
| cluster headache treatment | Tension Cluster | 5 | ENABLED | 0 |
| neurologists in sydney | Appt Bookings | 4 | ENABLED | 0 |
| neurophysiology sydney | NCS | **3** | ENABLED | 0 |
| best neurologist sydney (EXACT) | Appt Bookings | **1** | ENABLED | 2.5 |
| best neurologist Sydney (PHRASE) | Appt Bookings | **1** | ENABLED | 0 |
| top neurologist in sydney | Appt Bookings | **1** | ENABLED | 0 |
| neurologist inner west sydney | Appt Bookings | **1** | ENABLED | 0 |
