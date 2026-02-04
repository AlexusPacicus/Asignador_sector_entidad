# Auditor Offline v0

## Qué es el auditor

El auditor offline v0 es un script de análisis descriptivo que se ejecutó manualmente durante el desarrollo del sistema de detección de entidad en URLs.

Su función fue generar descripciones textuales sobre las señales observables en URLs procesadas, utilizando un modelo de lenguaje local (Ollama/gemma3:4b). El auditor recibía pares `(url, detected_entity)` de un CSV de casos y producía texto libre describiendo:

- Señales literales visibles en la URL (dominio, segmentos de ruta).
- Patrones generales que esas señales podrían indicar.
- Ambigüedades o elementos que dificultan la detección.

El auditor no participó en el flujo de detección activo ni modificó ningún comportamiento del sistema.

## Qué NO es el auditor

- **No es un validador.** No determina si una detección es correcta o incorrecta.
- **No es un decisor.** No elige entidades ni resuelve casos ambiguos.
- **No propone reglas.** No sugiere patrones, pesos, prioridades ni mejoras.
- **No es un componente del sistema activo.** Sus outputs no se consumen automáticamente.
- **No aprende ni se ajusta.** No hay retroalimentación ni ciclo de mejora.

El prompt del auditor incluye restricciones explícitas que le impiden evaluar corrección, proponer cambios o justificar el sistema.

## Cuándo se usó (fase v0)

El auditor se ejecutó durante la fase inicial de desarrollo (v0) para generar evidencia descriptiva sobre casos procesados por el sistema de detección.

Su uso fue:

1. **Manual.** Un operador ejecutaba el script `run_auditor_v0.py` contra un CSV de casos.
2. **Offline.** No conectado al flujo de detección ni a ningún pipeline activo.
3. **Puntual.** Se ejecutó en momentos específicos para documentar tensiones semánticas observadas.

El auditor operó bajo reglas pasivas (`RULES_PASSIVE.txt`) que describen cómo funciona la detección: coincidencia literal exacta contra listas cerradas, sin inferencia semántica.

## Qué genera (outputs)

Cada ejecución produce un archivo Markdown en `auditor/outputs/` con el formato:

```
auditor_outputs_raw_YYYY-MM-DD.md
auditor_outputs_raw_YYYY-MM-DD_N.md  (si hay múltiples ejecuciones el mismo día)
```

Cada archivo contiene:

- Fecha de ejecución y CSV de origen.
- Una sección por URL procesada con:
  - La URL analizada.
  - La entidad detectada (o vacío si no hubo detección).
  - El texto libre generado por el modelo.

Los outputs son texto descriptivo sin estructura formal. No contienen puntuaciones, rankings ni recomendaciones.

## Estado actual

**CERRADO.**

El auditor v0 no se modifica, no se vuelve a ejecutar y no recibe mantenimiento.

Los artefactos generados permanecen como evidencia histórica de la fase de desarrollo.

## Nota de gobernanza

El auditor v0 se cerró por las siguientes razones:

1. **Alcance cumplido.** Generó la documentación descriptiva necesaria para la fase inicial.
2. **Riesgo de deriva.** Mantenerlo abierto invitaría a atribuirle capacidades que no tiene.
3. **Claridad operativa.** Un componente cerrado no genera expectativas de evolución.

Cualquier necesidad futura de análisis descriptivo implicaría crear un auditor v1 con alcance y restricciones definidas desde cero.

---

*Este documento describe el auditor tal como existió. No constituye una especificación para futuros desarrollos.*
