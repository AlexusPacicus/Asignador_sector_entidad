"""
CONTRATO DE SALIDA v3

CASO ÉXITO (sin abort):
- abort_reason is None
- entity presente y cumple invariantes:
  - entity_detected siempre presente (bool)
  - si True  -> entity_id y entity_name no-None
  - si False -> entity_id y entity_name None

CASO ABORT:
- abort_reason poblado 
- entity == None
"""
from typing import TypedDict, Optional


# total=False: campos opcionales durante el grafo; el contrato aplica al estado final.
class State(TypedDict, total=False):
    url: Optional[str]            # Entrada raw (entrypoint)
    input: Optional[dict]         # Entrada validada (ej: {"url": "..."})
    entity: Optional[dict]        # Resultado de detección (entity_detected, entity_id, entity_name)
    abort_reason: Optional[str]   # Razón de abort si aplica

"""
CONTRATO DE SALIDA v3

Semántica:
- La entidad representa una REFERENCIA NOMINAL detectada en la URL.
- No implica legitimidad, ownership ni autenticidad del dominio.
- No existe estado de ambigüedad: el detector siempre devuelve
  una única entidad o ninguna.

CASO ÉXITO (sin abort):
- abort_reason is None
- entity presente y cumple invariantes:
  - entity_detected siempre presente (bool)
  - si True  -> entity_id y entity_name no-None
  - si False -> entity_id y entity_name None

CASO ABORT:
- abort_reason poblado
- entity == None
"""
