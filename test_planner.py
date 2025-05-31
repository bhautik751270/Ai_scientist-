# test.py

import os
import sys
from dotenv import load_dotenv

# 🔓 Load environment variables from .env file
load_dotenv()

# 🔧 Add current directory to system path (to import agents)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.planner import plan_research

# 🎯 Define your research topic
topic = "Improving solar panel efficiency using nanostructured materials"

# 🧠 Get subtasks from Groq LLM
subtasks = plan_research(topic)

# 📤 Print the generated subtasks
print("Generated Subtasks:")
for task in subtasks:
    print("🔹", task)
