Lecciones aprendidas — LangGraph v2 → v3

(guía-burros, sin framework-speak)

1. Un nodo NO es dueño del estado

Si un nodo hace state["x"] = y, manda.

En sistemas gobernados, los nodos no mandan.

Regla:
Nodo = lee → propone
Grafo = decide → aplica

2. “Nodo puro” en LangGraph NO es lo que parece

Nodo puro ≠ devolver un state nuevo completo.

Nodo puro = devolver solo deltas (partial_update).

Bien: return {"entity_id": "bbva"}
Mal: return state

3. El estado es lógico, no operativo

UUIDs, timestamps, logs no son lógica.

Si algo cambia entre ejecuciones con el mismo input, no pertenece al state contractual.

Regla:
Lógica decide.
Meta observa.

4. Errores ≠ violaciones

errors = informativo, el flujo puede seguir.

violations = contrato roto → ABORT.

No mezclarlo o el sistema nunca sabrá decir “no”.

5. Los gates no piensan

Un gate no computa.

Un gate no valida.

Un gate solo lee flags ya calculados.

Si un gate tiene lógica, está mal ubicada.

6. Ningún nodo debe lanzar excepciones por datos

KeyError, TypeError, etc. no son control.

Todo fallo debe convertirse en estado explícito.

Principio:
Los sistemas serios no crashean: aborton.
a
7. Separar semántica ≠ separar estructuras

Separar “lógica” y “meta” no implica TypedDicts anidados.

LangGraph funciona mejor con state plano.

Regla:
Separa por significado, no por capas técnicas.

8. La autoridad no se impone con código (en grafos pequeños)

Guards por nodo, validadores runtime, permisos de escritura → sobre-ingeniería.

En grafos de 5 nodos, la autoridad se mantiene con:

- README claro
- convención
- revisión

9. v3 NO es para añadir dominio

v3 no mejora detección.

v3 no añade sector, scoring ni inteligencia.

Función de v3:
Hacer gobernable lo que ya funciona.

10. Tests antes que arquitectura

Antes de refactorizar:

congela comportamiento con tests de app.invoke().

Si no, no sabrás si rompiste algo o “mejoraste”.

11. LangGraph ya es la abstracción

No interfaces.
No adapters.
No factories.

Regla:
Funciones + grafo.
Nada más.
