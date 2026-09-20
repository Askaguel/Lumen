# Verification status

Status snapshot: 2026-09-20. This is an evidence summary, not a public software release.

The private V29 / 0.3.0 checkpoint recorded 46 passing local tests. Its private
package was restored and checked on the same host with the existing dependency
environment. That is a local restore check, not an independent clean-room audit.

Local checks cover reference schemas, evidence freshness, hashing, regression
behavior, and a bounded VSF round trip. Neither structural validation nor a hash
proves factual truth, legal compliance, certification, or commercial readiness.

Independent external reproduction: **PENDING**. Exact token consumption, cost
savings, and a matched independent ChatGPT-only baseline: **UNKNOWN / NOT MEASURED**.
The public materials expose summaries; private implementations and raw histories
are not included. A reader cannot reproduce all 46 private tests from this repo.

The public CI checks only the integrity of the public documentation and JSON.
It does not run or certify the private test suite.

See [project status](machine/project-status.json),
[verification summary](machine/verification-summary.json),
[experiment](multimodel-experiment.md), [VSF](vsf.md), and [home](index.html).

Copyright © 2026 Wolfgang Netik / LVS. Existing repository license and third-party rights apply.
