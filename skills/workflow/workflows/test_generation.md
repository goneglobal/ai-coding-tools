# Test Generation Workflow

This workflow helps users generate tests interactively, using `vscode_askQuestions` to gather requirements and confirm actions.

## Steps
1. Ask user to select functions or modules for test generation.
2. Present test types (e.g., unit, integration, property-based) as options.
3. Confirm test scaffolding and structure with the user.
4. Generate tests and present results for approval.

---

- All clarifications and choices are handled via `vscode_askQuestions`.
- Subagents are used only for generating specific test code.
