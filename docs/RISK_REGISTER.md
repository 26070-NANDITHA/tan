# Acme Corp Internal Knowledge Base Assistant - Risk Register

## 1. Purpose

This risk register identifies potential risks associated with developing and deploying the Acme Corp Internal Knowledge Base Assistant. It also defines technical safeguards to reduce the likelihood and impact of these risks.

## 2. Risk Assessment

| Risk ID | Risk Item | Failure Mode | Impact | Architectural Mitigation |
|---|---|---|---|---|
| RSK-01 | Secret Leak | API keys or passwords accidentally pushed to GitHub | Unauthorized access and security breaches | Use `.env` for secrets and configure pre-commit secret detection in Step 04. |
| RSK-02 | Hallucination | Assistant generates incorrect company policies | Employees may make decisions based on false information | Use RAG grounding checks and return "I don't know based on the available documents" when reliable sources are unavailable. |
| RSK-03 | PII Exfiltration | Employee emails, phone numbers or personal details are exposed to the LLM | Privacy violations and regulatory consequences | Apply regex-based PII redaction before sending text to the model in Step 06. |
| RSK-04 | Token Runaway | An agent repeatedly calls tools without stopping | Excessive compute usage and delayed responses | Set a maximum agent execution limit using `MAX_STEPS = 5` in Step 05. |
| RSK-05 | Unauthorized Action | Agent creates support tickets or performs sensitive actions without permission | Unapproved changes to company systems | Implement Human-in-the-Loop approval before executing sensitive tools in Step 05. |

## 3. Risk Prioritization

| Risk ID | Priority | Reason |
|---|---|---|
| RSK-01 | Critical | Exposed credentials can compromise systems. |
| RSK-02 | High | Incorrect policy information can mislead employees. |
| RSK-03 | Critical | Exposure of personal information can cause privacy violations. |
| RSK-04 | Medium | Uncontrolled execution can waste computing resources. |
| RSK-05 | Critical | Unauthorized actions can affect company operations. |

## 4. Monitoring and Review

- Review the risk register whenever a major architectural change is made.
- Test security controls before deployment.
- Monitor model responses for unsupported claims.
- Verify that sensitive actions require human approval.
- Update mitigations when new risks are identified.

## 5. Conclusion

Identifying risks before implementation helps make the Acme Corp Knowledge Base Assistant safer, more reliable and suitable for enterprise use. Security, privacy, cost control and human oversight are treated as core architectural requirements.
