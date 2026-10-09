<!-- Purpose-written correction evidence; source-only verification. See baseline.json for version metadata. -->
# Client workflow documentation correction ledger


All source evidence is **provisional main**, borhannasr/IMS_PG at `0d0ec8557954017f067b06088bddae23bef96909`. Component: IMS desktop client. Source AssemblyVersion/AssemblyFileVersion **9.4.4**, [AssemblyInfo.cs lines 34–35](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/Properties/AssemblyInfo.cs#L34-L35). This source metadata is not proof of a deployed release. Deployment baseline and operational-owner approvals remain unresolved. Existing page version badges are context labels, not runtime certification.

Documentation baseline: Starco-Solutions/docs.ims.starco.com.kw at `a4dd0a0c533eb3918ae6a9bbdee244b932b2a016`. Covers original findings 2, 4–6, 8 and 12–15. Accurate existing layout/content was retained outside the narrow corrections.

## system/settings.html
- Sections: #update-server
- Correction and reason: Finding 2: Separate nonsecret URL/login storage from Security Guard password status/update, explain stored mask and unchanged/blank preservation, qualify legacy migration and separate settings writes.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_System/SystemSettings.cs L495–563](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_System/SystemSettings.cs#L495-L563)
  - [_Menu_System/SystemSettings.cs L687–713](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_System/SystemSettings.cs#L687-L713)
  - [_Menu_System/SystemSettings.cs L822–823](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_System/SystemSettings.cs#L822-L823)
  - [_Menu_System/SystemSettings.cs L867–901](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_System/SystemSettings.cs#L867-L901)

## tools/stock-maintenance.html
- Sections: #run, #process, #safety
- Correction and reason: Finding 4: Require a maintenance window and coordinated activity pause, remove cross-session blocking/exact restoration guarantees, retain attempted transaction rollback, distinguish post-commit log errors and require store-state verification.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Tools/StockMaintenace.cs L86–120](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Tools/StockMaintenace.cs#L86-L120)
  - [_Menu_Tools/StockMaintenace.cs L298–350](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Tools/StockMaintenace.cs#L298-L350)

## inventory/purchases.html
- Sections: #recovery, #journal
- Correction and reason: Finding 5: Replace guaranteed manual recovery recipe with best-effort recovery and administrator reconciliation before finalization/Roll Back retry. Add separate financial write/IMS acknowledgement warning, including ambiguous displayed success. No pending Purchase refactor claim.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Inventory/_Purchase/Purchases.cs L2337–2378](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/_Purchase/Purchases.cs#L2337-L2378)
  - [_Menu_Inventory/_Purchase/Purchases.cs L2653–2740](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/_Purchase/Purchases.cs#L2653-L2740)
  - [_Menu_Inventory/_Purchase/Purchases.cs L2753–2777](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/_Purchase/Purchases.cs#L2753-L2777)
  - [_Menu_Inventory/_Purchase/PostPurchase.cs L358–361](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/_Purchase/PostPurchase.cs#L358-L361)
  - [_Menu_Inventory/_Purchase/PostPurchase.cs L706–749](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/_Purchase/PostPurchase.cs#L706-L749)

## sales/sales-transactions.html
- Sections: #save-print
- Correction and reason: Finding 6: Distinguish saved sale from printed receipt and uncertain save. Verify existing invoice and use existing Transactions Expert print/email anchor before creating another sale.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_SalesTransactions/SalesTrans.cs L5742–5807](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_SalesTransactions/SalesTrans.cs#L5742-L5807)
  - [_SalesTransactions/SalesTrans.cs L5889–5916](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_SalesTransactions/SalesTrans.cs#L5889-L5916)

## shopify/incoming-orders.html
- Sections: #reconciliation
- Correction and reason: Finding 8: Add decision guide preserving distinct refresh, reconcile, uncertain-fulfillment, same-reversal retry and pre-commit reversal-not-saved messages. No replacement-order or database-remapping repair recipe.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Shopify/OnlineOrders.cs L2804–2833](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Shopify/OnlineOrders.cs#L2804-L2833)
  - [_Menu_Shopify/OnlineOrders.cs L2885–2899](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Shopify/OnlineOrders.cs#L2885-L2899)
  - [_Menu_Shopify/OnlineOrders.cs L3668–3685](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Shopify/OnlineOrders.cs#L3668-L3685)

## getting-started/main-screen.html
- Sections: #startup
- Correction and reason: Finding 12: Correct startup to bootstrap API/workstation, global identity, company selection, company database then initialization/access; separate troubleshooting dependencies.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [Main.cs L406–456](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/Main.cs#L406-L456)
  - [Main.cs L540–635](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/Main.cs#L540-L635)

## reports/main-sales-report.html
- Sections: #kpis
- Correction and reason: Finding 13A: Remove double subtraction of returns from Net Qty, state signed-component amount sum, scope inventory quantities, and add illustrative sale/return arithmetic.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Reports/MainSalesReport.cs L3294–3308](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Reports/MainSalesReport.cs#L3294-L3308)
  - [_Menu_Reports/MainSalesReport.cs L3327–3338](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Reports/MainSalesReport.cs#L3327-L3338)
  - [_Menu_Reports/MainSalesReport.cs L3379–3387](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Reports/MainSalesReport.cs#L3379-L3387)

## reports/purchasing-report.html
- Sections: #footer-totals
- Correction and reason: Finding 13B: Distinguish row Retail/Landed markup from bottom Retail/Local markup and add nonzero-expense example. No zero-denominator display guarantee, business-intention assertion or expanded return example.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Reports/PurchasingReports.cs L1328–1337](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Reports/PurchasingReports.cs#L1328-L1337)
  - [_Menu_Reports/PurchasingReports.cs L1349–1356](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Reports/PurchasingReports.cs#L1349-L1356)
  - [_Menu_Reports/PurchasingReports.cs L1434–1457](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Reports/PurchasingReports.cs#L1434-L1457)

## financial/sales-payment-types.html
- Sections: #fields, #special-types, #edit
- Correction and reason: Finding 14, OWNER BLOCKED: Retain existing supported exclusions (Star Cards and BNPL exclude Only Refund), remove broad checkbox-availability/universal-enforcement promises, label guidance as supported configuration policy and require owner reconciliation of policy/UI discrepancy. No definitive truth table and no accidental combination legitimized.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Finance/SalesPayments.cs L152–166](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Finance/SalesPayments.cs#L152-L166)
  - [_Menu_Finance/SalesPayments.cs L198–211](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Finance/SalesPayments.cs#L198-L211)
  - [_Menu_Finance/SalesPayments.cs L332–340](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Finance/SalesPayments.cs#L332-L340)
  - [_Menu_Finance/SalesPayments.cs L354–410](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Finance/SalesPayments.cs#L354-L410)

## financial/posting.html
- Sections: #interrupted-posting
- Correction and reason: Finding 15: Separate external journal, IMS acknowledgement and log; retain journal/type/store/branch/error and require authorized finance reconciliation before retries, with verified Posted Transactions totals link.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Finance/Posting.cs L963–971](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Finance/Posting.cs#L963-L971)

## financial/posted-transactions.html
- Sections: #interrupted-unposting
- Correction and reason: Finding 15: Separate deletion/acknowledgement/log and require reconciliation before unpost or repost retries; missing acknowledgement does not prove no deletion.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Finance/PostedTransactions.cs L257–273](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Finance/PostedTransactions.cs#L257-L273)

## inventory/stock-transfer.html
- Sections: #save
- Correction and reason: Finding 15: Separate saving/printing and verify voucher plus both stores movements before duplicate creation; escalate uncertain save/downstream status. No guaranteed recovery display claim.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Inventory/StockTransfer.cs L649–720](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransfer.cs#L649-L720)
  - [_Menu_Inventory/StockTransfer.cs L805–855](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransfer.cs#L805-L855)
  - [_Menu_Inventory/StockTransfer.cs L1135–1160](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransfer.cs#L1135-L1160)

## inventory/transfer-following.html
- Sections: #variance, #accept
- Correction and reason: Finding 15: Acceptance confirms receiving, not corrective stock movement; review counts/retain variance and resolve through authorized separate adjustment process. Qualify variance sign to reloaded values because remove-one uses inconsistent sign.
- Component/version: IMS desktop client, source 9.4.4, provisional main `0d0ec8557954017f067b06088bddae23bef96909`.
- Pinned evidence:
  - [_Menu_Inventory/StockTransFollowing.cs L82–98](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransFollowing.cs#L82-L98)
  - [_Menu_Inventory/StockTransFollowing.cs L187–199](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransFollowing.cs#L187-L199)
  - [_Menu_Inventory/StockTransFollowing.cs L289–410](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransFollowing.cs#L289-L410)
  - [_Menu_Inventory/StockTransFollowing.cs L420–446](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransFollowing.cs#L420-L446)
  - [_Menu_Inventory/StockTransFollowing.cs L512–553](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransFollowing.cs#L512-L553)
  - [_Menu_Inventory/StockTransFollowing.cs L581–607](https://github.com/borhannasr/IMS_PG/blob/0d0ec8557954017f067b06088bddae23bef96909/StarcoIMS/_Menu_Inventory/StockTransFollowing.cs#L581-L607)

## Verification and unresolved scope
- Static diff/whitespace review completed with `git diff --check`. No builds, application tests or workflows were run.
- Existing cross-links used: `sales/transactions-expert.html#print-email` and `financial/posted-transactions.html#financial-totals`; anchors verified in local documents.
- Financial payment policy remains owner-blocked; the prose explicitly avoids a definitive enforcement table.
- No Purchase branch or unmerged changes were inspected or modified.
- Current/deployed-version claims were not introduced; source pins alone remain insufficient deployment evidence.
