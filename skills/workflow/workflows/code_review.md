# Code Review Workflow

This workflow guides the user through an interactive code review process using `vscode_askQuestions` for all clarifications and decisions.

## Steps
1. Ask user to select files or modules for review.
2. Present review focus areas (e.g., security, performance, style) as selectable options.
3. For each area, ask if the user wants automated suggestions or manual review.
4. Summarize findings and next steps, confirming with the user before proceeding.

---

- All clarifications and choices are handled via `vscode_askQuestions`.
- Subagents are used only for atomic review tasks (e.g., linting, static analysis).
