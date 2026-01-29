# Patrones observados – Auditor v0
Fecha: 2026-01-29
Fuente: auditor_outputs_raw_2026-01-29.md

Este documento recoge patrones observados de forma repetida en el output del auditor LLM.
No son reglas. No implican decisiones. No se aplican al sistema activo.

---

## P1. Marca presente fuera del dominio raíz

Observación:
La marca asociada a una entidad aparece frecuentemente en subdominios largos o en la ruta,
no en el dominio raíz registrado.

Ejemplos estructurales:
- marca en subdominio profundo
- marca en path con múltiples niveles

Nota:
El sistema mecánico actual solo detecta coincidencias literales simples en path
y dominio, lo que deja fuera muchos de estos casos.

---

## P2. Dominio contenedor genérico + estructura interna rica

Observación:
Se repiten dominios genéricos o de infraestructura que alojan rutas con alta
carga semántica asociada a entidades conocidas.

Dominios contenedor recurrentes:
- servicios de hosting
- plataformas de despliegue
- dominios técnicos no asociados a marca

Nota:
El patrón no es el dominio en sí, sino la combinación dominio genérico + path informativo.

---

## P3. Alta densidad de tokens funcionales en la ruta

Observación:
Las rutas contienen múltiples tokens funcionales relacionados con acciones de usuario,
especialmente en contextos de autenticación o gestión.

Tokens recurrentes:
- login
- sms
- codigo
- firma
- recibir
- cuenta
- usuario

Nota:
No es un token aislado, sino la acumulación de varios en una misma URL.

---

## P4. Estructuras WordPress reutilizadas

Observación:
Aparecen rutas y directorios típicos de WordPress en múltiples URLs analizadas.

Indicadores estructurales:
- wp-admin
- wp-includes
- rutas internas largas

Nota:
No identifican entidad, pero aparecen de forma consistente como contexto técnico.

---

## P5. Complejidad estructural elevada

Observación:
Muchas URLs presentan:
- múltiples subdominios
- paths muy profundos
- mezcla de tokens relevantes e irrelevantes

Nota:
La complejidad estructural aparece de forma recurrente como fuente de ambigüedad,
no como señal única.

---

## Fuera de alcance

- No se derivan reglas a partir de estos patrones.
- No se ajustan pesos ni prioridades.
- No se modifica el sistema mecánico.
- La interpretación es exclusivamente humana.
