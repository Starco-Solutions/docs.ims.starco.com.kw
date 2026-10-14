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
- Preserve useful architecture, schema, deployment, and generic security
  guidance. Remove actual secrets and environment-specific privileged details;
  do not remove technical documentation merely because it is technical.
- Back substantive corrections with owning implementation evidence and record
  provenance in a private correction ledger as described in the maintainer
  policy. Source verification and owner deployment assertions are distinct.
- Run the documented offline checks and review the final diff. Passing checks
  does not establish application behavior, deployment state, or editorial
  compliance. Do not commit, push, publish, or deploy without authorization.
