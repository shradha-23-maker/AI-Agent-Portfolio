# Contribution Log

## Project: AI Agent Portfolio

This contribution log records my work on the AI Agent Portfolio project using the project's Git history.

| Date | Commit ID | Contribution | Outcome |
|---|---|---|---|
| 08-08-2026 | `ba86c4f` | Created the initial AI Agent project structure and files. | Established the basic foundation of the AI Agent Portfolio. |
| 08-08-2026 | `64a01ac` | Added the learning reflection to the portfolio. | Documented my learning and experience during the project. |
| 10-08-2026 | `f83384b` | Added my name and PRN information to the README. | Added personal identification information required for the portfolio. |
| 10-08-2026 | `4e1ffa0` | Corrected a spelling/typing error in the name section of the README. | Improved the accuracy of the project documentation. |
| 10-08-2026 | `ad3e70c` | Removed unnecessary hash symbols from personal information. | Improved the formatting and presentation of the README. |
| 14-08-2026 | `4830ca2` | Changed the AI Agent to accept questions interactively from the user. | The agent can now accept user questions and generate responses using Llama 3.2 through Ollama. |

## Technical Contributions

During this project, I contributed to the following areas:

### 1. Project Setup
- Created the basic project structure.
- Set up the Python development environment.
- Used a Python virtual environment for project dependencies.

### 2. AI Agent Development
- Developed the Python AI Agent.
- Connected the agent with Ollama.
- Used the Llama 3.2 local AI model.
- Tested the agent by asking questions and receiving AI-generated responses.
- Improved the agent to accept user input interactively.

### 3. Documentation
- Created and updated the README file.
- Added personal project information.
- Added a learning reflection.
- Corrected documentation errors and formatting.

### 4. Version Control
- Used Git to track project changes.
- Created commits for different project contributions.
- Used GitHub to store and manage the project.
- Pushed the completed changes to the remote repository.

## Learning Outcomes

Through this project, I learned:

- How to create a Python project structure.
- How to use a Python virtual environment.
- How to install dependencies using `requirements.txt`.
- How to use Ollama for running a local AI model.
- How to work with the Llama 3.2 model.
- How to connect Python code with an AI model.
- How to create an interactive AI Agent.
- How to test and troubleshoot a Python application.
- How to use Git and GitHub for version control.
- How to document project development and contributions.

## Evidence

The Git history provides evidence of the development process and shows the changes made to the project over time.

The final commit:

`4830ca2 - Make AI agent interactive`

represents the improvement that allows the AI Agent to accept questions from the user and return responses from the Llama 3.2 model.

## Summary

The project progressed from an initial AI Agent structure to a working interactive AI Agent. Git and GitHub were used throughout the development process to record and manage project changes.Ctrl + End


## AI Tools Used

1. **ChatGPT**
   - Used for understanding AI Agent concepts.
   - Used for step-by-step guidance while setting up Python, virtual environment, and Ollama.
   - Used for troubleshooting errors during project development.
   - Used for understanding Git commands and project documentation.

2. **Ollama**
   - Used to run the AI model locally.
   - Used with the Llama 3.2 model to generate responses from the AI Agent.

3. **Llama 3.2**
   - Used as the local language model for answering user questions through Ollama.

## AI-Generated Parts

- ChatGPT provided explanations and guidance about AI Agents and their components.
- ChatGPT assisted with understanding Python and Ollama integration.
- ChatGPT provided guidance for troubleshooting setup and execution errors.
- AI assistance was used to improve project documentation and understand Git workflow.
- Llama 3.2 generates the responses displayed by the interactive agent.

## My Own Contribution

- Created and maintained the GitHub repository.
- Created the project folder structure and required files.
- Set up the Python virtual environment.
- Installed the required Python packages.
- Installed and configured Ollama and Llama 3.2.
- Modified `src/agent.py` to make the AI Agent interactive.
- Tested the agent using different questions.
- Created and maintained the README, ADR, Learning Reflection, and Contribution Log.
- Used Git to track project changes and maintain commit history.

## Issues/Risks and Fixes

### 1. Python Environment Issue
**Issue:** Python and the virtual environment were unavailable after the system reset.

**Fix:** Python 3.14.7 was installed again and a new virtual environment was created.

### 2. PowerShell Execution Policy
**Issue:** PowerShell prevented activation of the virtual environment.

**Fix:** The execution policy was temporarily bypassed for the current terminal session.

### 3. Ollama Not Recognized
**Issue:** The `ollama` command was initially not recognized after the system reset.

**Fix:** Ollama was installed again and verified using `ollama --version`.

### 4. Agent Testing
**Issue:** Questions were initially typed directly into PowerShell instead of into the running agent.

**Fix:** The agent was run using `python src/agent.py`, and questions were entered after the `You:` prompt.

### 5. Git Installation
**Issue:** Git was not recognized after the system reset.

**Fix:** Git was installed again and the existing repository was verified using `git status`.