# Local documentation validation

Run: 9 October 2026, isolated documentation checkout. No IMS application execution.

## Passed

- `python3 maintainer/validate_docs.py`: 111 HTML pages; local href/src existence and fragments; unique IDs; one html/head/body/main/h1; structured JSON; JSON artifacts; page-manifest coverage; canonical origin; sitemap/AI-index exact coverage; robots and fallback search selector.
- `node maintainer/test_search.js`: explicit-card and fallback matching, no-results state and clear/reset with minimal DOM doubles. Headings retained for context.
- `node --check assets/js/docs.js`: JavaScript syntax.
- `git diff --check`: no whitespace errors.
- Illustrative report arithmetic: net quantity 12, net sales 112; row markup 1.25 versus summary ratio 1.5.
- CNAME byte-identical to documentation base; no tracked workflow directory added; no old canonical documentation origin in HTML; no local research paths in public reports.
- Manual source/evidence consistency review of affected claims, including the targeted pinned Global API-view SQL review; existing local cross-links retained and new ones checked.

## Not performed / limitations

- Rendered browser, accessibility and live external-link checks. DOM doubles are not pixel/rendering verification.
- Full standards-conformance HTML validation; the local checker verifies a useful structural subset.
- IMS builds, tests, UI interactions, workflow launches, production/API requests, database queries or recovery experiments.
- Release/deployment equivalence, external integration acceptance, live role/grant/schema/HA or secret-consumer compatibility.
- Complete generated OpenAPI or exhaustive DTO/schema validation. The added contract detail is explicitly partial and source-pinned.

Normal independent review remains required. Successful static checks do not certify application behavior or authorize merge/publication/deployment.
