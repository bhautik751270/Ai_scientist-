# test_evaluator.py

from agents.evaluator import evaluate_results

topic = "Improving solar panel efficiency using nanostructured materials"

simulated_results = """
Our simulation of nano-pyramidal surface geometry showed a 12.4% improvement in photon absorption compared to flat surfaces.
Key tools used: COMSOL, Python (scikit-nano), custom optical simulations.
"""

related_work_summary = """
Prior studies on nanostructured solar cells (e.g., Zhao et al., 2022) showed 8–10% improvement using nanowires and nanopillars.
Our approach uses pyramidal nanostructures, which have not been widely studied.
"""

report = evaluate_results(topic, simulated_results, related_work_summary)

print("\n📊 Evaluation Report:\n")
print(report)
