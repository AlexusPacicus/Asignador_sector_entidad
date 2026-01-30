"""
Tests de contrato v3
====================
Validan SOLO el contrato de salida.
Deben pasar ANTES y DESPUÉS del refactor.
"""
import pytest
from graph.graph import app


def validate_entity_invariants(entity):
    """Valida los invariantes del contrato de salida."""
    assert "entity_detected" in entity, "entity_detected siempre presente"
    assert isinstance(entity["entity_detected"], bool)
    
    if entity["entity_detected"]:
        assert entity["entity_id"] is not None, "entity_id ≠ None cuando detected"
        assert entity["entity_name"] is not None, "entity_name ≠ None cuando detected"
    else:
        assert entity["entity_id"] is None, "entity_id == None cuando no detected"
        assert entity["entity_name"] is None, "entity_name == None cuando no detected"


def is_abort(state):
    """Determina si el estado es un abort."""
    return state.get("abort_reason") is not None


class TestContractHappyPath:
    """Test: entidad detectada"""
    
    def test_entity_detected_bbva(self):
        state = app.invoke({"url": "http://bbva.es/login"})
        
        assert state.get("abort_reason") is None
        assert state["entity"] is not None
        validate_entity_invariants(state["entity"])
        assert state["entity"]["entity_detected"] is True
        assert state["entity"]["entity_id"] == "bbva"
        assert state["entity"]["entity_name"] == "BBVA"


class TestContractNoEntity:
    """Test: sin entidad detectada"""
    
    def test_no_entity_detected(self):
        state = app.invoke({"url": "http://login-seguro.com"})
        
        assert state.get("abort_reason") is None
        assert state["entity"] is not None
        validate_entity_invariants(state["entity"])
        assert state["entity"]["entity_detected"] is False
        assert state["entity"]["entity_id"] is None
        assert state["entity"]["entity_name"] is None


class TestContractAbort:
    """Test: input inválido → abort limpio"""
    
    def test_empty_url(self):
        state = app.invoke({"url": ""})
        
        assert is_abort(state), "debe ser abort"
        assert state.get("entity") is None, "entity debe ser None en abort"
    
    def test_missing_url(self):
        state = app.invoke({})
        
        assert is_abort(state), "debe ser abort"
        assert state.get("entity") is None, "entity debe ser None en abort"
    
    def test_invalid_url_type(self):
        state = app.invoke({"url": 123})
        
        assert is_abort(state), "debe ser abort"
        assert state.get("entity") is None, "entity debe ser None en abort"
