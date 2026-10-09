<!-- Purpose-written correction evidence; source-only verification. See baseline.json for version metadata. -->
# API/security documentation corrections

Docs-only. IMS.Api pin 91759f410cfcac252155ee0d6bfcf86c5024ee43, main; not verified deployed. No application execution.

## technical/security.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Program.cs#L112-L117 — Business middleware boundary
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Data/GlobalDb.cs#L296-L324 — runtime authorization
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/ShopifySecretService.cs#L47-L59 — authorized plaintext runtime read
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Security/BootstrapSessionStore.cs#L11-L59 — bootstrap sessions
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Security/GlobalAdminSessionStore.cs#L10-L66 — admin sessions

## technical/secret-vault.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Security/SecretVaultProtector.cs#L10-L79 — encryption envelope
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/SecretVaultService.cs#L18-L43 — read/write auditing
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/IntegrationSecretService.cs#L27-L69 — integration secret contract
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/ShopifySecretService.cs#L29-L111 — Shopify status, read and replacement
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Data/SecretVaultRepository.cs#L42-L75 — central vault upsert

## technical/api-v1/index.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Program.cs#L112-L117 — Business API boundary
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/StoresController.cs#L9-L41 — read-only resource example
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/PromotionsController.cs#L10-L119 — promotion routes

## technical/api-v1/authentication.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Middleware/BusinessApiKeyMiddleware.cs#L18-L81 — header, quota and authorization sequence
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Data/Business/BusinessApiRepository.cs#L16-L124 — key validity and company access
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/BusinessApiControllerBase.cs#L21-L47 — scope before company validation
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/GlobalAdminService.ApiAdmin.cs#L278-L423 — key lifecycle

## technical/api-v1/requests.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/BusinessApiControllerBase.cs#L21-L108 — shared validation
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/StoresController.cs#L21-L41 — stores envelope
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/ItemsController.cs#L22-L49 — paged envelope
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/SalesController.cs#L50-L66 — dated envelope
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/DiscountCouponEventsController.cs#L22-L92 — coupon contract
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Repositories/Business/ItemsRepository.cs — offset/count queries
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Repositories/Business/PromotionsRepository.cs#L115-L140 — inclusive interval overlap
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Repositories/Business/MarkdownsRepository.cs#L76-L104 — markdown interval overlap
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Data/Business/DbReader.cs#L8-L53 — null mapping

## technical/api-v1/errors-rate-limits.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Security/BusinessApiRateLimiter.cs#L5-L39 — per-process UTC fixed windows
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Middleware/BusinessApiKeyMiddleware.cs#L18-L126 — quota, responses and logging
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/BusinessApiControllerBase.cs#L21-L119 — explicit validation responses
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Program.cs#L76-L117 — framework and middleware setup

## technical/api-v1/reference.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/SalesController.cs#L22-L39 — sales validation
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/PurchasesController.cs#L22-L46 — purchase validation
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/InventoryMovementsController.cs#L22-L50 — movement validation
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Controllers/PromotionsController.cs#L14-L196 — promotion values and relations
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Contracts/Business/SaleDto.cs — sales field types
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Repositories/Business/SuppliersRepository.cs#L64-L80 — supplier search

## technical/api-v1/data-semantics.html

Sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Repositories/Business/SalesRepository.cs — sales view mapping
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Repositories/Business/PurchasesRepository.cs — purchase view mapping
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Contracts/Business/SaleDto.cs — sales response shape
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Contracts/Business/DiscountCouponEventDto.cs — coupon response shape

## Change summary and verification
- security.html: replace exclusive server-side implication with at-rest/runtime distinction; distinguish business/API session/module boundaries and in-process HA limitations. Retained self-protection wording with server-source links.
- secret-vault.html: document AES-GCM metadata (no key values), runtime read/status differences, replacement versus deletion, clone identity binding, lack of credential-value uniqueness, and unresolved vault/legacy-worker compatibility.
- api-v1/index.html: replace unsupported stable/future-release guarantee with pinned route baseline; distinguish 19 GET business operations from internal APIs.
- authentication.html: tighten key validity, company-404 precedence and rotation/revocation boundaries; explain header constraints and quota ordering.
- requests.html: correct null mapping; add exact empty paged envelope, unpaged distinction, date overlap/optional coupon filters and no snapshot guarantee.
- reference.html: add verified accepted values and partial typed sales DTO fields, relation validation and search semantics; do not claim full schema completeness.
- errors-rate-limits.html: explain nonuniform framework 400s, unverified 500 shape, UTC client fixed windows, per-process counter limits and request-log coverage.
- data-semantics.html: verify selected formulas against the packaged Global SQL; distinguish source-proven calculation from deployed DDL equivalence, source-data integrity, upstream discount allocation and unverified promotion units. Preserve response-shape versus upstream-data boundaries.


Additional security.html sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/GlobalAdminService.cs#L442-L479 — admin self-protection
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/GlobalAdminService.cs#L666-L684 — workstation self-protection

Additional secret-vault.html sources:
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/SmtpSecretService.cs — SMTP runtime flow
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/UpdaterSecretService.cs — updater runtime flow
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/FinanceSecretService.cs — finance runtime flow
- https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/SupplierFtpSecretService.cs — supplier FTP runtime flow

## Packaged Global view contract: targeted semantic verification

Owning source: IMS Global 1.4.0, main bb49fd38b985c4788a7310e99b299fef7dd24d7d; `IMS_Global/Sql/API_v1_Company_Contract.sql`, Git blob `c1e14dc9182999207946f070ecdd253f60e16edd`. This supersedes the earlier API-only evidence limit, not the deployment limit.

- [sales formulas, lines 80–136](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L80-L136)
- [purchase cost and header identity, lines 349–408](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L349-L408)
- [current inventory valuation, lines 430–461](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L430-L461)
- [transfer signs, lines 569–574](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L569-L574)
- [sales movements, lines 613–664](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L613-L664)
- [purchase movement eligibility, lines 670–726](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L670-L726)
- [adjustment and depreciation signs, lines 806–870](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L806-L870)
- [markdown percentage points, lines 889–904](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L889-L904)
- [promotion raw value, lines 920–966](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Sql/API_v1_Company_Contract.sql#L920-L966)

Sales net quantity is zero outside merchandise and sign-reversed for return types; no ABS/positivity constraint is inferred. Net sales subtract disc2. Purchase local/landed/expense formulas and document-level Discount Earned exclusion are explicit; header totals require composite document deduplication. Current-stock values, movement transformations and markdown percentage points are source-backed. Raw promotion getValue does not establish business units. Full deployed DDL equivalence, source data and upstream allocation remain unverified.
