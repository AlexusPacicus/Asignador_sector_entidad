# Auditor Output - 2026-01-30

**CSV:** cases_post_R1_2026-01-29.csv

---

## URL: http://particulares-bancosantander-es.tempurl.host/es/grupo/home/codigo_incorrecta.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, particulares-bancosantander-es, tempurl, host, es, grupo, home, codigo_incorrecta, php.
2. Patrón potencial: La URL parece estar basada en la coincidencia literal de segmentos de ruta, donde cada segmento se evalúa contra una lista predefinida, sin considerar el orden o el significado semántico. La estructura de la URL sugiere una posible segmentación en componentes relacionados con la identidad del dominio y la ruta específica dentro de él.
3. Ambigüedades:
    * La inclusión de “tempurl” y “host” podría indicar un entorno de pruebas o desarrollo.
    * El uso de “codigo_incorrecta” en la ruta podría ser un ejemplo o un valor predeterminado.
    * El nombre de dominio, ‘particulares-bancosantander-es’, es una cadena de texto completa y no presenta caracteres especiales ni abreviaturas que puedan afectar la detección.

---

## URL: http://loc52.caixabank.es.lacaixa.actualizar.information.ay-min.az/soporte-directonow/home/Espera.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: loc52, caixabank, .lacaixa, actualizar, information, ay-min, az, soporte-directonow, home, Espera, html
2. Patrón potencial: La URL contiene una serie de segmentos de dominio y ruta que parecen estar concatenados literalmente. La detección de entidad se basa únicamente en la coincidencia exacta de estos segmentos en una lista predefinida.
3. Ambigüedades:
    * La longitud variable de los segmentos de dominio.
    * La inclusión de guiones en los segmentos de la ruta.
    * La presencia de caracteres especiales en el dominio (loc52).

---

## URL: http://oficinacorreos.page.link/es

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: dominio ('oficinacorreos'), segmento de ruta ('page.link'), esquema ('http'), jerarquía de dominio ('page').
2. Patrón potencial: El patrón general indica que la detección de entidad se basa en una coincidencia exacta del dominio y de un segmento de la ruta, sin considerar la estructura general de la URL.
3. Ambigüedades:
    * La presencia de "page.link" podría ser una señal errónea.
    * La jerarquía de dominio "page" podría ser ambigua.
    * El esquema "http" no aporta información útil para la detección.

---

## URL: https://bbva.es.suspension-tarjeta.com

**detected_entity:** bbva

### Output del modelo:

1. Señales observables:
    *   dominio: bbva.es
    *   segmento de ruta 1: suspension-tarjeta
    *   segmento de ruta 2: com

2. Patrón potencial: La detección de la entidad “bbva” se basa en la coincidencia literal del dominio registrado "bbva.es" con el segmento de ruta "suspension-tarjeta.com". La presencia de “bbva.es” es el indicador principal.

3. Ambigüedades:
    *   La presencia de otros segmentos de ruta, aunque presentes, no contribuyen a la detección.
    *   La extensión ".es" del dominio no es relevante para la detección.
    *   La estructura completa de la URL es necesaria para la detección.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/sms_codigo.php

**detected_entity:** santander

### Output del modelo:

1. Señales observables:
   - Dominio: 000o8dc.wcomhost.com
   - Ruta: www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/sms_codigo.php

2. Patrón potencial: La URL contiene una coincidencia literal exacta del dominio registrado y una coincidencia exacta de la ruta definida. Esto sugiere que la detección de la entidad se basa en la correspondencia directa entre estos componentes.

3. Ambigüedades:
   - La presencia de subdominios en el dominio puede llevar a coincidencias falsas si se permite la coincidencia parcial.
   - La ruta puede contener caracteres especiales o frases que no se consideran en la lista de entidades.
   - La longitud de la ruta podría ser un factor para la detección.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/fc1d08f1e92f5327005249a01496da74/sms_codigo.php

**detected_entity:** santander

### Output del modelo:

1. Señales observables:
    - Dominio: 000o8dc.wcomhost.com
    - Ruta: www.santanderbanco.es/bancosantander/es/particulares/Santander/fc1d08f1e92f5327005249a01496da74/sms_codigo.php

2. Patrón potencial:
    La URL contiene una coincidencia exacta del dominio registrado y una coincidencia exacta de una ruta específica, separada por el carácter '/'. Este patrón indica que la detección de la entidad se basa en una correspondencia literal exacta de estos componentes de la URL.

3. Ambigüedades:
    * La presencia de subdominios en el dominio no se considera.
    * La ruta está compuesta por múltiples segmentos separados por '/'.
    * La longitud de los segmentos de la ruta puede variar.

