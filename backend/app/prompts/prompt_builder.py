from app.prompts.system_prompt import SYSTEM_PROMPT


def build_prompt(user_query: str) -> str:
    """
    Builds the final prompt sent to the LLM.
    """

    return f"""
{SYSTEM_PROMPT}

User Query:
{user_query}
"""