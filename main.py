# # main.py

# from agents.planner import plan_research
# from agents.researcher import summarize_relevant_papers
# from agents.simulator import design_simulation
# from agents.evaluator import evaluate_results

# topic = "Improving solar panel efficiency using nanostructured materials"

# print("📌 STEP 1: Planning...")
# subtasks = plan_research(topic)
# for i, task in enumerate(subtasks): print(f"  {i+1}. {task}")

# print("\n📚 STEP 2: Researching papers...")
# literature_summary = summarize_relevant_papers(topic)
# print(literature_summary)

# print("\n🧪 STEP 3: Simulating experiment...")
# simulation_plan = design_simulation(topic, subtasks)
# print(simulation_plan)

# print("\n📊 STEP 4: Evaluating...")
# evaluation = evaluate_results(topic, simulated_results=simulation_plan, related_work_summary=literature_summary)
# print(evaluation)


# main.py

import sys
from agents.planner import plan_research
from agents.researcher import summarize_relevant_papers
from agents.simulator import design_simulation
from agents.evaluator import evaluate_results

def run_research_pipeline(topic: str):
    print("📌 STEP 1: Planning...")
    subtasks = plan_research(topic)
    for i, task in enumerate(subtasks): print(f"  {i+1}. {task}")

    print("\n📚 STEP 2: Researching papers...")
    literature_summary = summarize_relevant_papers(topic)
    print(literature_summary)

    print("\n🧪 STEP 3: Simulating experiment...")
    simulation_plan = design_simulation(topic, subtasks)
    print(simulation_plan)

    print("\n📊 STEP 4: Evaluating...")
    evaluation = evaluate_results(
        topic,
        simulated_results=simulation_plan,
        related_work_summary=literature_summary
    )
    print(evaluation)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py 'Your Research Topic'")
        sys.exit(1)

    topic = sys.argv[1]
    run_research_pipeline(topic)
