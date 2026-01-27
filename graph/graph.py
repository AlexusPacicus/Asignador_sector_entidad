from langgraph.graph import StateGraph, END
from .state import State
from .nodes import ingest, validate, route, enrich, finalize

graph = StateGraph(State)

# nodos
graph.add_node("ingest", ingest)
graph.add_node("validate", validate)
graph.add_node("route", route)
graph.add_node("enrich", enrich)
graph.add_node("finalize", finalize)

# entry
graph.set_entry_point("ingest")

# flujo
graph.add_edge("ingest", "validate")

# gate duro: si hay errores → END
graph.add_conditional_edges(
    "validate",
    lambda s: "route" if not s["errors"] else "__end__",
    {
        "route": "route",
        "__end__": END
    }
)


# routing
graph.add_conditional_edges(
    "route",
    lambda s: "enrich" if s["entity_id"] is None else "finalize",
    {"enrich": "enrich", "finalize": "finalize"}
)

# cierre
graph.add_edge("enrich", "finalize")
graph.add_edge("finalize", END)

app = graph.compile()
