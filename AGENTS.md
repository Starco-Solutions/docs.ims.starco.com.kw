# IMS documentation contributor instructions

Before editing this repository, read [maintainer/README.md](maintainer/README.md).
Its editorial policy applies to developers, reviewers, and AI agents, including
public HTML, examples, search descriptions, navigation, and generated discovery
files.

- Describe genuine capabilities and supported behavior accurately. Public IMS
  documentation is not a changelog or a record of engineering repairs.
- Keep defects (including resolved defects), root causes, risks, tests, and
  remediation in an approved private engineering record, outside this public
  repository. Do not repackage repairs as features or milestones.
- Public IMS documentation explains what IMS can do and how to use, configure,
  maintain, troubleshoot, and perform a fresh installation independently.
  Preserve exact user-facing controls, supported installer procedures, and the
  real externally supported Business API contract.
- Source code and tests are verification evidence, not text to translate into
  public documentation. Do not expose internal table/column names, transaction
  codes, document-counter mappings, implementation-specific security routes,
  bootstrap shortcuts, credential storage/recovery mechanics, build scripts,
  or package internals unless the owner explicitly approves a necessary public
  interface. Avoid company-specific installation choices and tested settings.
- Use fictional, non-identifiable data in all examples and screenshots. Remove
  business-data screenshots from both HTML and published assets. If a supported
  operation cannot be explained without an internal workaround, raise the gap
  instead of publishing that workaround.
- Back substantive corrections with owning implementation evidence and record
  provenance in a private correction ledger as described in the maintainer
  policy. Source verification and owner deployment assertions are distinct.
- Run the documented offline checks and review the final diff. Passing checks
  does not establish application behavior, deployment state, or editorial
  compliance. Do not commit, push, publish, or deploy without authorization.
