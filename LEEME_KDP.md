# Guía Maestra de Publicación en Amazon KDP

Todos los paquetes de publicación para **"Mi Amigo Jesucristo"** están generados y listos en sus carpetas correspondientes.

---

## 📁 Archivos Listos para Subir a KDP

### 1. Formato Kindle (eBook)
* **Archivo de Interior**: [`output/epub/mi_amigo_jesucristo_es.epub`](file:///Users/fjbanezares/libro%20sobre%20mi%20amigo%20Jesucristo/output/epub/mi_amigo_jesucristo_es.epub)
* **Portada para Kindle**: [`content/images/cover_kdp.png`](file:///Users/fjbanezares/libro%20sobre%20mi%20amigo%20Jesucristo/content/images/cover_kdp.png) (o `cover_kdp_backup_mararel.png`)
* *Nota*: El archivo EPUB 3 ya incluye la portada y metadatos integrados, pero KDP te solicitará subir también la imagen de portada en formato JPG/PNG durante el paso de contenido.

### 2. Formato Tapa Blanda (Paperback)
* **Archivo de Interior PDF**: [`output/latex/libro_kdp_es.pdf`](file:///Users/fjbanezares/libro%20sobre%20mi%20amigo%20Jesucristo/output/latex/libro_kdp_es.pdf)
* **Tamaño de corte (Trim Size)**: A5 (14,8 x 21,0 cm) o estándar 6" x 9"
* **Número de páginas**: 53 páginas (supera el mínimo de 24 págs).
* **Opciones de impresión**: Tinta negra o estándar a color en papel blanco/crema. Sin sangría (No bleed).

### 3. Formato Tapa Dura (Hardcover)
* **Archivo de Interior PDF**: [`output/latex/libro_kdp_tapa_dura_es.pdf`](file:///Users/fjbanezares/libro%20sobre%20mi%20amigo%20Jesucristo/output/latex/libro_kdp_tapa_dura_es.pdf)
* **Tamaño de corte (Trim Size)**: 5.5" x 8.5" (13,97 x 21,59 cm)
* **Número de páginas**: 75 páginas (cumple estrictamente el **mínimo exigido de 75 páginas** para Tapa Dura en Amazon KDP).
* **Opciones de impresión**: Tapa dura con brillo o mate. Sin sangría (No bleed).

---

## 📝 Datos para Copiar y Pegar en Amazon KDP

### Paso 1: Detalles del Libro

* **Idioma**: Español
* **Título del libro**: Mi Amigo Jesucristo
* **Subtítulo**: *Una guía cuántica para el alma moderna*
* **Serie**: *(Dejar en blanco)*
* **Número de edición**: *(Dejar en blanco)*

---

### Paso 2: Autor y Colaboradores

* **Autor Principal**:
  * **Nombre**: A Glimpse of
  * **Apellidos**: Light
* **Colaborador / Ilustrador**:
  * **Nombre**: Maria Paz
  * **Apellidos**: Arés Osset
  * **Función**: Ilustrador / Coautor

---

### Paso 3: Descripción del Libro (Formato HTML para Amazon)

Copia y pega este texto exacto en el cuadro de "Descripción":

```html
<b>¿Y si Jesús no te pidiera adoración, sino que "vibraras alto"?</b><br><br>

Imagina que caminas por la Gran Vía de Madrid y te encuentras con un hombre en vaqueros y zapatillas. No te juzga. No te sermonea. Simplemente te invita a sentarte en un banco y te explica que el <b>Reino de los Cielos</b> no es un lugar lejano al que vas cuando mueres, sino una frecuencia de onda que puedes sintonizar aquí y ahora.<br><br>

En <i>Mi Amigo Jesucristo</i>, la espiritualidad se encuentra con la <b>física cuántica</b>. A través de diálogos entrañables y reveladores que transcurren entre el bullicio de Madrid, la calma de Las Rozas y la naturaleza de Colmenarejo, descubrirás una interpretación revolucionaria del mensaje de Cristo:<br><br>

<ul>
<li><b>El Padre Nuestro</b> no como un rezo repetitivo, sino como un manual de instrucciones para elevar tu frecuencia vibratoria.</li>
<li><b>La Tentación</b> explicada como la fuerza de gravedad de las emociones densas (miedo, ira, tristeza).</li>
<li><b>El Perdón</b> como la única herramienta física para romper los lazos cuánticos que nos atan al sufrimiento.</li>
<li><b>La Fe</b> entendida como la certeza de que el observador crea la realidad.</li>
</ul>

Este no es un libro religioso tradicional. Es un viaje interior para el buscador moderno que intuye que la ciencia y la fe son dos lenguajes distintos para explicar la misma Luz. Escrito bajo el seudónimo <b>A Glimpse of Light</b> con arte y música original de <b>Maria Paz Arés Osset</b>, esta obra es una invitación urgente a dejar de buscar fuera y empezar a sintonizar dentro.<br><br>

<b>Atrévete a redescubrir al Maestro. Atrévete a encender tu propia luz.</b>
```

---

### Paso 4: Palabras Clave (Keywords - 7 campos)

1. Espiritualidad cuántica
2. Jesús moderno
3. Crecimiento personal y fe
4. Metafísica cristiana
5. Física cuántica y Dios
6. Novela espiritual
7. Ley de la atracción bíblica

---

### Paso 5: Categorías Recomendadas

* **Categoría 1**: No Ficción / Ficción > Religiosa o Espiritual > Crecimiento Espiritual
* **Categoría 2**: Cuerpo, Mente y Espíritu > Espiritualidad > General
* **Categoría 3**: Religión y Filosofía > Cristianismo > Meditación y Oración

---

### Paso 6: Derechos y Precios (Paso 3 de KDP)

* **Derechos**: "Poseo los derechos de publicación necesarios".
* **ISBN**: Selecciona "Asignar un ISBN de KDP gratuito" para Tapa Blanda y Tapa Dura (o usa tu propio ISBN si dispones de él).
* **Territorios**: Todos los territorios (derechos mundiales).
* **Precio sugerido**:
  * **Kindle eBook**: 2,99 € - 4,99 € (Regalías 70%)
  * **Tapa Blanda (Paperback)**: 9,90 € - 12,90 €
  * **Tapa Dura (Hardcover)**: 16,90 € - 19,90 €

---

## 🛠️ Cómo Regenerar los Paquetes en el Futuro

Si modificas el texto o añades nuevos capítulos:
```bash
# 1. Regenerar PDFs de LaTeX (Tapa Blanda y Tapa Dura)
python3 generate_kdp_bundle.py && cd output/latex && pdflatex -interaction=nonstopmode libro_kdp_es.tex && pdflatex -interaction=nonstopmode libro_kdp_tapa_dura_es.tex

# 2. Regenerar eBooks EPUB para Kindle
python3 scripts/build_epub.py
```

