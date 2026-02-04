---

**P1 — brand_in_subdomain_of_foreign_domain**  
**Definición:**  
La marca aparece como subdominio, pero el dominio registrado no le pertenece.  
**Evidencia:**  
- bbva.ejemplo.com  
- santander.phishing.net  

---

**P2 — brand_only_in_path**  
**Definición:**  
La marca aparece solo en la ruta (path), no en dominio ni subdominio.  
**Evidencia:**  
- /bbva/login  
- /Santander/particulares/  

---

**P3 — brand_concatenated_with_tokens**  
**Definición:**  
La marca está fusionada con otros tokens sin separadores claros.  
**Evidencia:**  
- bancosantander  
- santanderes  
- appsantandrsms  

---

**P4 — multiple_brand_tokens_present**  
**Definición:**  
Aparecen múltiples marcas distintas en la misma URL.  
**Evidencia:**  
- /bbva/.../santander/...  
- bbva.caixa.fake.com  

---

**P5 — misleading_country_or_tld_usage**  
**Definición:**  
Uso engañoso de país o TLD asociado a la marca sin dominio legítimo.  
**Evidencia:**  
- bbva.es-login.com  
- santander-es.info  

---

**P6 — ambiguous_token_collision**  
**Definición:**  
El token coincide literal, pero es genérico o colisiona semánticamente.  
**Evidencia:**  
- ing  
- orange  

---

**P7 — human_inferred_without_literal_brand**  
**Definición:**  
El humano asigna entidad sin aparición literal válida de la marca.  
**Evidencia:**  
No aparece bbva, santander, etc. en la URL.

---

**P8 — typosquatting_brand_variant**  
**Definición:**  
Variante ortográfica deliberada de la marca (errores mínimos).  
**Evidencia:**  
- sntnder  
- santandr  
- bbvaa  

**Reglas duras:**  
- 1–2 ediciones  
- Sin substring limpio  
- Solo descriptivo (auditor)  

---

**P0 — NO_PATTERN**  
**Definición:**  
No encaja limpiamente en ninguno de los anteriores.

---
Orden de decisión (exclusivo)
P4 — multiple_brand_tokens_present
Si hay ≥2 marcas → P4 y se termina.
P8 — typosquatting_brand_variant
Si parece marca mutada sin substring limpio → P8.
P3 — brand_concatenated_with_tokens
Si la marca aparece completa pero fusionada → P3.
P1 — brand_in_subdomain_of_foreign_domain
Marca como subdominio, dominio ajeno.
P2 — brand_only_in_path
Marca solo en path.
P5 — misleading_country_or_tld_usage
Uso engañoso de país/TLD.
P6 — ambiguous_token_collision
Token genérico/colisión.
P7 — human_inferred_without_literal_brand
Inferencia humana sin literal.
P0 — NO_PATTERN
Nada encaja limpiamente.