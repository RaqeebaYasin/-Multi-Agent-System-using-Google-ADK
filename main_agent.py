Purpose:
This is your controller — the "boss" that coordinates the other agents.

Code:

from researcher_agent import researcher
from summarizer_agent import summarizer

def main():
    print("🤖 Multi-Agent System Started!")
    query = input("Enter your question: ")

    # Sequential agent coordination
    research_output = researcher.chat(query).text
    summary_output = summarizer.chat(research_output).text

    print("\n✅ Final Answer:\n", summary_output)

if __name__ == "__main__":
    main()
