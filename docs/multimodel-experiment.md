# Bounded multi-model experiment

Recorded on 2026-09-20; 12 simple synthetic tasks covering transformations,
fixtures, extraction and diffs. Each provider received the same small corpus.
Acceptance required deterministic agreement with the local expected results.

| Provider | First attempt | Final after at most one retry |
| --- | --- | --- |
| Gemini | 12/12 accepted | 12/12; no retry |
| Copilot | 0/12 accepted; invalid JSON | 12/12; one retry |
| Meta AI | 0/12 accepted; invalid JSON | 12/12; one retry |

36/36 final task instances were accepted. Across the 60 task attempts, 36 were
accepted (60%). The first-pass transport failures are retained, not hidden by
the final score. A missing valid envelope does not by itself prove incorrect
semantic reasoning.

This is not a general model ranking or an estimate of real-world accuracy. It
does not justify automatic production routing. The author knew the oracle;
there was no independently measured ChatGPT-only baseline. Exact provider
tokens, total-system tokens, costs and matched timing are unknown. No 70% saving
or general 100% quality claim follows from this experiment.

Next proposed evaluation: unseen matched variants, identical fenced JSON
transport, instrumented usage and an independent baseline. No private project
upload is needed. Raw provider sessions remain private.

[Verification status](verification-status.md) · [Home](index.html)
