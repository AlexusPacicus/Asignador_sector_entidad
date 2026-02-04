# Auditor Mecánico Output - 2026-02-04

**CSV:** cases.csv
**Modelo:** gemma3:4b

---

## [1] URL

```
http://044088d.wcomhost.com/www.santanader.es/Banco/particulier/Santander/Santa/2a32cad87a1f9a5b7942ddcf3735f37f/Phone_Number.php
```

**detected_entity:** santander

**human_entity:** santander

### Output:

```json
```json
{
  "pattern_id": "P2",
  "pattern_confidence": "high",
  "pattern_evidence": "/Banco/particulier/Santander/Santa/",
  "notes": "Marca presente solo en la ruta."
}
```
```

---

## [2] URL

```
http://0c4d4e6.wcomhost.com/Banco-Santander/particulares/Iogin/home/sms_codigo.php
```

**detected_entity:** (vacío)

**human_entity:** santander

### Output:

```json
```json
{
  "pattern_id": "P3",
  "pattern_confidence": "high",
  "pattern_evidence": "Banco-Santander",
  "notes": "La marca 'Santander' está fusionada con otros tokens ('particulares', 'Iogin', 'home', 'sms_codigo') sin separadores claros."
}
```
```

---

## [3] URL

```
http://agancicaix034-b726fc.ingress-baronn.ewp.live/wp-admin/acceso/es/clients/login.php
```

**detected_entity:** (vacío)

**human_entity:** caixabank

### Output:

```json
```json
{
  "pattern_id": "P8",
  "pattern_confidence": "high",
  "pattern_evidence": "http://agancicaix034-b726fc.ingress-baronn.ewp.live/wp-admin/acceso/es/clients/login.php",
  "notes": "Variante ortográfica deliberada de la marca (errores mínimos). Typoquatting de 'caixabank'."
}
```
```

---

## [4] URL

```
http://alertanotificacionesdinamicos.com/Verificacion/Estado/Ingreso/Proceso/Estimado/sucarsal/index.php
```

**detected_entity:** (vacío)

**human_entity:** (vacío)

### Output:

```json
```json
{
  "pattern_id": "P3",
  "pattern_confidence": "medium",
  "pattern_evidence": "alertanotificacionesdinamicos.com/Verificacion/Estado/Ingreso/Proceso/Estimado/sucarsal/index.php",
  "notes": "Brand concatenated with tokens: alertanotificacionesdinamicos.com"
}
```
```

---

## [6] URL

```
http://ayusjcaexascuentolasalaos-b632a8.ingress-daribow.ewp.live/audirs/home/sms.html
```

**detected_entity:** (vacío)

**human_entity:** (vacío)

### Output:

```json
```json
{
  "pattern_id": "P8",
  "pattern_confidence": "medium",
  "pattern_evidence": "sntnder",
  "notes": "Variante ortográfica deliberada de la marca (errores mínimos)."
}
```
```

---

## [7] URL

```
http://bancaonline.bankinter.com.login.cuenta.mazayame.com/?pwd=bankinter
```

**detected_entity:** (vacío)

**human_entity:** bankinter

### Output:

```json
```json
{
  "pattern_id": "P5",
  "pattern_confidence": "medium",
  "pattern_evidence": "http://bancaonline.bankinter.com.login.cuenta.mazayame.com/?pwd=bankinter",
  "notes": "Uso engañoso de país/TLD. El TLD .com se usa en conjunción con .cuenta.mazayame.com, lo que genera confusión sobre la ubicación legítima del servicio."
}
```
```

---

## [8] URL

```
http://bancosantander.es.hotelparadis.es/aviso/60d6672570af1c8/login.php
```

**detected_entity:** (vacío)

**human_entity:** santander

### Output:

```json
```json
{
  "pattern_id": "P3",
  "pattern_confidence": "medium",
  "pattern_evidence": "bancosantander",
  "notes": "La marca 'Santander' está fusionada con otros tokens sin separadores claros."
}
```
```

