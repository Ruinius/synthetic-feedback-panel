# Agents Documentation

This file outlines the architectural patterns, module boundaries, and documentation standards for the `synthetic-feedback-panel` project.

## Project Overview
This is a personal project which creates 10 synthetic users that can give feedback on presentations, demos, products, etc.
The goal is to run this on OpenHands or Hermes Agent to leverage sub-agents and avoid context pollution.

## Guidelines
- **Pre-Coding Check:** ALWAYS read `AGENTS.md` before starting to write any new code or implementing new features.
- **Tooling:** Always use `uv` for Python-related tasks. Never use `pip` or `venv` directly.
- **Execution:** Run Python scripts and tools exclusively using `uv run`.
- **Dependencies:** Use `uv add <package>` to install new dependencies.
- **Tmp Code:** Temporary logs and scripts saved into `tmp/` directory.

## Module Boundaries
*(To be defined as the project grows)*

## Documentation Standards
- Keep documentation up to date.
- Update this file when major architectural changes occur.
