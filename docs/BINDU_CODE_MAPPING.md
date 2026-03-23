# BINDU CODE MAPPING

This document explains how the canonical Bindu logic should be implemented in runtime code.

It does not define a new law.
It translates `BINDU_CANON.md` into executable logic for `gitcube-os`.

---

## Canonical Input

Bindu reads the following runtime metrics:

- shadow
- coherence
- target_fit
- vitality

These metrics must already be computed before Bindu is called.

---

## Canonical Output

Bindu may return:

- COMMIT
- SOFT_COMMIT
- REJECT
- REROUTE

The minimal runtime implementation may begin with:

- COMMIT
- SOFT_COMMIT
- REJECT

REROUTE may be added by loop logic.

---

## Minimal Runtime Mapping

Suggested runtime logic:

    if coherence >= 0.85 and shadow <= 0.10:
        decision = "COMMIT"
    elif coherence >= 0.80 and shadow <= 0.15:
        decision = "SOFT_COMMIT"
    else:
        decision = "REJECT"

---

## Extended Runtime Checks

Optional checks:

    if vitality < 0.20:
        decision = "REJECT"

    if target_fit < 0.30:
        decision = "REJECT"

These checks should remain simple in the OS layer.

---

## Runtime Separation Rule

Navigator defines:
- meaning
- thresholds
- canonical semantics

OS defines:
- executable function
- memory write behavior
- reroute behavior

Therefore:

- `BINDU_CANON.md` belongs in Navigator
- `runtime/bindu.py` belongs in GitCube OS

---

## One-line Summary

Navigator defines what Bindu means.
OS implements how Bindu runs.