---

## [9] URL

```
http://bbvaspaing.temp.swtest.ru/bbva21/bbva/area_cliente/SMSconfirmacion.html
```

**detected_entity:** bbva

**human_entity:** bbva

### Output:

```json
```json
{
  "pattern_id": "P2",
  "pattern_confidence": "high",
  "pattern_evidence": " /bbva21/bbva/area_cliente/SMSconfirmacion.html",
  "notes": "Brand only in path."
}
```
```

---

## [10] URL

```
http://caixabank.es.sabadent.ir/particular/holabank/online-banking/login.php?cmd=login_submit&id=50e1dfe46956cea691d7a1586bbfff5d50e1dfe46956cea691d7a1586bbfff5d&session=50e1dfe46956cea691d7a1586bbfff5d
```

**detected_entity:** (vacío)

**human_entity:** caixabank

### Output:

```json
```json
{
  "pattern_id": "P4",
  "pattern_confidence": "medium",
  "pattern_evidence": "/caixabank.es.sabadent.ir/particular/holabank/online-banking/login.php",
  "notes": "Multiple brand tokens present: caixabank, holabank."
}
```
```

---

## [11] URL

```
http://caixa-confirmacion-974baa.ingress-florina.easywp.com/mi-cuenta/acceso/es/clients/login.php?verification
```

**detected_entity:** (vacío)

**human_entity:** caixabank

### Output:

```json
```json
{
  "pattern_id": "P4",
  "pattern_confidence": "medium",
  "pattern_evidence": "caixa-confirmacion-974baa.ingress-florina.easywp.com/mi-cuenta/acceso/es/clients/login.php",
  "notes": "Uso engañoso de país/TLD asociado a la marca."
}
```
```

---

## [12] URL

```
http://casosapple.com-verificacionapple.com/index.php/false/false/py1n.html/discovercard.com/dfs/accounthome/summary/-www.schwab.com/secure.accurint.com/unfcu2.org/login1/wachovia.com/myaccounts.aspx/investing.schwab.com
```

**detected_entity:** (vacío)

**human_entity:** apple

### Output:

```json
```json
{
  "pattern_id": "P4",
  "pattern_confidence": "medium",
  "pattern_evidence": "/discovercard.com/dfs/accounthome/summary/-www.schwab.com/secure.accurint.com/unfcu2.org/login1/wachovia.com/myaccounts.aspx/investing.schwab.com",
  "notes": "Multiple brands present in the URL path."
}
```
```

---

## [13] URL

```
http://correos-1-bc9a64.ingress-erytho.ewp.live/info/pagomente
```

**detected_entity:** (vacío)

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P2",
  "pattern_confidence": "high",
  "pattern_evidence": " /info/pagomente",
  "notes": "La marca 'correos' aparece únicamente en la ruta."
}
```
```

---

## [14] URL

```
http://correos-cliente-spain.koncil.com/pago/manage/sms/sms2.html
```

**detected_entity:** (vacío)

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P5",
  "pattern_confidence": "high",
  "pattern_evidence": "correos-cliente-spain",
  "notes": "Uso engañoso de país/TLD asociado a la marca sin dominio legítimo."
}
```
```

---

## [15] URL

```
http://correos.es-es-es-herramientas-localizador-envios.u962745a2w.ha005.t.justns.ru/71da2eb1bb4778f/sms/index.html
```

**detected_entity:** correos

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P5",
  "pattern_confidence": "high",
  "pattern_evidence": "bbva.es-login.com",
  "notes": "Uso engañoso de país/TLD asociado a la marca sin dominio legítimo."
}
```
```

---

## [16] URL

```
http://correosexpress.elementor.cloud/wp-content/plugins/pagomente/Recibir_paquete.php
```

