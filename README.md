# sector_entidad_lang

Este proyecto implementa un flujo determinista basado en **LangGraph** para identificar entidades a través de sus URLs. El sistema analiza una dirección web, localiza tokens predefinidos en ella y devuelve la entidad asociada de forma estructurada y predecible.

## Propósito y Alcance

Para garantizar la precisión técnica, es fundamental definir los límites del sistema:

### Qué NO hace el sistema
*   **No es un detector de phishing:** No evalúa la seguridad de la URL.
*   **No prioriza alertas:** No gestiona la criticidad de los eventos.
*   **No usa IA:** No utiliza Machine Learning ni Modelos de Lenguaje (LLMs).
*   **No clasifica:** No realiza scoring ni categorización de datos.

### Exclusiones específicas de la v3
En esta versión no se incluye lógica de sectores, sistemas de puntuación, integraciones con LLMs ni abstracciones adicionales que no formen parte de la detección mecánica principal.

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
    "abort_reason": None
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
    "abort_reason": "url missing or invalid"
}
```

## Como funciona (v3)

El grafo ejecuta los siguientes nodos:

1. **validate_input** - Valida que `url` sea string valido. Retorna `input` o `abort_reason`.
2. **[gate]** - Si `abort_reason` → END.
3. **detector_mecanico** - Busca tokens en la URL. Retorna `entity`.

## Invariantes del sistema

- **Nodos puros**: no mutan estado, retornan deltas.
- **Gates**: solo leen flags, no computan.
- **Determinismo**: mismo input → mismo output (sin timestamps/UUIDs en contrato).
- **Defensividad**: accesos con `.get()`, cero excepciones por datos.

## Guía de Inicio Rápido

### Instalación y Ejecución
Para configurar el entorno y ejecutar el flujo principal:

```bash
pip install -r requirements.txt
python main.py
```

### Verificación del Contrato
Para asegurar que el sistema respeta los invariantes y el esquema de salida definido:

```bash
pytest test_contract.py -v
```

