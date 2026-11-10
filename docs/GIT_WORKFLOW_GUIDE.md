
# Git Workflow and Security Guide

## 1. Branching Strategy

The project uses separate Git branches for each development phase.

- `main` – Stable project version.
- `step-01-project-scaffold` – Initial project setup.
- `step-02-considerations-and-risks` – Architecture and risk planning.
- `step-03-secure-confidential-data` – Environment configuration and data security.
- `step-04-git-industrial-workflow` – Git workflow and automated secret detection.
- `step-05-agent-tools-and-skills` – Agent tools and skills implementation.

Create a new branch for each development phase.

```powershell
git switch -c step-05-agent-tools-and-skills
```

## 2. Conventional Commit Messages

Use clear and consistent commit messages.

Format:

`type(scope): description`

Examples:

- `feat(agent): add document retrieval tool`
- `fix(guardrail): prevent unauthorized actions`
- `docs(readme): update project instructions`
- `test(security): add secret detection tests`

Common commit types:

- `feat` – New functionality.
- `fix` – Bug fixes.
- `docs` – Documentation changes.
- `test` – Testing changes.
- `refactor` – Code improvements without changing functionality.

## 3. Pre-commit Security Checks

The project uses two automated security scanners:

### Gitleaks

Detects accidentally exposed credentials, API keys, passwords, and tokens.

### detect-secrets

Scans files for potential secrets and compares findings against `.secrets.baseline`.

Configuration is stored in `.pre-commit-config.yaml`.

Install Git hooks:

```powershell
pre-commit install
```

Run security checks on all applicable files:

```powershell
pre-commit run --all-files
```

## 4. Secret Management Rules

- Never commit `.env` files.
- Store configuration in environment variables.
- Use `.env.example` to document required settings.
- Never hardcode real API keys or passwords.
- Review every finding before approving it in the secrets baseline.
- Never bypass security hooks to force a commit.

## 5. Simulated Secret Leak Test

The project includes `scripts/simulate_leak.py` to test secret detection.

Generate a temporary fake credential:

```powershell
python scripts/simulate_leak.py generate
```

Stage the temporary file:

```powershell
git add test_leak.py
```

Attempt a commit:

```powershell
git commit -m "test(security): verify secret detection"
```

Gitleaks and detect-secrets should detect the fake credential and block the commit.

Remove the temporary file from staging:

```powershell
git reset HEAD test_leak.py
```

Delete the temporary file:

```powershell
python scripts/simulate_leak.py cleanup
```

## 6. Standard Development Workflow

1. Create or switch to the appropriate feature branch.
2. Make the required code changes.
3. Run tests and security checks.
4. Stage the intended files.
5. Commit using conventional commit messages.
6. Push the branch to GitHub.
7. Create a Pull Request for review.
8. Merge only after the required checks pass.

## 7. Important Security Principle

Security checks must run before every commit. Real credentials must never be stored in the Git repository.

The purpose of this workflow is to maintain code quality, protect confidential information, and support safe collaboration.
