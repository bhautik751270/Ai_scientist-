# agents/evaluator.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_groq(prompt: str):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


def evaluate_results(topic: str, simulated_results: str, related_work_summary: str) -> str:
    prompt = f"""
You are an AI research analyst.

Given the research topic: "{topic}"

Here are the simulation results:
{simulated_results}

Here is the summary of related research:
{related_work_summary}

Evaluate how well the results align with prior work. Suggest:
- Improvements
- Pitfalls or assumptions to revisit
- Next steps to extend the study

Structure it clearly with headings.
"""
    return call_groq(prompt)
