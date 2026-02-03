# sector_entidad_lang
# La lista de entidades está congelada

Este proyecto implementa un flujo determinista basado en LangGraph para la detección de entidades mediante el análisis de URLs. Su función principal es recibir una URL, buscar tokens predefinidos en su estructura y devolver la entidad correspondiente si existe una coincidencia exacta.

Nota crítica:
El sistema identifica referencias nominales de entidad en URLs como metadata.
La detección de una entidad NO implica legitimidad, ownership ni autenticidad del dominio.

## Descripción del Proyecto

El sistema está diseñado para ser predecible y eficiente, operando mediante reglas mecánicas de coincidencia de tokens en lugar de inferencia probabilística.

### Fuera de Alcance

Para mantener el enfoque y la simplicidad técnica, este proyecto **no** realiza las siguientes tareas:
- Detección de phishing o sitios maliciosos.
- Priorización o gestión de alertas.
- Uso de modelos de Machine Learning o Large Language Models (LLMs).
- Clasificación de contenidos o asignación de puntajes (scoring).

### Exclusiones de la Versión 3 (v3)

En la versión actual, se han excluido explícitamente las siguientes funcionalidades:
- Gestión de sectores.
- Sistemas de scoring.
- Integración con LLMs.
- Abstracciones adicionales o lógica de negocio compleja.

## Especificaciones de Entrada

El sistema recibe un diccionario con la clave `url` de tipo string:

```python
{"url": "http://ejemplo.com"}
```

## Contrato de Salida (v3)

### Caso de Éxito (Detección completada)

```python
{
    "entity": {
        "entity_detected": True,   # o False
        "entity_id": "bbva",       # o None si detected=False
        "entity_name": "BBVA"      # o None si detected=False
    },
    "abort_reason": None,
}
```

**Invariantes de Salida:**
- `entity.entity_detected` siempre está presente como valor booleano.
- Si es `True`, `entity_id` y `entity_name` deben tener valores (no-None).
- Si es `False`, `entity_id` y `entity_name` deben ser `None`.

### Caso de Aborto (Error o Validación fallida)

```python
{
    "entity": None,
    "abort_reason": "url missing or invalid"
```

## Funcionamiento Interno (v3)

El grafo de ejecución se compone de los siguientes nodos:

1. **validate_input**: Valida que la URL sea un string válido. Retorna el input procesado o un motivo de aborto (`abort_reason`).
2. **[gate]**: Nodo de control. Si existe un `abort_reason`, el flujo finaliza inmediatamente.
3. **detector_mecanico**: Realiza la búsqueda de tokens en la URL. Retorna la entidad detectada (`entity`).

## Invariantes del Sistema

- **Nodos Puros**: Los nodos no modifican el estado global; retornan deltas que se integran al flujo.
- **Gates (Compuertas)**: Solo evalúan banderas existentes, no realizan cálculos adicionales.
- **Determinismo**: El mismo input garantiza siempre el mismo output. No se incluyen elementos variables como marcas de tiempo o UUIDs en el contrato.
- **Programación Defensiva**: Se prioriza el uso de `.get()` para accesos seguros a datos, evitando excepciones en tiempo de ejecución.

## Instalación y Ejecución

Para poner en marcha el proyecto, ejecute los siguientes comandos:

```bash
pip install -r requirements.txt
python -m main.py
```

## Pruebas

Para validar el contrato y la lógica del sistema:

```bash
pytest test_contract.py -v
```

Estado del detector mecánico:
v0 — FROZEN.
El comportamiento descrito es estable y no se modifica sin nueva versión (v1).
