# Auditor Mecánico v1

## Qué es

Auditor mecánico offline que asigna exactamente un patrón P0–P8 por URL.

- Ejecuta un auditor mecánico vía LLM (Ollama) bajo contrato estricto.
- Sin inferencia, sin aprendizaje, sin estado
- Produce output estructurado en JSONL

## Qué NO es

- No valida corrección
- No decide entidad
- No propone reglas ni mejoras
- No forma parte del flujo LangGraph
- No modifica el sistema activo

## Input

CSV con columnas:

| Columna | Descripción |
|---------|-------------|
| `url` | URL a auditar |
| `detected_entity` | Entidad detectada por el sistema |
| `human_entity` | Entidad asignada por humano |
| `reviewed` | Flag de revisión |

## Output

Archivo `.jsonl`. Una línea por URL válida.

Schema cerrado:

```json
{
  "pattern_id": "P0|P1|P2|P3|P4|P5|P6|P7|P8",
  "pattern_confidence": "low|medium|high",
  "pattern_evidence": "fragmentos literales de la URL",
  "notes": "opcional"
}
```
Siempre se asigna un único pattern_id, ante duda, p0

## Uso

```bash
# Default: usa rem/inputs/cases.csv y modelo gemma3:4b
python scripts/run_auditor_v1.py

# CSV personalizado
python scripts/run_auditor_v1.py /path/to/cases.csv

# CSV y modelo personalizados
python scripts/run_auditor_v1.py /path/to/cases.csv qwen
```

Output en `rem/mecanico/outputs/auditor_v1_{fecha}.jsonl`

## Gobernanza

- Contrato v1 **FROZEN**
- No se modifica
- Cualquier cambio implica crear auditor v2
- Outputs no se consumen automáticamente

## Artefactos

| Archivo | Función |
|---------|---------|
| `PROMPT.txt` | Prompt enviado al modelo |
| `contrato_auditor_mecanico_v1.md` | Especificación formal |

## Estado

**v1 — FROZEN**
