from urllib.parse import urlparse
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
    parsed = urlparse(url.lower())
    netloc = parsed.netloc
    path = parsed.path
    
    # Capa 1: Dominio exacto - netloc termina en {token}.es o {token}.com
    for token, entity_id in ENTITY_LOOKUP.items():
        if netloc.endswith(f"{token}.es") or netloc.endswith(f"{token}.com"):
            return {
                "entity": {
                    "entity_detected": True,
                    "entity_id": entity_id,
                    "entity_name": ENTITY_NAMES.get(entity_id)
                }
            }
    
    # Capa 2: Subdominio - netloc empieza por {token}.
    for token, entity_id in ENTITY_LOOKUP.items():
        if netloc.startswith(f"{token}."):
            return {
                "entity": {
                    "entity_detected": True,
                    "entity_id": entity_id,
                    "entity_name": ENTITY_NAMES.get(entity_id)
                }
            }
    
    # Capa 3: Path - path contiene /{token}/
    for token, entity_id in ENTITY_LOOKUP.items():
        if f"/{token}/" in path:
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
