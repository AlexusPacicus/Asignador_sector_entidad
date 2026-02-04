# vo_patterns_human.md

Patrones observacionales extraídos del Auditor v0.  
Uso exclusivo como **contexto pasivo** para Auditor v1.  
No normativos. No prescriptivos. No accionables.

---

## VO-01 — Marca como subdominio de dominio registrado ajeno

La marca aparece como subdominio o prefijo mientras que el dominio registrado pertenece a un tercero.

**Señales observables típicas:**
- `marca.es.dominio-ajeno.tld`
- `marca-es-*.preview-domain.com`
- Subdominios largos que incluyen la marca completa

---

## VO-02 — Marca presente solo en la ruta (path)

La marca no aparece en el dominio, sino únicamente en uno o varios segmentos de la ruta.

**Señales observables típicas:**
- `/Marca/particulares/...`
- `/marca-movil/es/...`
- Marca como nombre de carpeta o archivo

---

## VO-03 — Marca concatenada con otros tokens

La marca aparece fusionada con otros términos sin separadores claros, tanto en dominio como en ruta.

**Señales observables típicas:**
- `bancosantander`
- `santanderes`
- `ingdirect-acceso`
- Marca unida a sufijos o prefijos funcionales

---

## VO-08 — Uso de país, TLD o subdominio asociado a la marca

La marca aparece junto a códigos de país, TLDs o subdominios que generan estructuras largas o ambiguas.

**Señales observables típicas:**
- `marca.es-login.com`
- `marca.es.theacademy.co.ug`
- Combinaciones de país y subdominio alrededor de la marca

---

## VO-09 — Variantes ortográficas cercanas a la marca

Aparición de tokens muy cercanos a la marca, pero no idénticos.

**Señales observables típicas:**
- `caixma`
- `caixanew`
- `caixa-…`
- Variantes con una o dos letras alteradas

---

## Notas de uso

- Estos patrones **no crean ni justifican** `primary_pattern`.
- Solo pueden influir en `secondary_patterns` o `notes`.
- Si no hay dominancia clara → `P0`.
- Ante duda razonable → `P0`.

Estado: **APTO como input de Auditor v1**.
