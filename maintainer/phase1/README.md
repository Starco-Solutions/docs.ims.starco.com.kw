# Documentation Phase 1 review

Review date: 9 October 2026. Scope: documentation only, based on the immutable main snapshots in [baseline.json](baseline.json). No application changes, application execution, production calls, deployment, hosting changes or workflow additions. This is a draft correction set requiring normal review; it does not authorize publication.

- [All 20 audit findings and closure status](correction-ledger.md)
- [Global, architecture and site evidence](global-site-evidence.md)
- [Client workflow evidence](client-evidence.md)
- [API and security evidence](api-evidence.md)
- [Worker and integration evidence](worker-evidence.md)
- [Outstanding decisions and next phases](outstanding-and-roadmap.md)
- [Local validation results](validation.md)

A corrected documentation claim does not close the associated operational or application limitation. Source-verified means static evidence; reported policy and runtime-unverified behavior are separately identified. Source links may require repository access.

## Maintaining these pages

Preserve accurate content and existing URLs. Every significant behavioral correction needs a page/section, reason, component version, immutable source SHA and path/lines. Do not substitute an unmerged branch for released evidence. Reconcile component compatibility before describing a full deployed system. Public architecture, schema, business rules, generic role/configuration, PostgreSQL replication/HA, backup/restore and deployment guidance are legitimate documentation topics. Never add actual secrets, production addresses or access material, sensitive network configuration, private vault locations or privileged environment details.

Use the shared origin and page manifest in `maintainer/site-manifest.json`; run `python3 maintainer/update_discovery.py` after adding pages and `python3 maintainer/validate_docs.py` for local static checks. No CI workflow is added. Local checks do not execute the IMS applications or establish runtime behavior.
