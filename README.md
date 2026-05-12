# Synthetic Feedback Panel

A personal project that creates 10 synthetic users capable of providing feedback on presentations, demos, products, and more.

## Purpose
The goal of this project is to simulate a panel of diverse users to get constructive feedback on various artifacts. This helps in iterating on designs, presentations, and products before showing them to real users.

## Agentic Workflow
This project is designed with agentic workflows in mind. I am targeting execution on **OpenHands** or **Hermes Agent**. A key requirement is the ability to spawn sub-agents to avoid context pollution, ensuring each synthetic user operates with its own distinct persona and context.

## Setup
This project uses `uv` for dependency management.

```powershell
uv sync
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
