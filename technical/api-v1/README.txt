IMS API 1.1.0.0 / Business API v1 external integration documentation package

Pages:
- index.html
- quick-start.html
- authentication.html
- requests.html
- reference.html
- data-semantics.html
- errors-rate-limits.html
- examples.html
- partner-data.html
- customer-delta.html
- ordinary-delta.html

Developer downloads:
- IMS_API_v1.http
- IMS_API_v1.postman_collection.json

Customers examples require approved access and customers.read. Use full-catalog
pagination for full exports; capture the Delta baseline and revision first when
maintaining an incremental mirror. Footfall requires footfall.read.
Both downloadable collections cover all 26 GET operations, plus ordinary Delta
poll/continuation and transaction timestamp examples. Use returned baseline,
policyVersion, through and continuation keys, not synthetic values. Honor
maintenance HTTP 503 and Retry-After; do not advance a failed cursor.
Replace synthetic host/company/key values before use. Never use real customer
data in shared examples. Global administrator procedures are documented at
../ims-global-api-administration.html.
