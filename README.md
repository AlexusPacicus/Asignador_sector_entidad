# sector_entidad_lang

## Que es este proyecto

Flujo LangGraph determinista para enriquecimiento de entidades a partir de URLs.
Recibe una URL, busca tokens conocidos en ella y devuelve la entidad asociada si existe coincidencia.
El sistema asume URLs espanolas como precondicicon (tokens de bancos, organismos publicos y empresas espanolas).

## Que NO es

- No es un detector de phishing.
- No es un priorizador de alertas.
- No utiliza Machine Learning ni LLMs.

## Input

Diccionario con una clave `url` de tipo string.

```python
{
    "url": "http://ejemplo.com"
}
```

## Output

El estado final contiene un campo `result` con la siguiente estructura:

| Campo            | Tipo           | Descripcion                                      |
|------------------|----------------|--------------------------------------------------|
| `entity_id`      | `str` o `None` | Identificador de la entidad detectada            |
| `entity_name`    | `str` o `None` | Nombre legible de la entidad                     |
| `entity_detected`| `bool`         | `True` si se detecto entidad, `False` en caso contrario |

## Como funciona 

El grafo ejecuta los siguientes nodos en orden:

1. **ingest** - Inicializa el estado con metadatos y estructuras vacias.
2. **validate** - Verifica que el campo `url` sea un string valido.
3. **route** - Punto de decision: si ya existe `entity_id`, salta a finalize.
4. **enrich** - Busca tokens conocidos en la URL y asigna `entity_id` si hay coincidencia.
5. **finalize** - Construye el objeto `result` con los datos de la entidad.

## Como ejecutar

```bash
pip install -r requirements.txt
python main.py
```

## Ejemplo de ejecucion

### Input

```python
{
    "url": "http://bbva-login.com"
}
```

### Output

```python
{
    'url': 'http://bbva-login.com',
    'entity_id': 'bbva',
    'errors': [],
    'meta': {
        'run_id': '34aaaa61-081c-45de-b3ef-9c6457580012',
        'ts_start': '2026-01-27T17:34:24.941579',
        'ts_end': '2026-01-27T17:34:24.942873'
    },
    'result': {
        'entity_id': 'bbva',
        'entity_name': 'BBVA',
        'entity_detected': True
    }
}
```

## Estado del proyecto

- Version congelada: v2
- Auditada
- Lista para integracion aguas abajo
