# Refactor Workflow

This workflow orchestrates code refactoring with user-driven steps and minimal LLM requests.

## Steps
1. Ask user to select code regions or files to refactor.
2. Present refactoring options (e.g., rename, extract method, optimize imports).
3. Confirm changes with the user before applying.
4. Summarize results and next steps.

---

- All user input and confirmations are handled via `vscode_askQuestions`.
- Subagents perform only the specific refactoring actions.
