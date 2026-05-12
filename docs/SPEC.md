# Specification: Synthetic Feedback Panel

## Overview
The Synthetic Feedback Panel simulates 10 distinct synthetic users (personas) to provide feedback on presentations, demos, products, etc. This specification outlines the operational workflow for running the panel using OpenHands.

## Workflow
1. **Input Preparation**: The user puts the item to be reviewed (e.g., presentation text, product description) and an optional list of questions in the `input/` folder.
2. **System Startup**: The user starts OpenHands and points it to this repository.
3. **Execution Request**: The user asks OpenHands to review the item.
4. **Delegation**: OpenHands uses the Delegate function to call each of the 10 persona skills independently.
5. **Feedback Generation**: Each skill (acting as a sub-agent) reads the input, adopts its persona, and writes a brief markdown feedback file in the `output/` folder.
6. **Summarization**: A final agent (or the main agent) reads the 10 feedback files and writes a short summary in the `output/` folder.

## Folder Structure
- `input/`: Contains files to be reviewed.
- `output/`: Contains generated feedback and summary.
- `.openhands/microagents/`: Contains consolidated OpenHands skill definitions and persona profiles.
- `.agents/skills/`: Contains other skills (e.g., utility skills like summarizer).

## Personas
This panel is designed for testing **AI-native new product ideas** or presentations about them. The personas are based on real-world demographics to avoid functional prejudice and ensure a diverse range of perspectives.

1. **The smart, tech-forward high school student**: Early adopter, values speed and convenience, may lack deep domain knowledge but understands tech trends.
2. **The elite college student**: High expectations, values innovation and prestige, future-oriented.
3. **The normal college student**: Pragmatic, cost-conscious, looking for tools that help with studies or social life.
4. **Young professional (Tech)**: Works at a company like Google. Deeply familiar with tech, expects high quality, values efficiency and automation.
5. **Young professional (Professional Services)**: Works at a big firm. Values reliability, clear value proposition, and professional utility.
6. **Young professional (Finance)**: Works at a big bank. Focuses on security, compliance, ROI, and efficiency.
7. **Mid-level Manager**: Manager or director at a big company. Focuses on team productivity, scalability, and business impact.
8. **Local Business Owner/Manager**: Medium-sized business. Focuses on operations, customer satisfaction, and manageable costs.
9. **Small Business Owner**: Community-focused. Values simplicity, affordability, and direct impact on their business.
10. **Independent Consultant**: Contracts for large companies. Values flexibility, personal productivity, and tools that make them look good to clients.
