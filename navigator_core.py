import json
import urllib.request
from typing import Dict, Any

STATE_URL = "https://raw.githubusercontent.com/pozdnyavladimer-jpg/gitcube-os/main/v_resonance.json"

def load_state() -> Dict[str, Any]:
    with urllib.request.urlopen(STATE_URL) as response:
        return json.loads(response.read().decode())

def extract_vector(state: Dict[str, Any]) -> Dict[str, float]:
    flower = state.get("flower", {})
    return {
        "pressure": float(flower.get("pressure", 0)),
        "flow": float(flower.get("flow", 0)),
        "structure": float(flower.get("structure", 0)),
        "balance": float(flower.get("balance", 0)),
        "law": float(flower.get("law", 0)),
        "future": float(flower.get("future", 0)),
    }

def analyze(vector: Dict[str, float]):
    issues = []

    if vector["flow"] < 0.2:
        issues.append("LOW_FLOW")

    if vector["law"] < 0.2:
        issues.append("LOW_LAW")

    if vector["pressure"] > 0.5:
        issues.append("HIGH_PRESSURE")

    if vector["balance"] > 0.75:
        issues.append("OVER_STABLE")

    return issues

def decide_correction(issues):
    if "LOW_FLOW" in issues:
        return "INCREASE_FLOW"
    if "LOW_LAW" in issues:
        return "INCREASE_LAW"
    if "HIGH_PRESSURE" in issues:
        return "REDUCE_PRESSURE"
    if "OVER_STABLE" in issues:
        return "DESTABILIZE"
    return "STABLE"

def build_feedback(action: str, issues, vector: Dict[str, float]) -> Dict[str, Any]:
    return {
        "source": "NAVIGATOR",
        "action": action,
        "issues": issues,
        "vector": vector,
    }

def main():
    try:
        state = load_state()
    except Exception as e:
        print("ERROR loading state:", e)
        return

    vector = extract_vector(state)
    issues = analyze(vector)
    action = decide_correction(issues)

    feedback = build_feedback(action, issues, vector)

    with open("navigator_feedback.json", "w", encoding="utf-8") as f:
        json.dump(feedback, f, ensure_ascii=False, indent=2)

    print("=== NAVIGATOR ===")
    print("vector:", vector)
    print("issues:", issues)
    print("action:", action)
    print("saved: navigator_feedback.json")

if __name__ == "__main__":
    main()
