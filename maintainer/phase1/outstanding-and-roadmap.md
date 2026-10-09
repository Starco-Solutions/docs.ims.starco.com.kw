# Outstanding decisions and next phases

## Owner decisions / release gates

1. Release owners: confirm which pinned source versions actually shipped together. Version metadata is not release or deployment evidence.
2. Integration/API owners: resolve vault-only secret setters versus legacy-reading Autos and Shopify workers. Identify the approved compatible release or supported bridge; do not infer a production outage or invent a migration workaround.
3. Global/API owners: administrator identity and policy membership replacement/fallback are under Partner Data Phase 2 review. This docs change only qualifies existing provisional-main behavior and implements none of those changes. Confirm intended least-privilege rules and approved release before documenting corrected behavior.
4. Finance/component owner: decide payment-type compatibility and consistent enforcement. Keep supported configuration exclusions until resolved; do not bless accidental checkbox combinations.
5. Operations/finance owners: approve recovery authority and environment-specific procedures for partial provisioning, credential-save failure, interrupted posting and imported-but-unfulfilled orders. Current guidance stops at verification/escalation rather than inventing SQL repair.

## Newly verified source limitations, separate from the original 20

- Global provisioning, role changes, secret updates and multi-company synchronization are staged, not distributed atomic operations. Reused roles are not automatically stripped of prior privilege.
- Autos polling pauses during execution; daily jobs and report schedules use different clocks. Supplier notification watermark can advance after a failed send. Maintenance state is cooperative and not universally cleared by the outer error handler.
- Outbound Integration Center sends to configured Endpoint URL; target code is metadata. Success means HTTP 2xx, not business acceptance. Revisit-based retries are not exactly-once delivery, and a failed success-log write can allow resend.
- Shopify import commits separately from fulfillment. Existing imported orders are skipped by the automatic new-order path; manual retrieval is not a fulfillment replay. Some catalog misses do not fail an inventory batch, so watermark progress is not proof every item matched.
- API quotas and sessions are process-local at the reviewed pin. Distributed deployment behavior, replay/snapshot consistency and deployed HA are unverified. Readiness of the Global DB is not comprehensive worker/company health.

## Phase 2: owners and source contracts

Reconcile the decisions above against approved release commits; document canonical schema/view DDL, database role grants and migrations. Complete Business API DTO nullability/requiredness, validation/error schemas and generated OpenAPI from approved source. Selected formulas are already verified in the packaged Global API-view contract. Reconcile deployed DDL and data integrity, upstream discount allocation and promotion units; review additional view semantics before expansion. Acceptance: owner-approved release-to-source/schema map, reproducible field-level contract and no provisional claim disguised as production truth.

## Phase 3: operational completeness

Develop supported public PostgreSQL installation/configuration, replication, repmgr/keepalived or other chosen HA, generic roles, backup/restore and disaster-recovery guidance with official references and product-owner approval. These topics are allowed publicly; real secrets, production addresses/access, sensitive network specifics, private vault locations and privileged environment details stay excluded. Confirm dependency matrix and installer/DSN packaging. Define recovery objectives and approved reconciliation procedures without destructive guesswork. Acceptance: reviewed runbooks and explicit prerequisite/authority boundaries; runtime exercises require separate authorization.

## Phase 4: broader business and UX review

Resolve Purchase VAT lifecycle/effective dates, closed-period boundaries, currency units/precedence, historical valuation and cross-report KPI populations, used campaign edits, signed cash receipts and import/override authority. Add reviewed examples and rendered documentation checks. Preserve source limitations until owners resolve them. Application branches and pending Purchase work are outside this documentation change.

## Publication

This work is a draft review change. Merge, publication, deployment, application builds/tests, production calls and workflow launches are not part of Phase 1 execution. Hosting, CNAME, DNS, repository settings and automation are unchanged by the documentation edits.
