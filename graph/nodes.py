import uuid
from datetime import datetime
from .entities import ENTITY_LOOKUP, ENTITY_NAMES


def ingest(state):
    state["errors"] = []
    state["meta"] = {
        "run_id": str(uuid.uuid4()),
        "ts_start": datetime.utcnow().isoformat()
    }
    state["entity_id"] = None
    state["result"] = None
    return state

def validate(state):
    if not isinstance(state.get("url"), str) or not state["url"].strip():
        state["errors"].append({
            "type": "INVALID_INPUT",
            "reason": "url missing or invalid"
        })
    return state

def route(state):
    return state

def enrich(state):
    url = state["url"].lower()
    for token, entity_id in ENTITY_LOOKUP.items():
        if token in url:
            state["entity_id"] = entity_id
            break
    return state


def finalize(state):
    if state["errors"]:
        return state

    if state["entity_id"]:
        state["result"] = {
            "entity_id": state["entity_id"],
            "entity_name": ENTITY_NAMES[state["entity_id"]],
            "entity_detected": True
        }
    else:
        state["result"] = {
            "entity_id": None,
            "entity_name": None,
            "entity_detected": False
        }

    state["meta"]["ts_end"] = datetime.utcnow().isoformat()
    return state
