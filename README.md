# ai-coding-tools

# AI Coding Tools

Personal AI Coding Tools to Aid Development

## Table of Contents

- [ai-coding-tools](#ai-coding-tools)
- [AI Coding Tools](#ai-coding-tools-1)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Models \& LLMs](#models--llms)
  - [Context \& Tokens](#context--tokens)
  - [Chat, Generate, Requests](#chat-generate-requests)
  - [IDEs: VSCode \& CLI](#ides-vscode--cli)
  - [Claude \& Copilot](#claude--copilot)
  - [Agents, Subagents, Skills, MCP](#agents-subagents-skills-mcp)
  - [Instructions, Todos, Sessions](#instructions-todos-sessions)
  - [Communication](#communication)
  - [Building a Skill](#building-a-skill)
  - [Best Practices](#best-practices)
  - [Linking Agents into CoPilot](#linking-agents-into-copilot)

---

## Introduction

This repository contains tools, scripts, and knowledge for AI-powered coding workflows. It covers working with large language models (LLMs), context management, agent architectures, and practical development in modern IDEs.

## Models & LLMs

- **LLMs (Large Language Models):** Foundation models like GPT-4, Claude, and others. Used for code generation, chat, and automation.
- **Model Selection:** Choose models based on task (e.g., code generation, summarization, chat).
- **Model Providers:** OpenAI, Anthropic (Claude), Microsoft (Copilot), etc.

## Context & Tokens

- **Context:** The information (code, docs, chat history) provided to the model for each request.
- **Tokens:** LLMs process text in tokens (words/parts of words). Token limits affect how much context you can send.
- **Best Practices:** Keep context relevant and concise. Use summaries or references for large files.

## Chat, Generate, Requests

- **Chat:** Interactive conversations with LLMs (e.g., Copilot Chat, Claude chat).
- **Generate:** One-off code or text generation requests.
- **Requests & Tokens:** Each request consumes tokens (input + output). Monitor usage to avoid hitting limits.

## IDEs: VSCode & CLI

- **VSCode:** Rich integration with AI tools (Copilot, chat, inline suggestions, skills).
- **CLI:** Command-line tools for automation, scripting, and batch operations.
- **Best Practice:** Use VSCode for interactive work, CLI for automation.

## Claude & Copilot

- **Claude:** Anthropic's LLM, strong at reasoning and summarization.
- **Copilot:** GitHub/Microsoft's AI coding assistant, deeply integrated with VSCode.
- **Usage:** Both can be used for code suggestions, chat, and automation.

## Agents, Subagents, Skills, MCP

- **Agents:** Autonomous or semi-autonomous processes that perform tasks (e.g., code generation, refactoring).
- **Subagents:** Specialized agents spawned by a main agent for subtasks.
- **Skills:** Modular, reusable knowledge or workflows (e.g., system-knowledge/SKILL.md).
- **MCP (Model Context Protocol):** Protocol for managing context, instructions, and agent communication.

## Instructions, Todos, Sessions

- **Instructions:** Custom prompts or rules for agents/skills (e.g., .instructions.md).
- **Todos:** Track tasks either via built-in systems or custom todo.md files.
- **Sessions:** Manage state and context across multiple interactions.


## Communication

**You MUST use `vscode/askQuestions` (or an equivalent ask-user tool) for communicating with the user whenever possible.**

- The number one priority is reducing premium requests and token usage.
- Always prompt the user for clarification or choices using askQuestions before making LLM requests that consume tokens.
- This approach saves tokens, reduces costs, and improves efficiency.

## Building a Skill

To build a new skill (e.g., `system-knowledge`):

1. **Create a folder:** `system-knowledge/`
2. **Add a `SKILL.md`:** Document the skill's purpose, usage, and best practices.
3. **References:** Link to relevant docs, scripts, or code.
4. **Scripts/Agents:** Add reusable scripts or agent definitions.
5. **Integration:** Reference the skill in your agent or workflow configuration.

**Example Structure:**

```
system-knowledge/
	SKILL.md
	references.md
	scripts/
		helper.py
	agents/
		custom_agent.py
```

## Best Practices

- **Using Skills vs MCP:** Prefer modular skills for reusable logic; use MCP for protocol-level context management.
- **Self-Spawn vs Subagents:** Self-spawned agents can handle recursive or parallel tasks; subagents are for isolated subtasks.
- **plan.md vs Plan Mode:** Use `plan.md` for persistent, editable plans; plan mode for ephemeral planning.
- **todo.md vs Built-in Todos:** Use `todo.md` for custom workflows or when you need more control than built-in systems.

---

For more examples and advanced usage, see the `system-knowledge` folder and other skill directories in this repo.

## Linking Agents into CoPilot
Each Agent must be individually sym linked (linked by file)
```
$ ln -s /Users/adamadair/coding/external/ai-coding-tools/agents/workflow/workflow.agent.md /Users/adamadair/.copilot/agents/workflow.agent.md
```

Each Skill must be individually sym linked (linked by directory)
```
ln -s /Users/adamadair/coding/external/ai-coding-tools/skills/skill-creator /Users/adamadair/.copilot/skills/skill-creator
```

Adding in a Global copilot-instructions.md file
```
$ ln -s /Users/adamadair/coding/external/ai-coding-tools/copilot-instructions.md /Users/adamadair/.copilot/copilot-instructions.md
``

## Check VSCode CoPilot Settings via - (Mac) - 'Command - Shift - P'`
```
@feature:chat instructions
```
