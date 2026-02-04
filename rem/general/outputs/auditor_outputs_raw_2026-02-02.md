# Auditor Output - 2026-02-02

**CSV:** cases_eval_v0.csv

---

## URL: https://banco.online.bbva.146-70-81-49.cprapid.com/BBVA-Movil/es/index.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: https, banco, online, bbva, 146-70-81-49, cprapid, com, index.php
2. Patrón potencial: La URL contiene una serie de segmentos que sugieren una estructura de dominio y ruta muy específica, con nombres de subdominios y elementos de la ruta concatenados literalmente. La precisión de la detección depende enteramente de la presencia exacta de estos segmentos.
3. Ambigüedades:
    * La presencia de números IP en el dominio podría generar confusión.
    * La inclusión de "/BBVA-Movil/" podría ser un fragmento aleatorio de la ruta.
    * La extensión ".php" en el segmento final de la ruta podría ser irrelevante.

---

## URL: https://bancosantander.es.hotelparadis.es/aviso/03a253e1ba5bba8/login.php?signin

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: bancosantander.es, hotelparadis.es, aviso, 03a253e1ba5bba8, login, php, signin
2. Patrón potencial: La URL parece estar construida a partir de segmentos de texto literales unidos, lo que sugiere una detección de entidad basada en una lista predefinida de nombres de dominio y rutas.  Es probable que la entidad se identifique mediante la coincidencia exacta de estos segmentos.
3. Ambigüedades:
    *   La presencia de 'hotelparadis.es' podría ser un subdominio, pero la regla solo permite coincidencias exactas de dominio registrado.
    *   La presencia de 'signin' podría ser una parte de la ruta, pero la regla solo permite coincidencias exactas de segmentos completos.
    *   El uso de 'login.php' es una estructura de ruta común pero no proporciona una señal distintiva para la detección de entidad.

---

## URL: https://bancosantander.es.hotelparadis.es/aviso/0f55bee3d3e7298/login.php?signin

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: bancosantander.es, hotelparadis.es, aviso, 0f55bee3d3e7298, login.php, signin
2. Patrón potencial: La URL parece estar estructurada en torno a un identificador (0f55bee3d3e7298) que está vinculado a un recurso (login.php) dentro de un dominio específico (bancosantander.es) y un subdominio (hotelparadis.es).  La presencia de "signin" sugiere una operación de inicio de sesión.
3. Ambigüedades:
    * La concatenación del dominio y subdominio puede generar combinaciones inesperadas.
    * El identificador numérico podría estar relacionado con un recurso específico, pero no de forma predecible.
    * La presencia de "signin" en la ruta podría indicar un flujo de inicio de sesión, pero no necesariamente de un servicio bancario.

---

## URL: https://bancosantander.es.hotelparadis.es/aviso/4ba5494c4c9d091/login.php?signin

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
    - Dominio: bancosantander.es.hotelparadis.es
    - Ruta: aviso
    - Ruta: 4ba5494c4c9d091
    - Ruta: login.php
    - Ruta: signin

2. Patrón potencial: La detección de entidad se basa en una coincidencia exacta de segmentos de la ruta después del dominio. Se identifica la entidad a partir de la presencia de un segmento específico de la ruta.

3. Ambigüedades:
    *   La inclusión de subdominios en el dominio es ignorada.
    *   La presencia de parámetros de consulta en la ruta no aporta información para la detección.
    *   La longitud de los segmentos de la ruta puede variar, lo que podría afectar la coincidencia.

---

## URL: https://bancosantander.es.hotelparadis.es/aviso/bf894657ff192a1/login.php?signin

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: "https", "bancosantander.es", "hotelparadis.es", "/aviso/", "bf894657ff192a1", "login.php", "?signin"
2. Patrón potencial: La URL parece estar construida a partir de segmentos literales, separadas por '/'. La combinación de dominio, segmento de ruta y la cadena '?signin' sugiere un intento de acceder a un formulario de inicio de sesión.
3. Ambigüedades:
    *   La presencia de un subdominio ("hotelparadis.es") podría llevar a resultados inesperados.
    *   La cadena "?signin" es un parámetro estándar, pero no ofrece información específica sobre el tipo de entidad.
    *   La presencia de "login.php" es genérica y no indica directamente la entidad.

---

## URL: https://bancosantander-es-online.preview-domain.com/xx/santa_presi/login

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
    *   bancosantander-es-online.preview-domain.com
    *   /xx
    *   /santa_presi
    *   /login

