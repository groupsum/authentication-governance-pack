<div align="center">

<h1>authentication-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/authentication-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/authentication-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/authentication-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/authentication-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/authentication-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/authentication-governance-pack.svg"></a>
  <a href="https://pypi.org/project/authentication-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/authentication-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/authentication-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/authentication-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/authentication-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/authentication-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p><a href="https://github.com/groupsum/authentication-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fauthentication--governance--pack-181717?logo=github"></a></p>

</div>

`authentication-governance-pack` is an SSOT Registry pack for digital identity proofing, authenticator assurance, federation assurance, credential lifecycle, session security, WebAuthn/FIDO authenticators, OIDC authentication claims, account recovery, and authentication evidence.

It governs how a repository proves that a claimant controls authenticators for a subscriber account, how strongly identity was proofed, how federation assertions are protected, and how sessions and recovery preserve the target assurance level. It does not govern application permissions.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed Architecture Decision Records (ADRs) and Specifications (SPECs) for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents that downstream repositories can synchronize into their local `.ssot` registry and link to features, tests, claims, evidence, and releases.

## Why This Pack Exists

Authentication governance is not authorization governance. Teams need stable requirements for identity proofing, authenticator strength, federation assertions, session lifecycle, recovery, and audit evidence without confusing those controls with resource permissions.

## IAL, AAL, And FAL

NIST SP 800-63-4 separates digital identity assurance into three functions:

- **IAL**, Identity Assurance Level, covers identity proofing and enrollment: how strongly the credential service provider established the applicant identity and subscriber account.
- **AAL**, Authentication Assurance Level, covers authentication events: how much confidence the verifier has that the claimant controls authenticators bound to the subscriber account.
- **FAL**, Federation Assurance Level, covers federation assertions: how strongly identity-provider assertions are protected and validated by a relying party.

IAL is not MFA strength. AAL is not identity proofing. FAL is not authorization permissioning.

## Pack Metadata

- Pack ID: `pack:authentication`
- PyPI package: `authentication-governance-pack`
- Import package: `authentication_governance_pack`
- GitHub repository: [groupsum/authentication-governance-pack](https://github.com/groupsum/authentication-governance-pack)
- Reservation owner: `extension-pack:authentication-governance-pack`

## Domain Focus

- NIST SP 800-63-4 digital identity assurance
- IAL identity proofing and enrollment
- AAL authenticator and authentication-event strength
- FAL federation assertion protection
- OIDC ID Token authentication claims, `acr`, and `amr`
- WebAuthn and FIDO authenticators
- authenticator lifecycle, account recovery, reset, and revocation
- session lifecycle, reauthentication, step-up, and logout
- authentication audit and release evidence

## Authority Sources

- [NIST SP 800-63-4 Digital Identity Guidelines](https://pages.nist.gov/800-63-4/)
- [NIST SP 800-63A-4 Identity Proofing and Enrollment](https://pages.nist.gov/800-63-4/sp800-63a.html)
- [NIST SP 800-63B-4 Authentication and Authenticator Lifecycle](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [NIST SP 800-63C-4 Federation and Assertions](https://pages.nist.gov/800-63-4/sp800-63c.html)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0-18.html)
- [OpenID Connect Extended Authentication Profile ACR Values 1.0](https://openid.net/specs/openid-connect-eap-acr-values-1_0.html)
- [W3C WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/)
- [FIDO CTAP 2.2](https://fidoalliance.org/specs/fido-v2.2-ps-20250714/fido-client-to-authenticator-protocol-v2.2-ps-20250714.html)
- [OAuth 2.0 Security Best Current Practice, RFC 9700](https://www.rfc-editor.org/rfc/rfc9700)

## Included ADRs And SPECs

This release includes 11 ADR templates and 12 SPEC templates covering authentication boundaries, NIST SP 800-63-4 assurance, IAL, AAL, FAL, OIDC authentication claims, WebAuthn/FIDO authenticators, authenticator lifecycle, session lifecycle, account recovery, failure handling, and authentication evidence.

## Install With uv

```bash
uv add authentication-governance-pack
uv add ssot-registry authentication-governance-pack
uvx --from ssot-registry --with authentication-governance-pack ssot --help
```

## Use With The SSOT Registry CLI

```bash
uv run ssot pack inspect authentication_governance_pack
uv run ssot pack preflight . authentication_governance_pack --all
uv run ssot pack sync . authentication_governance_pack --all --trust --yes
uv run ssot validate .
uv run ssot spec get . --id spc:pack.authentication.authentication-boundary-contract
```

## Programmatic Usage

```python
from authentication_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-authentication-boundary-contract.yaml")
```

## Resources

- GitHub repository: [groupsum/authentication-governance-pack](https://github.com/groupsum/authentication-governance-pack)
- PyPI package: [authentication-governance-pack](https://pypi.org/project/authentication-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
