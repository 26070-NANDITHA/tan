# Acme Corp Internal Knowledge Base Assistant

## 1. Executive Summary

The Acme Corp Internal Knowledge Base Assistant is an AI-powered application designed to help employees find answers to common HR and IT questions using internal company documents.

The system uses Retrieval-Augmented Generation (RAG), a local Large Language Model through Ollama, and a vector database to retrieve relevant information and generate grounded responses.

## 2. Project Objectives

- Provide quick answers to employee HR and IT questions.
- Retrieve information from internal company documents.
- Reduce repetitive work for HR and IT support teams.
- Support selected tools such as leave calculations and support ticket creation.
- Maintain privacy and security through local model execution and guardrails.

## 3. Technical Scope

- Document ingestion and preprocessing.
- Text chunking and embedding generation.
- Vector storage using ChromaDB.
- Semantic document retrieval.
- Answer generation using LangChain and Ollama.
- Tool calling and human approval for sensitive actions.
- Input validation, PII protection and automated testing.

## 4. Non-Goals (Strict Out-of-Scope)

- No legal or medical counselling.
- No autonomous write access to company systems.
- No access to confidential salary or employee records.
- No speculative answers when reliable information is unavailable.
- No execution of sensitive actions without human approval.

## 5. Technology Stack

- Programming Language: Python 3.12
- Agent Framework: LangChain
- Language Model: Llama 3.2 through Ollama
- Vector Database: ChromaDB
- Embedding Engine: FastEmbed
- Configuration: python-dotenv
- Testing: pytest
- Version Control: Git and GitHub
- Containerization: Docker

## 6. Security and Risk Controls

- Store secrets in environment variables.
- Exclude `.env` and virtual environments from Git.
- Detect possible credentials before committing code.
- Validate user inputs and retrieved documents.
- Require human approval for sensitive actions.
- Restrict answers to available and relevant knowledge sources.

## 7. Service Level Objectives (Initial Targets)

- Target at least 90% accuracy on the golden evaluation dataset.
- Zero intentional credential exposure.
- Target a cold-start deployment time below two minutes.
- Provide source-grounded answers whenever relevant documents are available.

These are project targets to be measured during testing, not yet verified performance results.

## 8. Expected Deliverables

- Working AI Knowledge Base Assistant.
- Internal document retrieval system.
- Tool-calling functionality.
- Guardrails and human approval workflow.
- Automated evaluation tests.
- Secure Git repository.
- Dockerized application and documentation.

## 9. Conclusion

This project aims to develop a secure, reliable and locally deployable AI assistant for internal company knowledge management. It combines modern LLM orchestration, retrieval, tool calling and security practices to demonstrate an industry-oriented AI application.