2. Patrón potencial: La detección de entidad parece basarse en una coincidencia literal exacta de segmentos de la URL. La presencia de `/login` como segmento de ruta es un indicador clave.

3. Ambigüedades:
    *   El uso de "preview-domain.com" sugiere un entorno de prueba.
    *   La presencia de `/xx` es un segmento de ruta sin una entidad conocida.
    *   La ruta contiene nombres de archivos y carpetas, pero no se observa ninguna señal válida según las reglas.

---

## URL: https://bancosantander-firma-es-account-activation-yakuzablyat101350359.codeanyapp.com/online1/particulares/request.php?step=one&id=92481757

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: https://, bancosantander, firma, es, account-activation, yakuzablyat101350359, codeanyapp, particulares, request, step, one, id, 92481757.
2. Patrón potencial: La URL parece estar estructurada alrededor de una serie de segmentos literales, posiblemente nombres de dominio y elementos de una ruta, que se combinan para formar una cadena completa. La presencia de parámetros en la URL (step, id) sugiere un intento de identificar un recurso específico dentro de ese conjunto de segmentos.
3. Ambigüedades:
    * La combinación de elementos de dominio como "bancosantander" y "codeanyapp" parece desordenada.
    * La longitud variable de los segmentos de ruta es inconsistente.
    * La presencia de caracteres alfanuméricos en el nombre de dominio ("yakuzablyat101350359") es atípica.

---

## URL: https://0560db8.wcomhost.com/Caixabank/particulares_es/home/Espera2.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: "https", "0560db8", "wcomhost.com", "Caixabank", "particulares", "es", "home", "Espera2", ".html".
2. Patrón potencial: La URL contiene una serie de segmentos de ruta que parecen componer una estructura jerárquica, dividida por caracteres "/".  La coincidencia exacta de cada segmento sugiere una lógica de detección basada en la presencia literal de estos términos.
3. Ambigüedades:
    *  La presencia de números en el dominio podría ser un factor en la detección.
    *  La combinación de "Caixabank" y "particulares" podría indicar una entidad específica.
    *  La extensión ".html" es un componente común en URLs, pero no aporta información específica de entidad.

---

## URL: https://0560db8.wcomhost.com/Caixabank/particulares_es/home/Espera.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: https://, 0560db8.wcomhost.com, Caixabank, particulares_es, home, Espera.html
2. Patrón potencial: La URL parece estar estructurada alrededor de un dominio registrado, seguido de segmentos de ruta que parecen formar una jerarquía.  La presencia de nombres específicos como "Caixabank" y "particulares_es" sugiere una estructura de ruta basada en una coincidencia exacta.
3. Ambigüedades:
    * La presencia de "0560db8.wcomhost.com" sugiere una dirección IP, que no es una señal esperada bajo las reglas.
    * La ruta contiene varios segmentos que podrían formar diferentes entidades, pero solo aquellos que coinciden exactamente con la lista predefinida son considerados válidos.
    * La extensión de archivo ".html" no contribuye a la detección.

---

## URL: https://0560db8.wcomhost.com/Caixabank/particulares_es/home/Forma.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
   - Dominio: 0560db8.wcomhost.com
   - Caixabank
   - particulares_es
   - home
   - Forma.html

2. Patrón potencial: La detección de entidad parece basarse en la coincidencia exacta de segmentos de la ruta, separadas por el carácter '/'.  El dominio también debe coincidir exactamente.

3. Ambigüedades:
   - La presencia de caracteres numéricos en el dominio podría ser un factor confuso.
   - La longitud variable de los segmentos de ruta podría generar variaciones.
   - La combinación de palabras en español en la ruta introduce un riesgo de error si la lista de coincidencias no es exhaustiva.

---

## URL: https://064f211.wcomhost.com/caixanew/CaixaBank/particular/GPeticionesPN/Es/home/Espera.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
    - Dominio: 064f211.wcomhost.com
    - Ruta: caixanew/CaixaBank/particular/GPeticionesPN/Es/home/Espera.html
    - Protocolo: https
    - Esquema: Es

2. Patrón potencial: El patrón se basa en la coincidencia exacta de segmentos de ruta, lo que indica una estructura jerárquica y posiblemente una navegación dentro del sitio web. La presencia de segmentos cortos y nombres específicos sugiere una identificación basada en la información textual presente en la URL.

3. Ambigüedades:
    - La longitud de los segmentos de ruta puede variar, afectando la precisión de la coincidencia.
    - La combinación de caracteres y palabras en la ruta puede introducir ruido si no se ajusta a la lista cerrada.
    - La falta de normalización de la ruta dificulta la detección de patrones similares a pesar de las diferencias en la escritura.

