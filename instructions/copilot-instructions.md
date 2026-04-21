---
description: Personal coding assistant instructions for GitHub Copilot. These guidelines ensure effective communication and optimal use of the tool.
applyTo: "**"
---

## Communication
- **MANDATORY: Use `vscode_askQuestions` BEFORE acting** whenever a request is ambiguous, missing key details, or has multiple valid interpretations. This is non-negotiable — do NOT make assumptions or start a new prompt asking the user to reply. Batch ALL clarifying questions into a single `vscode_askQuestions` call.
- **Never ask clarifying questions in plain text responses.** If clarification is needed, use the tool. If you find yourself typing "Could you clarify..." or "What did you mean by..." — stop and use `vscode_askQuestions` instead.
- Minimize premium request usage at every opportunity. Prefer one well-structured question over multiple follow-ups.
- Keep responses **concise**. Prefer bullet points and short paragraphs over lengthy prose.