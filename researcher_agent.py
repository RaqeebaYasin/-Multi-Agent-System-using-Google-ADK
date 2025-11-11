Purpose:
This agent gathers detailed information based on user queries.

Code:

from google.adk.agents import LlmAgent

researcher = LlmAgent(
    name="researcher_agent",
    model="gemini-1.5-flash",
    description="Finds and gathers relevant information on a topic.",
    instruction="Search and summarize key facts on the user query.",
)