---

## URL: http://pagos-correos-del.tempurl.host/es/manage/?view=login&appidkey=fcd00c0656cc490&country=

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, pagos-correos-del, tempurl, host, es, manage, login, appidkey, fcd00c0656cc490, country.
2. Patrón potencial: La URL presenta una estructura rígida, con el dominio y segmentos de ruta separados por '/', y los segmentos de ruta representan parámetros explícitos.
3. Ambigüedades:
    * La presencia de `tempurl.host` sugiere una URL temporal y podría afectar la identificación de entidades.
    * El uso de parámetros como `appidkey` y `country` introduce elementos que no contribuyen directamente a la detección.
    * La longitud variable de los segmentos de ruta es inconsistente, lo que puede hacer que la detección dependa de la coincidencia exacta.

---

## URL: http://particulares-bancosantander-es.tempurl.host/es/grupo/home/codigo_incorrecta.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
   - http
   - particulares-bancosantander-es.tempurl.host
   - es
   - grupo
   - home
   - codigo_incorrecta
   - php

2. Patrón potencial: La URL contiene una serie de segmentos de ruta que parecen ser nombres de directorio o archivos en el servidor, separados por '/'. La presencia del identificador 'codigo_incorrecta' sugiere una posible búsqueda o página de error.

3. Ambigüedades:
   - El uso de 'tempurl.host' como dominio puede ser inconsistente.
   - La presencia de 'codigo_incorrecta' podría ser un error o una variable aleatoria.
   - La combinación de segmentos de ruta y el nombre del archivo 'php' no aporta información clara.

---

## URL: http://particulares-santanderes.10web.site/wp-includes/XZlL3dlYi93cC1sa/orange/customer_center/customer-IDPP00C168/login.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, particulares-santanderes, 10web, site, wp-includes, XzLl3dlYi93cC1sa, orange, customer_center, customer-IDPP00C168, login.php
2. Patrón potencial: La URL contiene una serie de segmentos de ruta concatenados, con nombres de directorios y archivos que parecen formar una jerarquía dentro del sitio web. La estructura de la ruta parece indicar un proceso de inicio de sesión específico.
3. Ambigüedades:
    * La presencia de nombres de directorios y archivos específicos dificulta la generalización.
    * La longitud de las cadenas de ruta puede variar significativamente.
    * La combinación de nombres y extensiones de archivo no proporciona información adicional.

---

## URL: http://particulares-santanderes.10web.site/wp-includes/XZlL3dlYi93cC1sa/orange/customer_center/customer-IDPP00C638/login.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: dominio: particulares-santanderes.10web.site, segmento de ruta: wp-includes/XZlL3dlYi93cC1sa/orange/customer_center/customer-IDPP00C638/login.php
2. Patrón potencial: La URL se compone de una concatenación literal de segmentos de ruta, sin ninguna transformación ni simplificación. Esta estructura, basada en una coincidencia exacta, indica una detección de entidad basada en una lista cerrada de rutas.
3. Ambigüedades:
    *  La longitud de los segmentos de ruta varía significativamente.
    *  El uso de caracteres especiales dentro de los segmentos de ruta es común.
    *  La estructura de la ruta no proporciona ninguna indicación sobre el tipo de entidad.

---

## URL: http://ingdirect-acceso.com/app-login

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, ingdirect-acceso, com, app-login
2. Patrón potencial: La URL contiene segmentos literales que definen el dominio y la ruta de la aplicación de inicio de sesión.  La estructura de la URL es consistente con una posible aplicación web.
3. Ambigüedades:
    * El nombre de dominio "ingdirect-acceso" podría ser un indicador, pero no se puede inferir su significado.
    * La ruta "app-login" podría referirse a diferentes funcionalidades dentro de la aplicación.
    * La ausencia de información sobre el protocolo HTTP no afecta la detección.

---

## URL: http://ingdirect-app.com/es

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: dominio: ingdirect-app.com, ruta: /es
2. Patrón potencial: La URL contiene un dominio exacto y un segmento de ruta exacto.  Este patrón sugiere que la entidad detectada está asociada a la información presente en la ruta.
3. Ambigüedades:
    *  El dominio podría representar diferentes regiones o versiones de la aplicación.
    *  La ruta "/es" es un indicador de idioma, pero no es el único posible.
    *  La combinación del dominio y la ruta no es suficiente para determinar la entidad.

---

