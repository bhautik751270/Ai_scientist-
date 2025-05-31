# test_simulator.py

from agents.simulator import design_simulation

topic = "Improving solar panel efficiency using nanostructured materials"
subtasks = [
    "Literature review of existing nanostructured solar cells",
    "Identify efficiency bottlenecks in current designs",
    "Propose novel nanomaterial geometry",
    "Simulate photon absorption with new geometry",
    "Compare performance metrics with baseline"
]

plan = design_simulation(topic, subtasks)

print("\n🧪 Simulation Plan:\n")
print(plan)
