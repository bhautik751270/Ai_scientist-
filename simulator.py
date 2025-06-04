# agents/simulator.py

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


def design_simulation(topic: str, subtasks: list[str]) -> str:
    formatted_subtasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(subtasks)])
    
    prompt = f"""
You are a scientific simulation expert.

Research Topic: "{topic}"

Subtasks:
{formatted_subtasks}

Based on the above, design a detailed simulation or experiment plan including:
- Simulation objectives
- Tools/frameworks to be used (Python libs, ML tools, etc.)
- Dataset suggestions or how to generate synthetic data
- Evaluation criteria
- Workflow steps

Provide a clear, bullet-point breakdown of the plan.
"""
    return call_groq(prompt)