**detected_entity:** (vacío)

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P2",
  "pattern_confidence": "high",
  "pattern_evidence": " /correosexpress/",
  "notes": "Marca presente solamente en la ruta."
}
```
```

---

## [17] URL

```
http://correosseuraviso.page.link/infos
```

**detected_entity:** (vacío)

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P8",
  "pattern_confidence": "low",
  "pattern_evidence": "correosseuraviso.page.link",
  "notes": "Variante ortográfica deliberada de la marca (errores mínimos)."
}
```
```

---

## [19] URL

```
http://correos-tracking.tempurl.host/es/Recibir_paquete.php
```

**detected_entity:** (vacío)

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P3",
  "pattern_confidence": "medium",
  "pattern_evidence": "Recibir_paquete.php",
  "notes": "URL contiene el token 'Recibir' junto con 'paquete', similar a patrones de concatenación de tokens."
}
```
```

---

## [20] URL

```
http://cuenta-confirmacion-974baa.ingress-bonde.easywp.com/mi-cuenta/acceso/es/clients/login.php?verification=
```

**detected_entity:** (vacío)

**human_entity:** correos

### Output:

```json
```json
{
  "pattern_id": "P5",
  "pattern_confidence": "medium",
  "pattern_evidence": "cuenta-confirmacion-974baa.ingress-bonde.easywp.com",
  "notes": "TLD 'es' asociado a marca y subdominio de dominio ajeno."
}
```
```

---

## [21] URL

```
http://cuentas.15-237-142-160.cprapid.com/bbva2/?id_jibbrs=dr-417538
```

**detected_entity:** (vacío)

**human_entity:** bbva

### Output:

```json
```json
{
  "pattern_id": "P1",
  "pattern_confidence": "medium",
  "pattern_evidence": "cuentas.15-237-142-160.cprapid.com",
  "notes": "Subdominio 'cuentas' con la marca 'bbva' y un IP."
}
```
```

---

## [22] URL

```
http://hiringindia.com/pr/Actualizar-informacion/accesso/2b960/acceso-clientes/sms.php?Pm2d-zKiF7DBev16fBE56fX2S6FAjdaZ2x1g:6LyMTcn7-IoeX0T2780907PBq3Mp6kqmrcVd57AdQZrNZlQ7tQguX56n8SN
```

**detected_entity:** (vacío)

**human_entity:** (vacío)

### Output:

```json
```json
{
  "pattern_id": "P6",
  "pattern_confidence": "low",
  "pattern_evidence": "token genérico/colisión",
  "notes": "El token 'acceso' es genérico y ampliamente utilizado, sin una clara asociación con la marca 'hiringindia'."
}
```
```

---

## [23] URL

```
http://ing.es-operacionesweb.info/loginon.php
```

**detected_entity:** (vacío)

**human_entity:** ing

### Output:

```json
```json
{
  "pattern_id": "P6",
  "pattern_confidence": "low",
  "pattern_evidence": "ing",
  "notes": "Token genérico/colisión."
}
```
```

---

## [24] URL

```
http://loc10cxixaayuodaaccesoae-b40361.ingress-florina.ewp.live/loca4/home/sms2.html
```

**detected_entity:** (vacío)

**human_entity:** caixabank

### Output:

```json
```json
{
  "pattern_id": "P8",
  "pattern_confidence": "high",
  "pattern_evidence": "caixma",
  "notes": "Variante ortográfica deliberada de la marca (errores mínimos)."
}
```
```

---

## [25] URL

```
http://loc2.caixabank.es.ay-min.az/GPeticionesWebLogicSession/LaCaixa/home/Codigo.html
```

**detected_entity:** (vacío)

**human_entity:** caixabank

### Output:

```json
```json
{
  "pattern_id": "P4",
  "pattern_confidence": "medium",
  "pattern_evidence": " /caixabank.es.ay-min.az",
  "notes": "Multiple brand tokens present in the URL."
}
```
```