---

## URL: https://2022-bdaef4.ingress-earth.ewp.live/correos/Recibir_paquete.php

**detected_entity:** correos

### Output del modelo:

1. Señales observables: https, 2022-bdaef4, ingress-earth, ewplive, correos, Recibir_paquete, php
2. Patrón potencial: La URL parece descomponerse en un dominio registrado y una ruta, donde la ruta contiene un nombre de archivo PHP con un nombre específico.
3. Ambigüedades:
    *  La presencia de “ingress-earth.ewp.live” podría ser un dominio específico.
    *  El nombre de archivo “Recibir_paquete.php” es muy específico y podría ser un indicador.
    *  El uso de caracteres especiales en el nombre de archivo (“_”) podría generar confusiones.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/codigo_incorrecta.php

**detected_entity:** santander

### Output del modelo:

1. Señales observables:
    - Dominio: 000o8dc.wcomhost.com
    - Ruta: www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/codigo_incorrecta.php

2. Patrón potencial: La presencia del dominio registrado y una porción significativa de la ruta coinciden exactamente con la cadena especificada. Esto sugiere que la entidad ha sido identificada mediante una coincidencia literal precisa en los componentes de la URL.

3. Ambigüedades:
    *   La inclusión de subdominios en el dominio, aunque no se consideran para la detección, podría introducir confusión.
    *   La longitud de la ruta, con muchos segmentos, podría ser un factor que afecta la precisión de la coincidencia.
    *   El uso de caracteres especiales o no alfanuméricos en la ruta podría generar problemas en la detección.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/fc1d08f1e92f5327005249a01496da74/codigo_incorrecta.php

**detected_entity:** santander

### Output del modelo:

1. Señales observables:
   - dominio: 000o8dc.wcomhost.com
   - ruta: www.santanderbanco.es
   - ruta: bancosantander
   - ruta: es
   - ruta: particulares
   - ruta: Santander
   - ruta: fc1d08f1e92f5327005249a01496da74
   - ruta: codigo_incorrecta.php

2. Patrón potencial: La URL contiene coincidencias literales exactas con segmentos de la ruta, lo que sugiere que la entidad está definida por una lista de segmentos de ruta específicos.  La combinación de estos segmentos indica el nombre del dominio y, presumiblemente, partes de la ruta que se utilizan para identificar la entidad.

3. Ambigüedades:
   - El uso de subdominios (000o8dc) podría confundir la detección.
   - La ruta contiene una serie de segmentos que, en conjunto, podrían ser considerados como una única entidad.
   - La presencia de caracteres especiales en la ruta (“codigo_incorrecta.php”) podría dificultar la coincidencia exacta.

---

## URL: https://21321-bbf062.ingress-earth.ewp.live/pagomente/Recibir_paquete.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: https, 21321, bbf062, ingress-earth, ewplive, pagomente, Recibir_paquete, php
2. Patrón potencial: La URL parece estar estructurada alrededor de un identificador (21321-bbf062) y un segmento de ruta, "Recibir_paquete", lo que sugiere una solicitud específica relacionada con un paquete.
3. Ambigüedades:
    *   La presencia de "ingress-earth" y "ewplive" es inusual y podría ser un identificador de dominio específico.
    *   El nombre del archivo "Recibir_paquete.php" no proporciona información directa sobre la entidad.
    *   La combinación de segmentos de ruta es específica y no es un patrón común.

---

## URL: http://particulares-santanderes.10web.site/wp-includes/XZlL3dlYi93cC1sa/orange/customer_center/customer-IDPP00C168/login.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, particulares-santanderes, 10web, site, wp-includes, XzLl3dlYi93cC1sa, orange, customer_center, customer-IDPP00C168, login.php
2. Patrón potencial: La URL contiene una serie de segmentos de ruta con nombres de directorios y archivos, separados por '/'. La combinación específica de estos segmentos parece ser la señal principal para la detección de la entidad.
3. Ambigüedades:
    * La presencia de "wp-includes" podría ser una señal confusa.
    * La inclusión de caracteres especiales en los nombres de directorios y archivos podría dificultar la detección.
    * El nombre del archivo "login.php" no aporta una información específica para la entidad.

---

## URL: https://3476-1-bce161.ingress-baronn.ewp.live/pagomente/Recibir_paquete.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
   - Dominio: 3476-1-bce161.ingress-baronn.ewp.live
   - Ruta: pagomente/Recibir_paquete.php

