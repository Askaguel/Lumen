## LVS.AI_NEXUS V0.1 — status 2026-09-21

**PARTIAL — FIRST_EXTERNAL_AGENT_NEXUS_LOOP: BLOCKED / NOT VERIFIED.**

The local prototype passed 26/26 software tests. A deterministic synthetic
two-role loop produced a persistent checkpoint. Task validation, routing,
governance checks and checkpoints are implemented locally. These tests use
test doubles, not real AI calls; they are not independent external verification.

Remaining prerequisites: authorized API access and a concrete model, hard
pre-call live-budget enforcement, and complete Slack integration with delivery
evidence. The OpenAI adapter has not been verified live. Anthropic/Gemini
connections follow only after the first successful live loop.

Next: finish budget enforcement, configure authorized access locally, then test
a real Agent A to Agent B verification loop. No browser-chat API substitute and
no promotion of synthetic results to verified external capability.

This is a status summary only, not a source-code/runtime release. Private code,
credentials and raw test logs are not published with this update.

---

# LUMEN / LVS

**LUMEN Venture System (LVS)** is an AI-native capability supply-chain project.

> **Compile once. Supply every agent ecosystem.**

## Evidence/status update — 2026-09-20

This is a documentation/status update, not a public runtime release. The private
0.3.0 candidate is **not** distributed here; public release numbering is separate.

| Component | Public maturity |
| --- | --- |
| Capability Passport | Prototype |
| Educt Compiler | Staged |
| Procurement Compiler | Planned |
| VSF | Research / local reference prototype |
| Commercial runtime | Staged, not public |
| MEFO (Mutual Exchange for Operations) | Research / staged cooperation concept |

The V29 local checkpoint reports **46 passing local tests**. Independent external
reproduction remains pending. A small synthetic multi-model experiment reached
36/36 accepted task instances after bounded retries, but only 36/60 across all
attempts. This does not establish general accuracy, token savings, or production
readiness. See [verification status](docs/verification-status.md),
[experiment limitations](docs/multimodel-experiment.md), and [VSF](docs/vsf.md).

Machine-readable: [project status](docs/machine/project-status.json) and
[verification summary](docs/machine/verification-summary.json).

## Public prototype

- [Human-facing information site](https://sites.google.com/view/lumenventuresystem)
- [LVS website](https://askaguel.github.io/Lumen/)
- [Machine catalog](https://askaguel.github.io/Lumen/machine/catalog.json)
- [Capability discovery](https://askaguel.github.io/Lumen/.well-known/lvs-capabilities.json)
- [Example capability passport](https://askaguel.github.io/Lumen/machine/capability-passport.example.json)

These are static prototype documents, not a live transaction service or an
official protocol registration. Runtime and commercial capabilities remain
staged or planned as indicated in the individual descriptors.

LVS aims to normalize a software *educt* once and make it distributable across multiple AI and agent ecosystems through machine-readable metadata, provenance, software BOMs, capability passports, evaluation data, and target-specific adapters.

## Core idea

```text
Software / Tool / Agent
        ↓
   LVS Educt Compiler
        ↓
Canonical Capability Record
        ↓
OpenAPI · MCP · A2A · UCP · Cloud Marketplaces · Human Shop · Machine Shop
```

## Current focus

- Capability Passport
- Educt normalization
- Rights & provenance metadata
- BOM / SBOM
- Evidence and validation
- Multi-ecosystem packaging
- AI-native procurement

## Repository status

Early-stage / experimental.

Public repository content is intended for specifications, schemas, examples, documentation and selected tooling. Proprietary runtime, ranking, supplier intelligence and private evaluation data may remain outside this repository.

## Rights

Project-originated material is marked:

**Copyright © 2026 Wolfgang Netik**

Third-party code and materials remain under their original licenses and rights.

See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md).

## Contact

GitHub: [Askaguel](https://github.com/Askaguel)

---

Copyright © 2026 Wolfgang Netik
