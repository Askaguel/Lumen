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
