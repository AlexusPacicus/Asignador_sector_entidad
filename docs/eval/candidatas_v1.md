## P6 — Detección por labels DNS (CANDIDATA)

- **Orden:** Se evalúa antes que P7.
- **Alcance:** Labels DNS previos al dominio registrado.
- **Exclusiones (labels):** www, mail, cdn, api, img, static, m, dev

### Regla
- Match exacto `entity.token == label`

### Decisión
- 0 matches → `NO_DECISION` (pasa a P7)
- 1 match → `DECIDE(entity_id)`
- ≥2 entidades distintas → `ABORT(reason="multiple_entities_dns")`

### Notas
- No evalúa path.
- No substrings.
- No pesos.

---

## P7 — Detección por ruta (CANDIDATA)

- **Precondición:** P6 no decidió (0 matches).
- **Alcance:** Segmentos de ruta (`/`), sin query ni fragment.
- **Exclusiones (segmentos):** wp-includes, assets, static, css, js, img
- **Límite:** Profundidad > 6 segmentos → no aplica.

### Regla
- Match exacto `entity.token == segment`

### Decisión
- 0 matches → `NO_ENTITY`
- 1 match → `DECIDE(entity_id)`
- ≥2 entidades distintas → `ABORT(reason="multiple_entities_path")`

### Notas
- No evalúa DNS si P6 decidió.
- No substrings.
- No pesos.

---

## Invariantes (no negociables)

- Orden fijo: P6 → P7
- Una entidad o ABORT
- Nunca combinar P6 y P7 en la misma URL
- Determinista, sin inferencia, sin scoring
