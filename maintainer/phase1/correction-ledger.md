# Original audit: all 20 findings

Status is documentation closure, not certification of application behavior. “Qualified” means the unsupported guarantee is narrowed and the remaining owner/runtime question is still open. Evidence registers supply immutable source paths/lines and baseline.json supplies owning versions.

| # | Finding | Status | Changed pages / sections and reason | Evidence |
|---|---|---|---|---|
| 1 | Workstation administration | Corrected | system/workstation-admin; system overview; current Global route replaces stale company-local screen | Global/site |
| 2 | Updater credential storage | Corrected | system/settings, updater; separate nonsecret settings, vault status/update and retained legacy values | Client |
| 3 | NONE versus secret removal | Corrected | integration/integration-center, authentication; mode change is not deletion/revocation | Worker; API |
| 4 | Stock Maintenance | Qualified | tools/stock-maintenance, operation/recovery; transaction does not prove blocking or exact state restoration | Client |
| 5 | Purchase and finance recovery | Qualified | inventory/purchases, finalize/post; best-effort recovery and separate financial acknowledgement | Client |
| 6 | Saved sale versus print | Corrected | sales/sales-transactions, saving; verify/reprint instead of duplicating uncertain sale | Client |
| 7 | Clone credentials | Corrected | integration/integration-center, cloning; key never copied | Worker |
| 8 | Online order reconciliation | Corrected | shopify/incoming-orders, recovery decision guide; preserve distinct failure/reversal instructions | Client |
| 9 | Shopify credential uniqueness | Qualified | shopify/manage-profiles, validation/secrets; proven identifiers only, no credential-value guarantee | Worker; API |
| 10 | Deployment prerequisites | Qualified | technical/postgresql, prerequisites; publish source-backed generic checklist; exact installation matrix/packaging remains unverified | Global/site |
| 11 | Canonical schema/release docs | Deferred in part | technical/postgresql, schema baseline; packaged Global SQL identified and legacy notes disclaimed; complete release/schema/upgrade mapping awaits owners | Global/site; roadmap |
| 12 | Startup order | Corrected | getting-started/main-screen; API/workstation/global login precede company database | Client |
| 13 | Report definitions | Corrected | reports/main-sales-report and purchasing-report; net quantities and different markup denominators with examples | Client |
| 14 | Payment compatibility | Qualified; owner-blocked | financial/sales-payment-types; supported policy retained, universal UI enforcement claim removed; no invented truth table | Client |
| 15 | Money/stock uncertain outcomes | Qualified | financial posting/posted-transactions; inventory stock-transfer/transfer-following; reconcile outcomes before retry/acceptance | Client |
| 16 | Discovery origin | Corrected | all HTML canonical/structured URLs, robots, sitemap, llms; shared docs.ims.starco.com.kw origin; CNAME untouched | Global/site; validator |
| 17 | Missing Sales AI index | Corrected | all six sales pages included in shared page manifest and llms | Global/site; validator |
| 18 | Search fallback selector | Corrected statically | assets/css/docs.css and docs.js; class selector covers fallback blocks, headings retained | Global/site; rendered check still pending |
| 19 | Full API schema contract | Qualified; complete schema deferred | technical/api-v1 requests/reference/auth/errors/semantics; bounded source-backed envelopes, validation, types, selected packaged view formulas and limits; no complete OpenAPI claim | API; roadmap |
| 20 | Traceable baseline | Corrected for this pass | source-baseline page, baseline.json, evidence registers and per-page links; provisional source versus release/runtime explicit | All evidence registers |

Evidence: [Client](client-evidence.md), [Worker](worker-evidence.md), [API](api-evidence.md), [Global/site](global-site-evidence.md), [open decisions](outstanding-and-roadmap.md).
