# Patrones Observados — Detector Mecánico v0

> Observaciones empíricas y limitaciones del detector actual.

---

⚠️ Documento descriptivo (NO NORMATIVO)

Este documento recoge observaciones empíricas sobre URLs procesadas por el detector mecánico v0.
- NO define reglas.
- NO justifica cambios en el detector.
- NO altera el comportamiento del sistema.
- NO es input para decisiones automáticas.

Cualquier uso operativo de estos patrones requiere una nueva versión contractual (v1).

---

## Limitaciones conocidas

| Limitación | Descripción |
|------------|-------------|
| Sin exclusiones | No filtra labels genéricos (www, cdn, api) ni segmentos comunes (assets, static) |
| Primera coincidencia | Retorna la primera entidad encontrada; no detecta múltiples entidades |
| Sin ABORT | No aborta si hay ambigüedad (múltiples entidades posibles) |
| Sin límite de profundidad | Evalúa paths de cualquier longitud |

---

## Observaciones por capa

### Capa 1 — Dominio exacto

- No valida que el dominio sea legítimo, solo que termine en `{token}.es` o `{token}.com`.
- Incluye subdominios (ej: `www.bbva.es` también coincide con token `bbva`).

### Capa 2 — Subdominio

- Detecta cuando el token aparece como primer label DNS.
- No distingue dominios legítimos de fraudulentos.

### Capa 3 — Segmento en path

- Match exacto del segmento completo (no substrings).
- Evalúa todos los segmentos del path sin límite de profundidad.

---

## Patrones empíricos observados

### P1 — Marca en subdominio de dominio ajeno

**Descripción:**  
La marca aparece en subdominio o prefijo, pero el dominio registrado pertenece a un tercero.

**Señales comunes:**
- bancosantander.es.hotelparadis.es
- particulares-bancosantander-es.tempurl.host
- dominios tipo *.preview-domain.com, *.tempurl.host

**Ejemplos:**
- bancosantander.es.hotelparadis.es/aviso/…
- particulares-bancosantander-es.tempurl.host/…

---

### P2 — Marca solo en path profundo

**Descripción:**  
La marca no está en el dominio, aparece únicamente en segmentos de ruta.

**Señales comunes:**
- /Caixabank/particulares_es/home/…
- /SANTANDER-DRO/home/…
- paths largos, jerárquicos

**Ejemplos:**
- wcomhost.com/Caixabank/particulares_es/…
- ingress-earth.ewp.live/SANTANDER-DRO/…

---

### P3 — Hosting genérico + semántica bancaria

**Descripción:**  
Infraestructura genérica (hosting gratuito / temporal) combinada con paths bancarios.

**Señales comunes:**
- wcomhost.com, easywp.com, ewp.live, codeanyapp.com
- rutas con login, particulares, home, clientes

**Ejemplos:**
- 0560db8.wcomhost.com/Caixabank/…
- caixma-*.ewp.live/…/particulares/…

---

### P4 — Concatenación agresiva de tokens

**Descripción:**  
Dominio o subdominio con múltiples tokens concatenados (marca + idioma + acción).

**Señales comunes:**
- bancosantander-es-online
- bancosantander-firma-es-account-activation
- tokens unidos por -

**Ejemplos:**
- bancosantander-es-online.preview-domain.com/…
- bancosantander-firma-es-account-activation-*.codeanyapp.com/…

---

### P5 — Múltiples marcas / ruido léxico

**Descripción:**  
URL contiene varias marcas o palabras clave no coherentes entre sí.

**Señales comunes:**
- repetición de nombres (instagram…instagram)
- mezcla marca + país + plataforma

**Ejemplos:**
- instagramusicabrasilinstagram.blogspot.com.es

---

### P6 — Marca correcta pero enterrada en dominio largo

**Descripción:**  
La marca aparece como parte de un dominio extremadamente largo con múltiples niveles.

**Señales comunes:**
- acceso.caixabank.es.theacademy.co.ug
- dominios con >3 niveles antes del TLD

**Ejemplos:**
- acceso.caixabank.es.theacademy.co.ug/…
