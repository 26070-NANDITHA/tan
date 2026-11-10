# Acme Corp Internal Knowledge Base Assistant — Data Classification Framework

## 1. Purpose

This document defines how company information is classified and handled by the Acme Corp Internal Knowledge Base Assistant. The objective is to protect sensitive information and ensure that data is processed only in approved environments.

## 2. Data Classification Tiers

### Tier 1 — Public Data

**Examples:**
- Public marketing blogs
- Company website information
- Public news articles

**Handling Policy:**
- Can be processed by approved cloud-based or local LLMs.
- No special confidentiality restrictions apply.
- Information must still be checked for accuracy.

### Tier 2 — Internal Data

**Examples:**
- Cafeteria menus
- Company holiday calendars
- General employee announcements

**Handling Policy:**
- Accessible only to authorized employees.
- Prefer approved internal systems and local processing.
- Do not publish internal information without authorization.

### Tier 3 — Confidential Data

**Examples:**
- Internal HR leave policies
- Company IT support documents
- Internal operational procedures

**Handling Policy:**
- Must remain within approved company-controlled infrastructure.
- Stored in the local ChromaDB vector database.
- Processed using the local Ollama model.
- Must not be transmitted to unapproved external LLM services.

### Tier 4 — Restricted Data

**Examples:**
- Passwords and authentication credentials
- Credit card numbers
- Government identification numbers
- Highly sensitive personal information

**Handling Policy:**
- Must not be stored in the knowledge base or sent to an LLM.
- Must be detected and blocked or masked before processing.- - Access must be strictly restricted.
- Follow applicable company security and privacy policies.

## 3. Data Handling Summary

| Classification | Example | Cloud LLM | Local LLM | Policy |
|---|---|---|---|---|
| Tier 1 - Public | Public website content | Allowed | Allowed | Normal processing |
| Tier 2 - Internal | Holiday calendar | Approved services only | Allowed | Authorized access |
| Tier 3 - Confidential | HR leave policies | Not allowed | Allowed in approved infrastructure | Strict local processing |
| Tier 4 - Restricted | Passwords and IDs | Not allowed | Not allowed in this project | Block or mask |

## 4. Data Protection Measures

- Use environment variables for configuration and secrets.
- Keep sensitive files out of GitHub.
- Apply PII detection and redaction before LLM processing.
- Restrict access to internal documents.
- Use approved local storage and model infrastructure.
- Require human approval for sensitive operations.

## 5. Compliance Considerations

The system should follow applicable organizational security policies and relevant privacy requirements, including India's Digital Personal Data Protection Act and other applicable regulations.

## 6. Conclusion

A clear data classification framework helps prevent accidental exposure of company information. By applying different handling rules to each classification tier, the Acme Corp Knowledge Base Assistant can provide useful responses while maintaining privacy and security.

