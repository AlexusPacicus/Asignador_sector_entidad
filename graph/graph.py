from langgraph.graph import StateGraph, END
from .state import State
from .nodes import should_enrich, enrich

graph = StateGraph(State)

# nodo real
graph.add_node("enrich", enrich)

# ENTRY decide ruta (gate)
graph.set_conditional_entry_point(
    should_enrich,
    {True: "enrich", False: END}
)

# cuando termina enrich, termina el flujo
graph.add_edge("enrich", END)

app = graph.compile()
