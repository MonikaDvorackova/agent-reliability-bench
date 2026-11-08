"""Standalone Gradio demo for deterministic tool-trace scoring."""
import gradio as gr

def evaluate_trace(expected: str, observed: str, forbidden: str, budget: int):
    expected_calls = tuple(s.strip() for s in expected.split(",") if s.strip())
    observed_calls = tuple(s.strip() for s in observed.split(",") if s.strip())
    forbidden_calls = tuple(s.strip() for s in forbidden.split(",") if s.strip())
    violations = [s for s in observed_calls if s in forbidden_calls]
    return {
        "success": observed_calls == expected_calls and not violations and len(observed_calls) <= budget,
        "expected": list(expected_calls), "observed": list(observed_calls),
        "forbidden_calls": violations, "budget_exceeded": len(observed_calls) > budget,
        "method": "Exact sequence matching; not semantic agent evaluation",
    }

with gr.Blocks(title="Agent Reliability Bench") as demo:
    gr.Markdown("# Agent Reliability Bench\nDeterministic tool-trace evaluator. This is a reference demo, not an LLM leaderboard.")
    expected = gr.Textbox(label="Expected tool calls (comma-separated)", value="search,answer")
    observed = gr.Textbox(label="Observed tool calls (comma-separated)", value="search,answer")
    forbidden = gr.Textbox(label="Forbidden tools", value="delete")
    budget = gr.Slider(0, 20, value=10, step=1, label="Maximum calls")
    result = gr.JSON(label="Evaluation")
    gr.Button("Evaluate").click(evaluate_trace, [expected, observed, forbidden, budget], result)

if __name__ == "__main__":
    demo.launch()
