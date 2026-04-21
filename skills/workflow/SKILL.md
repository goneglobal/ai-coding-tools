# Workflow Skill

## Purpose
This skill provides a framework for orchestrating interactive, multi-step workflows using the `vscode_askQuestions` tool to keep sessions efficient and user-driven.

## Key Principles
- **Interactive Sessions:** Always use `vscode_askQuestions` to clarify, branch, or confirm steps, minimizing unnecessary LLM requests.
- **Thin Orchestration Agents:** Subagents should only handle atomic tasks, keeping orchestration logic in the main workflow agent.
- **Predefined Workflows:** Offer users a set of selectable, well-documented workflows for common tasks (e.g., code review, refactor, test generation).
- **Session Context:** Maintain session state and user choices to ensure continuity and reduce repeated questions.

## Usage Pattern
1. Present available workflows to the user via `vscode_askQuestions`.
2. For each step, use `vscode_askQuestions` to confirm or gather required input.
3. Delegate atomic actions to subagents, keeping orchestration logic minimal in subagents.
4. Store session state (e.g., in session memory or context objects) to track progress.
5. Minimize premium LLM requests by batching questions and only acting when all required info is available.

## Example Structure
```
skills/workflow/
  SKILL.md
  workflows/
    code_review.md
    refactor.md
    test_generation.md
  scripts/
    orchestrator.py
```

## Best Practices
- Never ask clarifying questions in plain text; always use `vscode_askQuestions`.
- Keep subagents focused on single, well-defined tasks.
- Use session memory to persist workflow progress and user choices.
- Prefer predefined workflows for repeatable tasks; allow custom workflows as needed.

## References
- See `instructions/copilot-instructions.md` for communication guidelines.
- See `README.md` for high-level architecture and best practices.
