# sector_entidad_lang

## Que es este proyecto

Flujo LangGraph determinista para deteccion de entidades a partir de URLs.
Recibe una URL, busca tokens conocidos en ella y devuelve la entidad asociada si existe coincidencia.

## Que NO es

- No es un detector de phishing.
- No es un priorizador de alertas.
- No utiliza Machine Learning ni LLMs.
- No hace scoring ni clasificacion.

## Que NO entra en v3

- sector
- scoring
- LLM
- abstracciones extra
- logica nueva

## Input

Diccionario con una clave `url` de tipo string.

```python
{"url": "http://ejemplo.com"}
```

## Output (Contrato v3)

### Caso exito (sin abort)

```python
{
    "entity": {
        "entity_detected": True,   # o False
        "entity_id": "bbva",       # o None si detected=False
        "entity_name": "BBVA"      # o None si detected=False
    },
    "abort_reason": None,
    "violations": []
}
```

**Invariantes:**
- `entity.entity_detected` siempre presente (bool)
- Si `True` → `entity_id` y `entity_name` no-None
- Si `False` → `entity_id` y `entity_name` None

### Caso abort

```python
{
    "entity": None,
    "abort_reason": "url missing or invalid",  # o violations != []
    "violations": []
}
```

## Como funciona (v3)

El grafo ejecuta los siguientes nodos:

1. **validate_input** - Valida que `url` sea string valido. Retorna `input` o `abort_reason`.
2. **[gate]** - Si `abort_reason` o `violations` → END.
3. **detector_mecanico** - Busca tokens en la URL. Retorna `entity`.
4. **finalize** - Valida invariantes del contrato. Retorna `violations` si falla.

## Invariantes del sistema

- **Nodos puros**: no mutan estado, retornan deltas.
- **Gates**: solo leen flags, no computan.
- **Determinismo**: mismo input → mismo output (sin timestamps/UUIDs en contrato).
- **Defensividad**: accesos con `.get()`, cero excepciones por datos.

## Como ejecutar

```bash
pip install -r requirements.txt
python main.py
```

## Como testear

```bash
pytest test_contract.py -v
```

## Estado del proyecto

- Version actual: v3
- Version congelada: v2 (tag v2.0)
