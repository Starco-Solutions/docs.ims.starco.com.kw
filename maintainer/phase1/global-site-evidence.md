# Global, architecture and site correction evidence

Owning versions: IMS Global 1.4.0, IMS client 9.4.4, IMS.Api v1 route baseline. All are provisional main snapshots, not deployed release verification. Complete metadata: [baseline.json](baseline.json).

## technical/ims-global.html#create-db; technical/multi-company.html#new-company; technical/postgresql/index.html#prerequisites

Provisioning prerequisites and stages; prevent atomicity assumptions and unsafe retries.

- [DBContext.cs:271–291](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L271-L291)
- [DBContext.cs:343–381](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L343-L381)
- [DBContext.cs:603–773](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L603-L773)
- [ManageCompanies.cs:425–501](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/ManageCompanies.cs#L425-L501)
- [DBContext.cs:1039–1040](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L1039-L1040)
- [DBContext.cs:1239–1274](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L1239-L1274)
- [Services/GlobalAdminService.cs:335–351](https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/GlobalAdminService.cs#L335-L351)

## technical/ims-global.html#database-password

Shared PostgreSQL roles and partial credential-save risks; reused-role privilege caveat.

- [ManageCompanies.cs:221–376](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/ManageCompanies.cs#L221-L376)
- [DBContext.cs:383–428](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L383-L428)
- [DBContext.cs:474–492](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L474-L492)

## technical/ims-global.html#users; technical/multi-company.html user assignment

Global save versus per-company synchronization; replacement/fallback warning, owner review remains open.

- [UsersAccounts.cs:413–513](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/UsersAccounts.cs#L413-L513)
- [UsersAccounts.cs:584–784](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/UsersAccounts.cs#L584-L784)

## technical/ims-global.html access; system/workstation-admin.html; system/index.html

Current Global screen, fields and actions; remove stale company-local route and unavailable controls.

- [WorkstationsAdmin.cs:62–104](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/WorkstationsAdmin.cs#L62-L104)
- [WorkstationsAdmin.cs:154–205](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/WorkstationsAdmin.cs#L154-L205)
- [WorkstationsAdmin.cs:308–310](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/WorkstationsAdmin.cs#L308-L310)
- [AdminApiClient.cs:15–79](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/AdminApiClient.cs#L15-L79)
- [Main.cs:24–94](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/Main.cs#L24-L94)
- [Main.Designer.cs:867–878](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/Main.Designer.cs#L867-L878)

## technical/architecture.html#runtime-boundaries

Direct company database connection and mixed worker credential boundary; no universal API proxy/deployed compatibility claim.

- [Actions/Security/BuildCompanyConnectionString.cs:8–26](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/Actions/Security/BuildCompanyConnectionString.cs#L8-L26)
- [UsersAccounts.cs:545–576](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/UsersAccounts.cs#L545-L576)
- [Services/IntegrationSecretService.cs:38–49](https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/IntegrationSecretService.cs#L38-L49)
- [Services/ShopifySecretService.cs:61–92](https://github.com/Starco-Solutions/IMS_API/blob/91759f410cfcac252155ee0d6bfcf86c5024ee43/src/IMS.Api/Services/ShopifySecretService.cs#L61-L92)

## technical/postgresql/index.html#prerequisites and #schema-baseline

Generic source-backed prerequisite checklist and legacy notes warning; exact package/version and complete schema map deferred.

- [App.config:5–11](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/App.config#L5-L11)
- [IMS.csproj:8–12](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/IMS.csproj#L8-L12)
- [IMS.csproj:76–120](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/IMS.csproj#L76-L120)
- [IMS_Components/DBConnectionStatics.cs:79–112](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/IMS_Components/DBConnectionStatics.cs#L79-L112)
- [IMS_Global.csproj:27–31](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/IMS_Global.csproj#L27-L31)
- [DBContext.cs:271–291](https://github.com/Starco-Solutions/IMS_Global/blob/bb49fd38b985c4788a7310e99b299fef7dd24d7d/IMS_Global/DBContext.cs#L271-L291)

## Site integrity and discovery (findings 16–18, 20)

Documentation base: [a4dd0a0c533eb3918ae6a9bbdee244b932b2a016](https://github.com/Starco-Solutions/docs.ims.starco.com.kw/tree/a4dd0a0c533eb3918ae6a9bbdee244b932b2a016).

- `CNAME:1` already selects docs.ims.starco.com.kw; it remains unchanged. `index.html:8–10`, `robots.txt:4`, `sitemap.xml:3–112` and llms.txt used the other host. Metadata now shares the origin in `maintainer/site-manifest.json`; the generator is offline and makes no DNS/hosting change.
- `llms.txt` omitted sales/index.html, items-search.html, open-close-pos.html, open-drawer.html, sales-transactions.html and transactions-expert.html. All six now appear in the manifest-driven AI index and sitemap, alongside the new source-baseline page.
- `assets/js/docs.js:12–29` applies search-hidden to fallback blocks; `assets/css/docs.css:44` previously required data-search-item as well. CSS now handles the assigned class. Headings remain visible for context. This is a static fix; browser rendering was not exercised.
- `technical/source-baseline.html`, `maintainer/phase1/baseline.json` and correction registers distinguish source version metadata from reported policy and runtime verification. The deployment date/version mapping remains owner work.

The architecture credential-consumer evidence is expanded in [worker evidence](worker-evidence.md). No blanket claim is made that vault administration and all reviewed workers form one compatible deployment.
