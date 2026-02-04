# Auditor Output - 2026-01-29

**CSV:** cases_post_R1_2026-01-29.csv

---

## URL: http://particulares-bancosantander-es.tempurl.host/es/grupo/home/codigo_incorrecta.php

**detected_entity:** (vacío)

### Output del modelo:

Señales observables:

* particulars (subdominio)
* bancosantander (subdominio)
* es (tomo de dominio)
* grupo (ruta)
* home (ruta)
* codigo_incorrecta (ruta)

Patrón potencial:
La presencia de subdominios y rutas que contienen palabras relacionadas con una entidad financiera, como "bancosantander" y "codigo_incorrecta", sugieren un patrón que se refiere a una entidad bancaria.

Ambigüedades:

• La ruta "grupo" puede referirse a diferentes tipos de grupos (organizaciones, comunidades, etc.), lo que podría confundir la detección.
• La palabra "incorrecta" en el nombre del archivo PHP puede ser una señal de alerta o una excepción, lo que podría requerir una evaluación adicional.

---

## URL: http://loc52.caixabank.es.lacaixa.actualizar.information.ay-min.az/soporte-directonow/home/Espera.html

**detected_entity:** (vacío)

### Output del modelo:

Señales observables:

* loc52.caixabank (dominio)
* caixa (subdominio)
* actualizer-information (ruta)
* ay-min (ruta)
* az (ruta)
* soporte-directonow (ruta)
* home (ruta)

Patrón potencial:
La presencia de subdominios y rutas que contienen tokens relevantes ("caixa", "actualizer-information", etc.) puede indicar un patrón general relacionado con la entidad "L Caixa Bank" o una división específica dentro de esta entidad.

Ambigüedades:

• La ruta "home" podría ser ambiguamente relacionada con cualquier entidad que tenga una sección llamada "home".
• La ruta "Espera.html" no es claramente relevante para la detección de la entidad.

---

## URL: http://oficinacorreos.page.link/es

**detected_entity:** (vacío)

### Output del modelo:

Señales observables:

* "oficinacorreos"
* ".page"
* "link"

Patrón potencial:
La presencia de "oficinacorreos" como dominio, seguida de la extensión ".page" y el token "link", puede indicar un patrón relacionado con correos o comunicación.

Ambigüedades:

• La palabra "link" puede referirse a una dirección en línea, lo que no necesariamente indica una entidad específica.
• El dominio "oficinacorreos" podría pertenecer a diferentes entidades (por ejemplo, oficina de correos o servicio de correos electrónicos).
• La extensión ".page" puede ser parte de un sitio web personal o una plataforma de contenido, lo que no proporciona información específica sobre la entidad.

---

## URL: https://bbva.es.suspension-tarjeta.com

**detected_entity:** bbva

### Output del modelo:

Señales observables:

* La URL contiene el dominio "bbva" con precisión, lo que podría indicar una relación directa con la entidad detectada.
* El subdominio ".es" sugiere un vínculo con España, lo que podría ser relevante para la detección de la entidad.
* La ruta "/suspension-tarjeta.com" puede contener tokens relevantes asociados a la entidad.

Patrón potencial:

La presencia del dominio "bbva" y el subdominio ".es" sugiere un patrón de detección que se centra en la identidad de una entidad financiera con presencia en España, lo que podría indicar que la entidad detectada es una institución bancaria o financiera.

Ambigüedades:

• La ruta "/suspension-tarjeta.com" puede contener información adicional sobre el servicio o producto ofrecido por la entidad, lo que podría influir en la detección.
• El uso de un subdominio ".es" no es exclusivo de BBVA y puede ser compartido por otras entidades financieras con presencia en España.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/sms_codigo.php

**detected_entity:** santander

### Output del modelo:

Señales observables:

* wcomhost.com (subdominio)
* santanderbanco.es (dominio)
* bancosantander (ruta)
* Santander (ruta)

Patrón potencial:
El patrón puede ser la presencia de un subdominio y un dominio que contienen el nombre de la entidad, seguido por una ruta que también contiene ese nombre. Esto sugiere que la entidad podría estar relacionada con el banco o institución financiera "Santander".

Ambigüedades:
• La ruta puede contener tokens irrelevantes para la detección, como "/14a6aa73533e725206d52204cb133ae4/"
• La presencia de palabras clave en el dominio y subdominio puede ser confusa si no se considera la estructura completa de la URL.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/fc1d08f1e92f5327005249a01496da74/sms_codigo.php

**detected_entity:** santander

### Output del modelo:

Señales observables:

* wcomhost.com (subdominio)
* santanderbanco.es (dominio exacto)
* bancosantander (ruta conteniendo tokens relevantes)
* es (ruta conteniendo tokens relevantes)

Patrón potencial:
La presencia de "santander" en el dominio o ruta sugiere una posible relación con la entidad Santander.

Ambigüedades:

• La ruta puede contener otros tokens relevantes, lo que podría distraer la atención.
• El uso de subdominios y rutas puede hacer que sea difícil distinguir entre señales confiables y no confiables.

---

## URL: https://2022-bdaef4.ingress-earth.ewp.live/correos/Recibir_paquete.php

**detected_entity:** correos

### Output del modelo:

Señales observables:

1. El dominio comienza con "2022-" seguido de un código alfanumérico.
2. La ruta contiene la cadena "correos".
3. La ruta termina con una extensión ".php".

Patrón potencial:
La presencia del código alfanumérico en el dominio y la cadena "correos" en la ruta pueden indicar un patrón de identificación de entidad relacionado con correos o servicios de comunicación.

Ambigüedades:

* El uso de números consecutivos en el dominio puede generar ambigüedad sobre si se trata de una fecha o un código único.
* La extensión ".php" puede ser confundida con otros lenguajes o tecnologías web, lo que puede afectar la precisión de la detección.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/codigo_incorrecta.php

**detected_entity:** santander

### Output del modelo:

Señales observables:

* santander (subdominio)
* bancosantander (ruta)
* particulares (ruta)

Patrón potencial:
La presencia de "santander" en el subdominio y en la ruta, puede indicar que la entidad detección es una entidad financiera o banca.

Ambigüedades:

• La palabra "banco" no está explícitamente presente en la URL, lo que podría generar confusión.
• La ruta "/particulares" puede referirse a diferentes entidades financieras, no solo a Santander.
• El término "Santander" también puede ser un nombre de persona o lugar, no exclusivamente una entidad financiera.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/fc1d08f1e92f5327005249a01496da74/codigo_incorrecta.php

**detected_entity:** santander

### Output del modelo:

Señales observables:

* santander.banco (subdominio)
* bancosantander.es (ruta)
* particulares (ruta)
* Santander (ruta)

Patrón potencial:
La presencia de "santander" en el subdominio y en la ruta, puede indicar una entidad relacionada con el banco Santander.

Ambigüedades:

• La palabra "Santander" puede referirse a diferentes entidades (banco, empresa, ciudad, etc.).
• La ruta "/bancosantander/es/particulares/Santander/" puede contener tokens irrelevantes para la detección de entidad.
• La presencia de otros tokens en la ruta y subdominio que no estén relacionados con la entidad "Santander" pueden influir en la detección.

---

## URL: https://21321-bbf062.ingress-earth.ewp.live/pagomente/Recibir_paquete.php

**detected_entity:** (vacío)

### Output del modelo:

