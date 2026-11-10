"""Centralized project configuration loaded from environment variables."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Find the root directory of the project
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Load settings from the .env file
load_dotenv(dotenv_path=PROJECT_ROOT / ".env")

# LLM configuration
LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama").strip().lower()
LLM_MODEL: str = os.getenv("LLM_MODEL", "llama3.2:latest").strip()

OLLAMA_BASE_URL: str = os.getenv(
    "OLLAMA_BASE_URL", "http://localhost:11434"
).strip()

# Project directories
DOCS_DIR = PROJECT_ROOT / os.getenv("DOCS_DIR", "data/docs").strip()
CHROMA_DIR = PROJECT_ROOT / os.getenv("CHROMA_DIR", "chroma_db").strip()