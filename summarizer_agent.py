Purpose:
This agent takes the researcher’s findings and summarizes them into short, readable text.

Code:

from google.adk.agents import LlmAgent

summarizer = LlmAgent(
    name="summarizer_agent",
    model="gemini-1.5-flash",
    description="Summarizes the gathered information.",
    instruction="Summarize the content in short, clear, and precise form.",
)
