# Migration

This historical package has been replaced by narrower governance packages.

| Historical document | Successor document IDs |
|---|---|
| `ADR-1000-authentication-is-proof-of-claimant-control-not-resource-authorization.yaml` | `adr:authentication-and-authorization-are-separate-governance-surfaces` |
| `ADR-1001-nist-800-63-4-is-the-digital-identity-assurance-authority.yaml` | `adr:identity-proofing-and-enrollment-use-nist-sp-800-63a-4`, `adr:aal-governs-authenticator-and-authentication-strength`, `adr:fal-governs-federation-assertion-protection` |
| `ADR-1002-ial-governs-identity-proofing-and-enrollment-not-login-strength.yaml` | `adr:ial-is-independent-from-aal-and-fal` |
| `ADR-1003-aal-governs-authenticator-strength-and-authentication-events.yaml` | `adr:aal-governs-authenticator-and-authentication-strength` |
| `ADR-1004-fal-governs-federation-assertion-protection-not-proofing-or-permissions.yaml` | `adr:fal-governs-federation-assertion-protection` |
| `ADR-1005-authenticator-lifecycle-is-a-governed-security-surface.yaml` | `adr:authenticator-binding-replacement-and-revocation-are-governed` |
| `ADR-1006-webauthn-and-fido-authenticators-are-phishing-resistant-authentication-surfaces.yaml` | `adr:webauthn-is-the-relying-party-public-key-credential-surface` |
| `ADR-1007-oidc-id-tokens-represent-authentication-events-not-permission-decisions.yaml` | `adr:oidc-claims-identify-subjects-not-application-permissions` |
| `ADR-1008-session-lifecycle-and-reauthentication-are-authentication-governance-requirements.yaml` | `adr:authenticated-sessions-begin-after-authentication`, `adr:reauthentication-and-step-up-triggers-are-explicit` |
| `ADR-1009-account-recovery-must-not-weaken-target-assurance.yaml` | `adr:account-recovery-must-preserve-target-assurance` |
| `ADR-1010-authentication-events-require-audit-and-assurance-evidence.yaml` | `adr:authentication-events-require-assurance-evidence` |
| `SPEC-2000-authentication-boundary-contract.yaml` | `spc:authn-authz-boundary-contract` |
| `SPEC-2001-digital-identity-assurance-level-contract.yaml` | `spc:identity-assurance-level-selection-contract`, `spc:authenticator-assurance-contract`, `spc:federation-assurance-contract` |
| `SPEC-2002-identity-proofing-and-enrollment-contract.yaml` | `spc:identity-proofing-and-enrollment-contract` |
| `SPEC-2003-authenticator-assurance-contract.yaml` | `spc:authenticator-assurance-contract` |
| `SPEC-2004-federation-assurance-contract.yaml` | `spc:federation-assurance-contract` |
| `SPEC-2005-oidc-authentication-claims-contract.yaml` | `spc:oidc-id-token-and-userinfo-claims-contract`, `spc:oidc-id-token-validation-contract`, `spc:oidc-userinfo-and-authentication-claims-contract` |
| `SPEC-2006-webauthn-fido-authenticator-contract.yaml` | `spc:webauthn-relying-party-configuration-contract`, `spc:webauthn-registration-ceremony-contract`, `spc:webauthn-authentication-ceremony-contract` |
| `SPEC-2007-authenticator-lifecycle-contract.yaml` | `spc:authenticator-binding-and-lifecycle-contract` |
| `SPEC-2008-session-lifecycle-and-step-up-contract.yaml` | `spc:session-issuance-and-binding-contract`, `spc:reauthentication-and-step-up-contract` |
| `SPEC-2009-account-recovery-and-reset-contract.yaml` | `spc:account-recovery-and-reset-contract` |
| `SPEC-2010-authentication-audit-and-evidence-contract.yaml` | `spc:authentication-event-and-audit-contract`, `spc:session-audit-evidence-contract`, `spc:federated-subject-attribute-release-and-audit-contract` |
| `SPEC-2011-authentication-failure-mode-and-rate-limit-contract.yaml` | `spc:authentication-failure-and-rate-limit-contract` |

Replacement packages:

- `identity-proofing-enrollment-governance-pack`
- `authenticator-lifecycle-governance-pack`
- `webauthn-fido-governance-pack`
- `federated-identity-governance-pack`
- `session-security-governance-pack`
- `oidc-authn-authz-boundary-governance-pack`