2. Patrón potencial: La URL contiene un dominio y una ruta que se separan por una barra. La ruta consiste en una serie de segmentos separados por "/".  La forma en que se construyen estos segmentos (dominio y ruta) podría ser un indicador del tipo de entidad que se está detectando.

3. Ambigüedades:
   * La longitud del dominio no proporciona información útil.
   * La ruta contiene palabras que podrían ser clave, pero no es suficiente para determinar la entidad.
   * No se observa ninguna señal válida según las reglas.

---

## URL: http://particulares-bancosantander-es.tempurl.host/es/grupo/home/codigo_incorrecta.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
    - dominio: particulares-bancosantander-es.tempurl.host
    - ruta: es/grupo/home/codigo_incorrecta.php
2. Patrón potencial: La detección de entidad se basa en la coincidencia exacta de segmentos de la ruta con una lista predefinida.  La estructura de la ruta, con sus divisiones por '/' y la presencia de "es" y "home", parece ser el factor determinante para la detección.
3. Ambigüedades:
    *   La extensión ".php" no aporta información relevante.
    *   La inclusión de "tempurl.host" en el dominio puede generar falsos positivos si está en la lista.
    *   La cadena "codigo_incorrecta" es una coincidencia literal y no ofrece información semántica.

---

## URL: http://particulares-santanderes.10web.site/wp-includes/XZlL3dlYi93cC1sa/orange/customer_center/customer-IDPP00C638/login.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, particulares-santanderes, 10web, site, wp-includes, XzLl3dlYi93cC1sa, orange, customer_center, customer-IDPP00C638, login.php
2. Patrón potencial: La URL contiene una serie de segmentos de ruta que, al ser extraídos y concatenados, conforman una ruta compleja.  Esta estructura parece estar definida por componentes específicos, sin intentar inferir un significado general.
3. Ambigüedades:
    * La presencia de nombres de archivos y carpetas (wp-includes, orange) podría generar confusión.
    * La concatenación de caracteres especiales y números en la ruta.
    * La longitud y estructura de los segmentos de ruta dificultan la identificación de patrones.

---

## URL: https://bienvenido-a-correoses-c251aa.ingress-erytho.ewp.live/wp-includes/certificates/cs/Recibir_paquete.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: https, bienvenido-a-correoses, ingress-erytho, ewｐ.live, wp-includes, certificates, cs, Recibir_paquete, php
2. Patrón potencial: La URL contiene una concatenación de segmentos de dominio y ruta, separados por "/", que corresponde a un segmento específico del dominio. La estructura de la ruta sugiere un posible archivo PHP relacionado con certificados dentro de un entorno de WordPress.
3. Ambigüedades:
    * La presencia de caracteres no alfanuméricos (ewｐ) en el dominio.
    * La ruta incluye un nombre de archivo con guiones y caracteres especiales.
    * El nombre del dominio contiene un segmento que podría ser parte de un nombre de producto o servicio.

---

## URL: https://appsantandrsms-b9501c.ingress-daribow.ewp.live/wp-admin/user/SANTANDER/es/clients/login.php?%22santander%22

**detected_entity:** santander

### Output del modelo:

1. Señales observables: https, appsantandrsms-b9501c, ingress-daribow, ew.live, wp-admin, user, SANTANDER, es, clients, login.php, %22santander%22.
2. Patrón potencial: La presencia literal de “SANTANDER” en el segmento de ruta, junto con la presencia literal de “santander” en la cadena de consulta, sugiere que la entidad detectada, "santander", está siendo identificada a través de una coincidencia exacta de texto.
3. Ambigüedades:
    * La presencia de "wp-admin" indica un contexto administrativo, pero no es directamente indicativo de la entidad.
    * El uso de "%22santander%22" en la cadena de consulta podría ser una forma de detección, pero no proporciona información adicional sobre la entidad.
    * La longitud variable de la ruta afecta a la posibilidad de encontrar coincidencias literales exactas.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/Mi_cuenta.php

**detected_entity:** santander

### Output del modelo:

1. Señales observables:
   - dominio: 000o8dc.wcomhost.com
   - ruta: www.santanderbanco.es
   - ruta: bancosantander
   - ruta: es
   - ruta: particulares
   - ruta: Santander
   - ruta: 14a6aa73533e725206d52204cb133ae4
   - ruta: Mi_cuenta.php

2. Patrón potencial: La URL contiene una serie de segmentos de ruta que coinciden exactamente con cadenas literales específicas. La presencia de "Santander" y "bancosantander" en la ruta parece ser un indicador clave de la entidad detectada.