## URL: http://instagramusicabrasilinstagram.blogspot.com.es

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: instagram, musicabrasil,blogspot,com,es
2. Patrón potencial: La URL parece estar compuesta por múltiples repeticiones de la palabra “instagram” y “musicabrasil” combinadas con un nombre de dominio registrado. Esto sugiere un intento de incluir una variedad de palabras clave para el sistema de detección.
3. Ambigüedades:
    * La inclusión de múltiples instancias de “instagram” puede confundir al sistema.
    * La combinación de nombres de dominio con el nombre de la entidad.
    * La ruta “blogspot” no aporta información útil en el contexto de la detección.

---

## URL: http://caixa-confirmacion-974baa.ingress-florina.easywp.com/mi-cuenta/acceso/es/clients/login.php?verification

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: caixacontraseña, ingress-florina, easywp, mi-cuenta, acceso, clients, login, verification.
2. Patrón potencial: La URL se compone de una serie de segmentos exactos que, al combinarse, sugieren una operación específica dentro de un servicio web. La estructura se basa en una ruta predefinida con parámetros.
3. Ambigüedades:
    * La presencia de ‘easywp’ podría ser un identificador de plataforma.
    * La combinación de segmentos no revela necesariamente el propósito de la URL.
    * La extensión ".php" no proporciona información sobre la entidad.

---

## URL: http://caixma-a7fd59.ingress-daribow.ewp.live/cai/particulares/home

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: caixma-a7fd59, ingress-daribow, ewp, cai, particulares, home
2. Patrón potencial: La URL se compone de una parte del dominio seguida de segmentos de ruta separados por '/'. La detección de entidad se basa en la coincidencia literal exacta de estos segmentos.
3. Ambigüedades:
    * La longitud variable de los segmentos de ruta.
    * La presencia de caracteres especiales en el nombre de dominio.
    * La ausencia de patrones consistentes en la estructura de la ruta.

---

## URL: http://acceso.caixabank.es.theacademy.co.ug/ok/caixa/particular/home/cc/caixa/apl/formularios/altaclientecbk100/index_esf4ef.html

**detected_entity:** caixabank

### Output del modelo:

1. Señales observables:
   - dominio: acceso.caixabank.es.theacademy.co.ug
   - ruta: ok/caixa/particular/home/cc/caixa/apl/formularios/altaclientecbk100/index_esf4ef.html
   -  la URL contiene 'caixabank' como segmento de la ruta.
   - la URL contiene 'caixa' como segmento de la ruta.

2. Patrón potencial: La presencia literal de "caixabank" o "caixa" en la ruta, combinada con el dominio registrado, sugiere una coincidencia exacta para la entidad detectada.

3. Ambigüedades:
   - La presencia de subdominios dentro del dominio registrado no es considerada.
   - La longitud de la ruta no parece ser un factor determinante.
   - La inclusión de caracteres especiales en la ruta no afecta al proceso de detección.

---

## URL: http://loc4.caixabank.es.gpeticiones.weblogicsession.ay-min.az/LaCaixa/home/Espera.html

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables: http, loc4, caixabank, es, gpeticiones, weblogicsession, ay-min, az, LaCaixa, home, Espera, html
2. Patrón potencial: La URL presenta una concatenación de segmentos de dominio y ruta, donde cada segmento es una coincidencia literal exacta. La estructura de la ruta parece seguir una convención específica, con componentes separadas por '/'.
3. Ambigüedades:
    *   La longitud variable de los segmentos de dominio.
    *   El uso de guiones y abreviaturas en los segmentos de dominio.
    *   La presencia de caracteres no alfanuméricos en algunos segmentos de la ruta.

---

## URL: https://autrasistema-ba63ea.ingress-earth.ewp.live/SANTANDER-DRO/home/particulares.php

**detected_entity:** (vacío)

### Output del modelo:

1. Señales observables:
    - dominio: autrasistema-ba63ea.ingress-earth.ewp.live
    - ruta: SANTANDER-DRO/home/particulares.php
2. Patrón potencial: La detección de entidad se basa en la coincidencia literal exacta de segmentos de la ruta. La presencia de "SANTANDER-DRO" en la ruta es un indicador clave.
3. Ambigüedades:
    *  La estructura de la ruta "/home/particulares.php" podría ser utilizada por múltiples entidades.
    *  La presencia de "ingress-earth.ewp.live" en el dominio es específica y podría no ser un indicador universal.
    *  El uso de guiones ("-") en el nombre de dominio y ruta, aunque válido, podría introducir ruido.

