# Maintaining the IMS documentation

This policy applies to all contributors, reviewers, and AI agents. It covers
public pages and all other public representations of their contents, including
examples, summaries, navigation, search metadata, compatibility tables, and
generated discovery files.

## Editorial policy

Public IMS documentation explains what IMS can do and how to use, configure,
maintain, troubleshoot, and implement a fresh installation independently. It is
a reference for users, administrators, implementers, and supported external API
consumers. It is not a changelog, a bug tracker, an engineering remediation
report, or a translation of the source code. Document genuine capabilities and
existing supported behavior accurately, with the prerequisites, component
versions, and limitations readers need.

## Public product boundary

Source code, tests, and an owner's deployment observations are evidence used to
verify the guide; they are not automatically publishable material. Public pages
must be written from the reader's supported **IMS screen, installer, report,
administrator task, or external API contract** rather than from the database
tables or implementation paths encountered during source review.

- Keep complete user-facing workflows, installer prompts, supported Fresh and
  Disaster Recovery procedures, product-level prerequisites, permission rules,
  report calculations, troubleshooting steps, and actual external Business API
  request/response contracts. Do not make a public API reference inaccurate by
  concealing fields that are part of its shipped contract.
- Do not disclose underlying table/column names, database transaction codes,
  document-counter mappings, internal identifiers, SQL maintenance shortcuts,
  exact security/bootstrap routes, authentication implementation mechanics,
  secret-storage locations, encryption-key recovery, credential provisioning,
  source/release paths, packaging scripts, or internal test parameters merely
  because source code contains them. Seek explicit owner approval before
  publishing any such technical interface as a supported public contract.
- Do not identify what Starco or any other installation actually uses: server
  addresses, selected SSL settings, financial connectors, tax-code defaults,
  integration credentials, schedules, company/store names, operational metrics,
  or test-environment configuration. Generic product options and regional
  capabilities can still be documented without identifying a deployment.
- Screenshots and examples must be synthetic or demonstrably free of business,
  personal, financial, credential, and company-specific configuration data.
  Remove unsafe screenshots from HTML, the image directory, and discovery text;
  keep clean menu/empty-form images and meaningful text instructions.
- When an installer or UI cannot complete a necessary operation, identify the
  unsupported/self-service gap for the owner. Never publish a database edit or
  privileged workaround to paper over that gap.

The editor's test is: **Can a user, implementer, or administrator complete a
supported task from this page without learning IMS persistence internals or
facts about a particular company's deployment?** If no, rewrite the page or
raise a specific product gap. This does not prohibit a genuinely supported
technical contract or a normal administrator workflow.

Do not include defects, even resolved defects, in public documentation. Do not
present hidden repairs, refactoring, atomicity changes, locking or race fixes,
performance repairs, or security repairs that restore intended behavior as
public features, release milestones, or compatibility milestones. Renaming a
repair as an "improvement", "hardening", or "new guarantee" does not make it a
product capability. Do not infer a new feature from a commit message or a test.

Necessary technical interfaces and recovery guarantees may be documented when
verified, relevant to readers, and stated factually as current contracts. Avoid
announcement framing, defect history, root-cause explanations, and unsupported
absolute guarantees. Explain the supported operation and its exact scope rather
than the repair that led to it. This is a contextual editorial decision, not a
ban on words such as transaction, atomicity, lock, retry, or recovery.

For example, a verified statement of which operations a transaction covers can
belong in a technical reference. A statement celebrating the repair of a partial
write or a race condition does not. These are editorial examples, not assertions
about any particular IMS implementation.

Keep engineering defects, root causes, engineering risks, tests, and remediation
in a separate approved private engineering record. Do not copy those records,
their private links, or sensitive evidence into this repository or the public
site. A directory named `maintainer` is not an access-control boundary; treat
tracked files as potentially public.

## Security claim separation

Keep descriptions of IMS security controls and runtime behavior separate from general security advice.

