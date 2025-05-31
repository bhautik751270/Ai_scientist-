# test_researcher.py

from agents.researcher import summarize_relevant_papers

topic = "Improving solar panel efficiency using nanostructured materials"
summary = summarize_relevant_papers(topic)

print("\n📘 Summary of Research Methods:\n")
print(summary)
