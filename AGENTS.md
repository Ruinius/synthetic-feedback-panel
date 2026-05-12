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

## Project Structure
- `docs/`: Contains project documentation.
    - `ARCHITECTURE.md`: Describes the system architecture and multi-agent workflow.
    - `PLAN.md`: Outlines the implementation plan and project phases.
    - `SPEC.md`: Specifies the operational workflow and personas.
- `personas/`: Empty directory (personas are now consolidated into `.openhands/microagents/`).
- `input/`: Directory for user items and questions to be reviewed.
- `output/`: Directory for generated feedback and summaries.
- `.openhands/microagents/`: Contains consolidated OpenHands skill definitions and persona profiles (microagents).
    - `[persona_name].md`: Individual skills for each of the 10 personas, containing both instructions and persona definition.
- `.agents/skills/`: Contains other skills (e.g., utility skills like summarizer).
    - `summarizer.md`: Skill to summarize feedback.
- `AGENTS.md`: This file, outlining guidelines and project structure.
- `README.md`: General project overview and setup instructions.
- `pyproject.toml`: Python project configuration (managed by `uv`).

## Module Boundaries
*(To be defined as the project grows)*

## Documentation Standards
- Keep documentation up to date.
- Update this file when major architectural changes occur.