- **Implementation documentation** describes supported IMS mechanisms, boundaries and verified limitations, with precise component/version scope when needed. A precaution is not evidence of an implemented control or a defect.
- **General Security Recommendations** is the home for general workstation, network, credential, memory, logging, backup and operational hardening advice. Mark advice as guidance, not proof that IMS performs or lacks the described behavior.
- A statement that authorized credentials can exist in runtime process memory does not, by itself, establish credential persistence or logging. Claims about logging, storage, vulnerabilities or guarantees require independent evidence.
- For substantive behavior changes, follow the evidence and private correction-ledger policy below. Keep engineering vulnerabilities, investigations and remediation details in approved private records rather than publishing them as product documentation.

When editing security references, check nearby summaries, navigation and discovery metadata so advice cannot be mistaken for an IMS implementation fact.

## Preserve useful technical documentation

Retain accurate public product architecture, supported external API schemas,
installation and deployment steps, generic security guidance, and necessary
administrator configuration interfaces. Technical depth is welcome when it
helps perform a supported product operation; implementation detail is not
automatically necessary because it exists in source code.

Remove internal persistence mappings, environment-specific privileged details,
actual secrets, and customer-specific configuration. Use generic placeholders
for required installer/API inputs. Do not broadly delete technical content
merely because it is technical: prefer rewriting it as a complete supported UI
or installer workflow. If uncertain, flag the exact disclosure and usability
tradeoff for owner review instead of inventing behavior or hiding a required
external API field.

## Evidence and private correction ledger

Every substantive factual correction must have a corresponding entry in an
approved private correction ledger outside this public repository. Keep the
public wording readable; implementation provenance and engineering review belong
in the private record. Never invent missing evidence or treat an old
documentation statement as implementation proof.

Record, at minimum:

1. The public page/section or claim being corrected and the resulting factual
   statement (or reason for removal).
2. The owning implementation repository, full commit SHA, source path, and line
   range or symbol identifying the supporting implementation. Record all owners
   needed for a cross-component claim.
3. The relevant component and version, with the evidence linking that version
   to the implementation. Distinguish a minimum supported version from a version
   merely inspected; do not extrapolate either one.
4. Verification status, date, scope, and unresolved questions. Label facts checked
   against source as **source-verified**. Label an owner's statement about an
   installation as **owner deployment assertion**, with its source and date.
   A source-verified capability is not proof that it is deployed. An owner's
   deployment assertion is not proof of the implementation behavior.
5. Any relevant private defect, risk, test evidence, or remediation record,
   without copying it into public documentation. Tests can support verification
   but are not a substitute for examining the owning implementation.

If implementation evidence or version mapping is unavailable, mark the claim
unverified in the private ledger and seek the missing source or owner review.
Do not publish it as established fact or silently convert a deployment assertion
into source verification. Editorial-only changes, including this policy, should
identify their editorial authority rather than fabricate implementation evidence.

## Review and validation workflow

1. Classify each substantive change as a genuine capability, a necessary current
   technical contract, an accuracy correction, or private engineering material.
   Keep the last category out of public content.
2. Verify the owning implementation and version, then update the private
   correction ledger. Confirm deployment statements separately when applicable.
3. Review surrounding text, headings, examples, and public summaries so removed
   repair announcements do not survive elsewhere under new wording.
4. If a public page's inventory or summary changes, update
   `maintainer/site-manifest.json` and run `python3 maintainer/update_discovery.py`.
   The generator rewrites `llms.txt`, `sitemap.xml`, and `robots.txt`, and may
   normalize known documentation-origin references in HTML. Inspect its diff.
5. From the repository root, run:

   ```sh
   python3 maintainer/validate_docs.py
   node maintainer/test_search.js
   git diff --check
   ```

6. Review the final diff for accuracy, sensitive disclosures, and repair-as-feature
   framing. Verify any affected rendered UI separately when presentation changes.
   Report checks as passed, failed, or not run, with their limitations.

The validator checks local links/fragments, document structure, structured JSON,
manifest and discovery coverage, canonical origins, and a search CSS selector.
The JavaScript test exercises documentation search with DOM doubles. Neither
check validates IMS application behavior, deployment state, external links,
browser rendering, or editorial compliance. They do not run IMS applications.

Do not replace contextual editorial review with a broad keyword blacklist:
legitimate interface and recovery contracts use the same vocabulary as repair
reports. Propose broader automated editorial checks for review before adding
them. Publication, commits, pushes, and deployment require the task's applicable
authorization.
