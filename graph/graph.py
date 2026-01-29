from langgraph.graph import StateGraph, END
from .state import State
from .nodes import validate_input, detector_mecanico

graph = StateGraph(State)

graph.add_node("validate_input", validate_input)
graph.add_node("detector_mecanico", detector_mecanico)

graph.set_entry_point("validate_input")

graph.add_conditional_edges(
    "validate_input",
    lambda s: "__end__" if s.get("abort_reason") else "detector_mecanico",
    {
        "detector_mecanico": "detector_mecanico",
        "__end__": END
    }
)

graph.add_edge("detector_mecanico", END)

app = graph.compile()
