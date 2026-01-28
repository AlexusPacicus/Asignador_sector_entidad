from .entities import ENTITY_LOOKUP, ENTITY_NAMES


def validate_input(state):
    """Valida input. Retorna input y/o abort_reason."""
    url = state.get("url")
    
    if not isinstance(url, str) or not url.strip():
        return {
            "input": None,
            "abort_reason": "url missing or invalid"
        }
    
    return {"input": {"url": url}}


def detector_mecanico(state):
    """Detecta entidad. Retorna solo entity."""
    input_data = state.get("input")
    if input_data is None:
        return {}
    
    url = input_data.get("url", "")
    url_lower = url.lower()
    
    for token, entity_id in ENTITY_LOOKUP.items():
        if token in url_lower:
            return {
                "entity": {
                    "entity_detected": True,
                    "entity_id": entity_id,
                    "entity_name": ENTITY_NAMES.get(entity_id)
                }
            }
    
    return {
        "entity": {
            "entity_detected": False,
            "entity_id": None,
            "entity_name": None
        }
    }


def finalize(state):
    """Valida contrato. Retorna violations si falla."""
    if state.get("abort_reason") or state.get("violations"):
        return {}
    
    entity = state.get("entity")
    if entity is None:
        return {}
    
    violations = []
    
    if "entity_detected" not in entity:
        violations.append("entity_detected ausente")
    else:
        detected = entity.get("entity_detected")
        eid = entity.get("entity_id")
        ename = entity.get("entity_name")
        
        if detected:
            if eid is None:
                violations.append("entity_id es None con detected=True")
            if ename is None:
                violations.append("entity_name es None con detected=True")
        else:
            if eid is not None:
                violations.append("entity_id no es None con detected=False")
            if ename is not None:
                violations.append("entity_name no es None con detected=False")
    
    if violations:
        return {"violations": violations}
    
    return {}
