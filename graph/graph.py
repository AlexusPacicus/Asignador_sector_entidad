from langgraph.graph import StateGraph, END
from .state import State
from .nodes import validate_input, detector_mecanico, finalize

graph = StateGraph(State)

# nodos
graph.add_node("validate_input", validate_input)
graph.add_node("detector_mecanico", detector_mecanico)
graph.add_node("finalize", finalize)

# entry
graph.set_entry_point("validate_input")

# gate duro: si abort → END
graph.add_conditional_edges(
    "validate_input",
    lambda s: "__end__" if s.get("abort_reason") or s.get("violations") else "detector_mecanico",
    {
        "detector_mecanico": "detector_mecanico",
        "__end__": END
    }
)

# flujo lineal
graph.add_edge("detector_mecanico", "finalize")
graph.add_edge("finalize", END)

app = graph.compile()
