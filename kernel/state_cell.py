from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

@dataclass
class StateCell:
    cell_id: str
    state_vector: Dict[str, float]

    graph_context: Dict[str, Any] = field(default_factory=dict)
    memory_links: List[Dict[str, Any]] = field(default_factory=list)
    active_agents: List[str] = field(default_factory=list)

    last_decision: Optional[Dict[str, Any]] = None
    metrics: Dict[str, float] = field(default_factory=dict)
    trace: List[Dict[str, Any]] = field(default_factory=list)

    def update_metrics(self, metrics: Dict[str, float]) -> None:
        self.metrics = metrics

    def add_trace(self, event: Dict[str, Any]) -> None:
        self.trace.append(event)

    def attach_memory(self, atom: Dict[str, Any]) -> None:
        self.memory_links.append(atom)

    def set_decision(self, decision: Dict[str, Any]) -> None:
        self.last_decision = decision
