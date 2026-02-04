# Auditor v1 — Checklist Operativa

Esta checklist define **cómo debe actuar el Auditor v1** al analizar un caso.
No define patrones ni reglas mecánicas.
No propone cambios al sistema.

---

## 1. Pre-check (obligatorio)

Antes de auditar una URL, verificar:

- `reviewed == true`
- `url` es string no vacío
- `detected_entity` presente (puede ser vacío)
- `human_entity` presente (puede ser vacío)

Si alguno falla → **NO AUDITAR**.

---

## 2. Determinar delta

Comparar:

- `detected_entity` (sistema)
- `human_entity` (humano)

Clasificar **exactamente uno**:

- `TP` — ambos coinciden
- `FP` — sistema detecta, humano no
- `FN` — sistema no detecta, humano sí
- `TN` — ninguno detecta

Si el delta no es claro → **NO AUDITAR**.

---

## 3. Evaluación de patrones (sin prioridad)

- Evaluar **todos** los patrones aplicables según la taxonomía.
- Asignar `primary_pattern` **solo si uno encaja de forma clara y dominante**.
- Si hay co-ocurrencia sin dominancia → `primary_pattern = P0`.
- Registrar patrones adicionales en `secondary_patterns` (observacional, sin efecto operativo).

Formato de salida:
- `primary_pattern`: uno o `P0`
- `secondary_patterns`: lista 0..N
---

## 4. Evidencia literal

Seleccionar **1 a 3 fragmentos literales** de la URL
que justifiquen el patrón elegido.

- Deben aparecer **exactamente** en la URL
- No se permite interpretación ni contexto externo

---

## 5. Cierre

- Si existe duda razonable → asignar `P0 — NO_PATTERN`
- Redactar `notes` descriptivas (máx. 2 líneas)
- No sugerir reglas ni cambios

---

## Reglas duras

- Un patrón o ninguno
- Evidencia siempre literal
- Cero inferencia
- Cero propuestas

---

Estado: **v1 — ACTIVO**