3. Ambigüedades:
   - La presencia de subdominios en el dominio podría generar falsos positivos.
   - La estructura de la ruta con múltiples segmentos podría ser utilizada por otros sitios web.
   - La inclusión de caracteres alfanuméricos en la ruta podría confundir la detección.

---

## URL: http://ing.es-misaccesos.info/loginon.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, ing, es-misaccesos, info, loginon, .php
2. Patrón potencial: La URL contiene una combinación específica de elementos de dominio y ruta que parecen ser una dirección de login. La presencia de "loginon.php" sugiere un script relacionado con el inicio de sesión.
3. Ambigüedades:
    * La extensión ".php" es común y no proporciona información específica.
    * La subdominio "es-misaccesos" es una cadena literal.
    * La combinación de "ing" con el resto de la URL es una señal única.

---

## URL: https://000o8dc.wcomhost.com/www.santanderbanco.es/bancosantander/es/particulares/Santander/14a6aa73533e725206d52204cb133ae4/firma_electronica.php

**detected_entity:** santander

### Output del modelo:

1. Señales observables: https://, 000o8dc.wcomhost.com, www.santanderbanco.es, bancosantander, es, particulares, Santander, 14a6aa73533e725206d52204cb133ae4, firma_electronica.php
2. Patrón potencial: La URL contiene una coincidencia exacta del dominio registrado seguida de segmentos de ruta que incluyen la palabra "Santander" y un identificador único. Esto sugiere que la entidad detectada (santander) está asociada con esta combinación específica de elementos de la URL.
3. Ambigüedades:
    * La presencia de subdominios (000o8dc.wcomhost.com) no es un factor en la detección.
    *  La longitud del identificador único (14a6aa73533e725206d52204cb133ae4) es irrelevante.
    * El segmento de ruta "firma_electronica.php" no aporta información adicional.

---

## URL: http://kbv.dnz.mybluehost.me/wp-admin/correos.es/servicios.paquete/pagomente/Recibir_paquete.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: kbv, dnz, mybluehost, me, wp-admin, correos, es, servicios, paquete, pagomente, Recibir_paquete, php
2. Patrón potencial: La URL contiene una concatenación literal de segmentos de ruta, cada uno de los cuales parece ser un componente de una dirección. La estructura sugiere un intento de identificar una página específica dentro de un sitio web a través de una ruta jerárquica.
3. Ambigüedades:
    *   La presencia de "wp-admin" podría indicar una página de administración.
    *   La combinación de términos como "servicios.paquete" y "pagomente" podría referirse a un servicio específico o una funcionalidad.
    *   El uso de ".php" al final de la URL sugiere un script dinámico.

---

## URL: http://ing.es-accesospanel.info/loginon.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, ing, es-accesospanel, info, loginon, php
2. Patrón potencial: La URL parece componerse de un protocolo, un dominio con un segmento de ruta, y un nombre de archivo .php. La detección de entidad se basa en la coincidencia exacta de estos componentes.
3. Ambigüedades:
    * La extensión .php podría ser una pista, pero no es utilizada en la detección.
    * El segmento 'ing' podría ser parte del nombre de dominio, pero se verifica como literal.
    * La combinación de 'es-accesospanel' con 'loginon' es la clave para la detección.

---

## URL: https://dhl-express-hfmxgobkwmqdbxefarqqying.pages.dev

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: dhl-express, pages, dev
2. Patrón potencial: La URL contiene fragmentos del nombre de dominio, lo que sugiere una coincidencia literal con el registro del dominio.
3. Ambigüedades:
    *   La presencia de "pages.dev" podría indicar un entorno de desarrollo o pruebas.
    *   El nombre de dominio es muy específico, lo que podría llevar a una coincidencia incorrecta si el registro se actualiza.
    *   La ruta es muy corta, lo que podría ser un indicador de que el patrón se basa en la coincidencia exacta.

---

## URL: https://banco.online.bbva.146-70-81-49.cprapid.com/BBVA-Movil/es/index.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: banco, online, bbva, cprapid, es, index, php
2. Patrón potencial: La URL parece estar compuesta por un dominio y una ruta, donde los segmentos de la ruta son identificadores literales que se utilizan para identificar el recurso solicitado. La estructura es consistente en utilizar elementos separados por '/'.
3. Ambigüedades:
    *   La presencia de un IP en el dominio podría generar confusión.
    *   El uso de caracteres especiales en la URL (como el número '146-70-81-49') es un factor que podría ser problemático.
    *   La ruta contiene múltiples segmentos que podrían ser relevantes, pero no permiten inferir ninguna entidad específica.

