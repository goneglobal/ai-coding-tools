"""
Orchestrator script for workflow skill.
- Uses vscode_askQuestions to keep sessions interactive and minimize LLM requests.
- Delegates atomic actions to subagents.
- Maintains session state for continuity.
"""

def ask_user(questions):
    """Call vscode_askQuestions with a list of questions."""
    # Placeholder: Integrate with actual askQuestions tool in your environment
    print("ASK USER:", questions)
    return input("User response: ")


def run_workflow(workflow_name):
    if workflow_name == "code_review":
        # Example: ask user for files and focus areas
        files = ask_user([{"header": "Select files", "question": "Which files to review?"}])
        focus = ask_user([{"header": "Focus area", "question": "What should the review focus on? (security, performance, style)"}])
        # Delegate to subagent for actual review
        print(f"Reviewing {files} for {focus}")
    elif workflow_name == "refactor":
        region = ask_user([{"header": "Code region", "question": "Which code region to refactor?"}])
        refactor_type = ask_user([{"header": "Refactor type", "question": "What kind of refactor? (rename, extract, optimize imports)"}])
        print(f"Refactoring {region} with {refactor_type}")
    elif workflow_name == "test_generation":
        target = ask_user([{"header": "Test target", "question": "Which functions or modules to generate tests for?"}])
        test_type = ask_user([{"header": "Test type", "question": "What type of test? (unit, integration, property-based)"}])
        print(f"Generating {test_type} tests for {target}")
    else:
        print("Unknown workflow.")

# Example usage:
# run_workflow("code_review")
