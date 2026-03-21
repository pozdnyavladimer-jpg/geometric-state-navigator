from .state_cell import StateCell

def run_canonical_pipeline(input_text: str):

    # 1. fake graph result (поки без GitCube інтеграції)
    risk_info = {
        "risk": 0.7,
        "cycles": 1
    }

    # 2. encode to state (спрощено)
    state = {
        "red_mass": 0.3,
        "orange_flow": 0.1,
        "yellow_struct": 0.2,
        "green_balance": 0.1,
        "blue_law": 0.2,
        "violet_future": 0.1
    }

    cell = StateCell(
        cell_id="demo",
        state_vector=state,
        graph_context=risk_info,
        active_agents=["planner", "stabilizer"]
    )

    # 3. fake decision
    decision = {
        "coalition": "planner+stabilizer",
        "status": "COMMIT"
    }

    cell.set_decision(decision)

    cell.update_metrics({
        "shadow": 0.05,
        "coherence": 0.9,
        "target_fit": 0.6,
        "vitality": 0.4
    })

    cell.add_trace({
        "step": 0,
        "event": "commit"
    })

    return cell


if __name__ == "__main__":
    result = run_canonical_pipeline("unstable system")

    print("Decision:", result.last_decision)
    print("Metrics:", result.metrics)