---

## URL: https://bbva.es.id8261.info/usuario

**detected_entity:** bbva

### Output del modelo:

1. Señales observables: https, bbva, es, id8261, info, usuario
2. Patrón potencial: La URL contiene una coincidencia exacta de "bbva" en el dominio y un segmento de ruta. Esta combinación de componentes apunta a una detección basada en coincidencias literales simples.
3. Ambigüedades:
    * La presencia de "es" podría indicar una variante geográfica.
    * La cadena "id8261" no aporta información útil para la detección.
    * La extensión del dominio "info" es genérica.

---

## URL: https://bbva.es.personal-cuenta.info/personal/index.php?tegdfs?

**detected_entity:** bbva

### Output del modelo:

1. Señales observables: https, bbva.es, personal-cuenta, info, personal, index.php, tegdfs
2. Patrón potencial: La URL presenta un dominio exacto ("bbva.es") seguido de segmentos de ruta que, al combinarse, forman parte de la entidad detectada ("bbva"). La presencia de "personal-cuenta" parece indicar una subruta específica.
3. Ambigüedades:
    *   La presencia de "tegdfs" en la ruta no aporta información útil para la detección.
    *   La ruta incluye caracteres no alfanuméricos, lo cual podría ser una señal pero no es explícitamente manejada.
    *   La combinación de elementos en la ruta podría ser significativa, pero no se considera en la detección.

---

## URL: https://bancaonline-bancosantander-es.com/particulares.gruposantander.es/SUPFPA_ENS/sms1.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: bancaonline, bancosantander, es, particulares, gruposantander, SUPFPA, ENS, sms1, html
2. Patrón potencial: La URL contiene una secuencia de cadenas que, al ser coincidentes literalmente, parecen ser identificadores únicos o nombres de archivo dentro de un dominio. El dominio y subdominios aparentemente forman un identificador, seguido de segmentos de ruta que también se presentan de manera literal.
3. Ambigüedades:
    * La presencia de "SUPFPA_ENS" es inusual y podría ser un identificador de flujo.
    * La combinación de "sms1.html" sugiere un archivo relacionado con SMS.
    * El uso de subdominios parece ser un patrón recurrente en la estructura de la URL.

---

## URL: https://bancaonline-bancosantander-es.com/particulares.gruposantander.es/SUPFPA_ENS/sms.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: bancaonline, bancosantander, es, particulares, gruposantander, SUPFPA, ENS, sms, html
2. Patrón potencial: La URL contiene una secuencia de segmentos de ruta, cada uno de los cuales es una cadena literal. La combinación de estos segmentos parece definir un recurso específico dentro de la estructura de dominio.
3. Ambigüedades:
    * La presencia de nombres de subdominios puede complicar el análisis.
    * La longitud variable de los segmentos de ruta introduce incertidumbre.
    * El uso de acrónimos y códigos internos podría afectar la precisión.

---

## URL: https://banco.online.bbva.146-70-81-49.cprapid.com/BBVA-Movil/es/index.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: banco, online, bbva, cprapid, es, index, php
2. Patrón potencial: La URL parece estar estructurada en torno a un dominio registrado y una ruta que incluye segmentos separados por '/'. La combinación específica de estas palabras clave sugiere un intento de identificar la entidad basándose en la coincidencia literal de estos componentes.
3. Ambigüedades:
    * La presencia de números IP en el dominio dificulta la detección.
    * El uso de caracteres mayúsculas y minúsculas es uniforme, lo que simplifica la coincidencia.
    * La ruta contiene varias palabras clave, lo que podría aumentar la complejidad si no se realiza una coincidencia exacta.

---

## URL: https://bancosantander-firma-es-account-activation-yakuzablyat101350359.codeanyapp.com/online1/particulares/request.php?step=one&id=92481757

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: “bancosantander”, “firma”, “es”, “account-activation”, “codeanyapp”, “online1”, “particulares”, “request.php”, “step”, “one”, “id”, “92481757”.
2. Patrón potencial: La URL contiene una serie de segmentos de ruta que parecen formar parte de una URL de código fuente PHP, lo que sugiere que el objetivo principal es la interacción con un script en línea.  La concatenación de palabras clave en la URL podría indicar una acción específica relacionada con una cuenta o un proceso de activación.
3. Ambigüedades:
    * La inclusión de "codeanyapp" sugiere el uso de una plataforma de desarrollo en línea.
    * El uso de “particulares” podría indicar un segmento específico de una cuenta.
    * La presencia de un identificador numérico ("92481757") podría ser un identificador de usuario o de transacción.

