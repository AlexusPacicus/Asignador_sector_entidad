from graph.state import State

def should_enrich(state: State) -> bool:
    return state["is_spanish"] and state["entity_id"] is None

def enrich(state):
    if "bbva" in state["url"]:
        state["entity_id"] = "bbva"
    return state
