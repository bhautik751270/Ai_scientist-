# # agents/planner.py

# import os
# from groq import Groq

# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# def call_groq(prompt: str) -> str:
#     response = client.chat.completions.create(
#         model="llama3-70b-8192",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.7,
#     )
#     return response.choices[0].message.content.strip()

# def plan_research(topic: str) -> list:
#     prompt = f"""
# You are a Lead AI Research Planner. Break down the research topic: '{topic}'
# into 3-5 subtasks covering: literature review, methodology design, simulation planning, and result evaluation.
# Return only numbered subtasks.
# """
#     response = call_groq(prompt)
#     return response.split('\n')



# agents/planner.py

import os
from dotenv import load_dotenv
from groq import Groq

# ✅ Load the environment variables from .env file
load_dotenv()

# ✅ Now it will correctly get the API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_groq(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()

def plan_research(topic: str) -> list:
    prompt = f"""
You are a Lead AI Research Planner. Break down the research topic: '{topic}'
into 3-5 subtasks covering: literature review, methodology design, simulation planning, and result evaluation.
Return only numbered subtasks.
"""
    response = call_groq(prompt)
    return response.split('\n')
