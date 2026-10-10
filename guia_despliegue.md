# Guía de Despliegue Web: Ramas Huérfanas (Orphan) y Clones Superficiales (Shallow)

Esta guía documenta en detalle la arquitectura y la estrategia de despliegue utilizada para publicar la versión web HTML del libro en el servidor de producción (IONOS), reduciendo drásticamente el peso del repositorio `.git` y manteniendo el servidor limpio de archivos innecesarios (LaTeX, ePub, borradores, herramientas internas).

---

## 1. Fundamentos: ¿Cómo funciona Git bajo el capó?

### Instantáneas (*Snapshots*), no deltas
Una confusión frecuente al usar Git es creer que almacena "las diferencias línea a línea" (deltas) entre un commit y el siguiente. En realidad:
- **Cada commit es una foto completa (*snapshot*)** del estado del Working Directory en ese instante.
- A nivel interno, Git crea objetos:
  - **Blobs:** el contenido puro de cada archivo comprimido.
  - **Trees:** la estructura de directorios (carpetas) que asocia nombres de archivos con sus correspondientes Blobs.
  - **Commits:** un objeto que contiene autor, fecha, mensaje, el puntero al árbol raíz (*Tree*) y el puntero al commit padre (*Parent*).
- Si un archivo no cambia entre commits, el nuevo Tree simplemente reutiliza el Blob anterior (ahorro de espacio).
- Sin embargo, en un repositorio normal con cientos de commits, el directorio `.git` acumula **todas las fotos históricas** de todos los archivos que alguna vez existieron (incluyendo borradores pesados, imágenes sustituidas o PDFs generados). Por esa razón tu `.git` pesaba más de 72 MB.

### ¿Qué es una rama huérfana (`orphan`)?
Normalmente, al crear una rama con `git checkout -b nueva-rama`, esta hereda todo el árbol genealógico anterior. Su commit inicial tiene como padre el commit donde te encontrabas.

Una rama **`--orphan`** es una rama **desconectada** del árbol principal:
- **Cero ancestros:** Su primer commit no tiene commit padre (*Parent*). Es una nueva raíz independiente dentro del mismo repositorio de Git.
- **Aislamiento total:** No arrastra el peso del historial de `main` (capítulos antiguos, versiones anteriores de imágenes, archivos LaTeX o ePub compilados).

```
[main]  C1 ---> C2 ---> C3 ---> C4  (Historial completo de redacción y código fuente)
                                     
[web]   W1                          (Rama huérfana: 1 único commit raíz sin pasado)
```

### ¿Qué es un clon superficial (`shallow clone`) con `--depth 1`?
Cuando ejecutas en el servidor:
```bash
git clone --depth 1 -b web <URL_REPOSITORIO> .
```
Le indicas a Git: *"Descarga únicamente la foto actual de la punta de la rama (`HEAD`), ignorando cualquier ancestro o historial hacia atrás"*.

**Implicaciones:**
1. **Transferencia mínima:** Solo viajan por la red los objetos indispensables para materializar esa foto exacta.
2. **Espacio en disco mínimo:** El directorio `.git` en el servidor no almacena historial, pesando unos pocos kilobytes en metadatos.
3. **El peso restante:** Si la web en IONOS ocupa ~36 MB, se debe casi al 100% al contenido estático multimedia (`images/` pesa 34 MB). Es decir: **ahora el servidor solo almacena lo estrictamente necesario para que la web funcione**.

---

## 2. Lo que hicimos (Paso a Paso)

1. **Asegurar el trabajo en `main`:**
   ```bash
   git push origin main
   ```
2. **Copiar el artefacto compilado a un directorio temporal:**
   ```bash
   cp -r output/html /tmp/libro_web_temp
   ```
3. **Crear la rama huérfana desconectada:**
   ```bash
   git checkout --orphan web
   ```
4. **Limpiar el índice y el directorio de trabajo en esta rama:**
   ```bash
   git rm -rf .
   ```
5. **Colocar los archivos finales en la raíz:**
   ```bash
   cp -r /tmp/libro_web_temp/. .
   rm -rf /tmp/libro_web_temp
   ```
6. **Crear el commit fundacional:**
   ```bash
   git add .
   git commit -m "Publicación estática para servidor web"
   ```
7. **Subir la rama al remoto:**
   ```bash
   git push -u origin web
   ```
8. **Volver a la rama de desarrollo:**
   ```bash
   git checkout main
   ```

---

## 3. Desmitificando los Comandos "Extraños"

### A) La secuencia de extracción desde `main`:
```bash
git checkout main -- output/html
mv output/html/* .
rm -rf output
```

A primera vista resulta chocante ver `git checkout` usado de esta forma mientras estás en la rama `web`. ¿Por qué funciona así?

1. **La doble personalidad de `git checkout`:**
   - Sin argumentos o con `-b` (`git checkout main`), cambia la rama activa completa y mueve `HEAD`.
   - Con el delimitador `-- <ruta>` (`git checkout main -- output/html`), **no cambia de rama**. Funciona como un comando de restauración o extracción puntual: le pide a Git *"Ve al commit de `main`, copia la carpeta `output/html` tal como estaba allí, y tráela a mi Working Directory actual y a mi Staging Area"*.
2. **Por qué se necesita `mv output/html/* .`:**
   - En `main`, esa carpeta se llama `output/html`. Git respeta esa ruta relativa al extraerla.
   - Pero en el servidor web (IONOS), el servidor HTTP (Apache/Nginx) sirve los archivos desde la raíz pública (`/var/www/vhosts/...` o `public_html/`). El archivo de entrada debe ser `./index.html`, no `./output/html/index.html`.
   - El comando `mv` "eleva" (*hoisting*) todo el contenido (archivos HTML, CSS, carpeta `images/`) a la raíz `.`.
3. **Por qué `rm -rf output`:**
   - Una vez vaciada la carpeta `output/`, queda como un cascarón residual. Con `rm -rf output` la eliminamos para que el árbol quede completamente limpio.

---

### B) ¿Qué es y qué implica `git commit --amend`?

En Git, **los commits son inmutables**. Cada commit tiene un hash SHA (por ejemplo `faeade5...`) calculado a partir de:
- El hash del árbol de archivos (*Tree*).
- El hash del commit padre (*Parent*).
- El autor, el mensaje y la marca de tiempo (*Timestamp*).

Por tanto, **es imposible modificar un commit existente**. Lo que hace `--amend` es:
1. Toma los cambios que tengas en el Staging Area (`git add .`).
2. Crea **un commit totalmente nuevo**, con un nuevo hash SHA.
3. Asigna a este nuevo commit el mismo padre que tenía el commit anterior (en nuestro caso, ninguno, porque es huérfano).
4. Mueve el puntero de la rama `web` hacia este nuevo commit.
5. El commit viejo queda abandonado (*dangling object*) en el reflog local y eventualmente el recolector de basura de Git lo eliminará.

**Efecto práctico en nuestra rama `web`:**
Mantiene la rama con **exactamente 1 solo commit de longitud perpetua**. Cada actualización no añade un eslabón a la cadena: sustituye la foto por una nueva foto fresca.

---

### C) `git push --force`: Implicaciones y por qué aquí es seguro

El comando `git push --force` tiene fama de peligroso por una razón justificada:
- Si haces `--force` en `main`, donde colaboran personas o donde guardas el historial del libro, sobrescribes la historia remota. Si alguien tenía cambios basados en el commit anterior, su historial se rompe (*divergent branch*).

**Por qué en la rama `web` es la estrategia idónea:**
- La rama `web` **no es una rama de desarrollo colaborativo**. Es un **artefacto de entrega (*build delivery artifact*)**, igual que un archivo `.zip` o un paquete de instalación.
- No hay programadores trabajando en `web`. Solo hay un servidor descargando archivos estáticos.
- Hacer `--force` en `web` garantiza que en GitHub la rama `web` nunca acumule decenas de megabytes de versiones viejas de imágenes o textos desfasados.

---

### D) ¿Por qué en IONOS usamos `fetch` + `reset --hard` en vez de `git pull`?

Cuando en local aplicas la estrategia de foto única con `--amend` y `push --force`:
- El hash del commit en el remoto cambia (de `hash_A` pasa a `hash_B`).
- Si en IONOS intentas hacer un simple `git pull`:
  - `git pull` equivale a `git fetch` + `git merge`.
  - Como `hash_B` no desciende directamente de `hash_A` (porque reescribiste la historia), Git detecta que los historiales han divergido.
  - En el mejor de los casos fallará con un error (*"Updates were rejected"* o *"refusing to merge unrelated histories"*). En el peor, creará un commit de mezcla (*Merge commit*) que romperá la naturaleza ligera del shallow clone.

**La solución limpia y determinista:**
```bash
git fetch --depth 1 origin web
git reset --hard origin/web
```
1. **`git fetch --depth 1 origin web`:** Descarga únicamente la nueva foto remota (`origin/web`) sin tocar aún los archivos del servidor.
2. **`git reset --hard origin/web`:** Fuerza a la rama local del servidor a apuntar directamente al nuevo commit, y actualiza el Working Directory para que sea un **espejo exacto** de la nueva versión. Cualquier archivo viejo que ya no exista en el libro se elimina automáticamente, y cualquier archivo modificado se actualiza.

---

## 4. Teoría Profunda de `git reset`: Los Tres Árboles y sus 7 Usos

### A) La Arquitectura de los Tres Árboles
Para entender qué hace `git reset` bajo el capó, hay que comprender que Git gestiona simultáneamente tres áreas o estados:
1. **`HEAD`**: El puntero al commit activo en el que estás situado en tu historia.
2. **El `Index` (o *Staging Area*)**: La foto preparada que se incluirá en el próximo commit.
3. **El `Working Directory`**: Los archivos físicos reales que ves y editas en tu carpeta de trabajo.

### B) La Esencia Teórica de `reset`: Mover la Aguja del Tocadiscos
En Git, un commit avanza la rama hacia adelante. **`git reset <commit>` hace exactamente lo contrario: mueve la aguja del tocadiscos hacia el commit que tú le digas.**

La pregunta clave es: cuando mueves la aguja hacia atrás, ¿qué haces con el disco y con lo que estabas escuchando? Ahí entran las tres modalidades de `reset`:

| Tipo de reset | Mueve `HEAD` | Actualiza el `Index` (Staging) | Modifica el `Working Directory` | Equivalencia conceptual |
| :--- | :---: | :---: | :---: | :--- |
| **`--soft`** | **SÍ** | NO | NO | *"Deshaz el commit, pero déjame todo listo en verde para volver a hacer commit"*. |
| **`--mixed`** *(defecto)*| **SÍ** | **SÍ** | NO | *"Deshaz el commit y el `git add`, pero no me borres nada del código"*. |
| **`--hard`** | **SÍ** | **SÍ** | **SÍ** | *"Teletranspórtame al 100% a ese commit y destruye cualquier cambio posterior"*. |

En nuestro caso en IONOS (`git reset --hard origin/web`), equivale teóricamente a:
> **"Obliga a mi servidor a ser un espejo ciego y milimétrico de la foto remota, sin importar qué diferencias hubiera antes".**

### C) ¿Solo se usa tras un `push --force` o tiene otros usos?
**No, para nada.** El caso de sincronizar tras un `--force` es solo una de sus aplicaciones. `git reset` es uno de los comandos más versátiles y nucleares de Git. Aquí tienes sus **7 usos principales**:

1. **Sacar archivos de la sala de espera (Deshacer un `git add`):**
   ```bash
   git reset archivo_secreto.txt
   ```
   Saca el archivo del Staging Area sin tocar ni borrar nada de tu disco.

2. **"Hice commit demasiado pronto" (`git reset --soft HEAD~1`):**
   Deshace el último commit pero **conserva todos tus cambios preparados en el Staging Area**. Ideal para retocar el commit o agregar un archivo olvidado antes de volver a confirmar.

3. **Descomponer un commit grande en commits más pequeños (`git reset HEAD~1`):**
   Deshace el commit y deja los archivos modificados en disco sin preparar. Permite hacer `git add` selectivo y dividir el trabajo en commits ordenados.

4. **Tirar a la basura un experimento fallido (`git reset --hard HEAD`):**
   Borra al instante todos los cambios locales no guardados y devuelve el proyecto a la última foto limpia confirmada.

5. **Volver a un punto seguro del pasado (Viaje en el tiempo):**
   ```bash
   git reset --hard <hash_commit>
   ```
   Mueve la rama actual al estado exacto en que estaba hace días, descartando todo lo posterior.

6. **Rescatar commits perdidos con `git reflog`:**
   Si por error hiciste un `reset --hard` y borraste algo que sí querías, ejecutas `git reflog`, localizas el commit previo y haces `git reset --hard HEAD@{n}` para resucitarlo.

7. **Sincronización espejo con el servidor (Nuestro caso en IONOS):**
   Cuando un entorno de producción solo debe reflejar un artefacto final sin historial local propio, `fetch` + `reset --hard` garantiza que el servidor jamás sufra conflictos de mezcla (*merge conflicts*), archivos residuales o desajustes de versiones.

---

## 5. La Filosofía "A las bravas": Tags como Anclas de la Historia

Tu planteamiento es sumamente acertado:
> *"Con los tags podemos generar cualquier edición del libro cuando queramos, así que ir a las bravas me parece la mejor estrategia."*

### Separación de Responsabilidades:
1. **Rama `main` + Tags = La Memoria Histórica:**
   - Aquí reside el alma del libro: los textos fuente, LaTeX, scripts, borradores y traducciones.
   - Cada vez que cierres una edición o cambio relevante, creas un tag:
     ```bash
     git tag -a v1.0.0 -m "Primera edición completa del libro"
     git push origin v1.0.0
     ```
   - Gracias a los tags, en cualquier momento en el futuro puedes hacer `git checkout v1.0.0`, ejecutar `python scripts/build.py` y reconstruir el HTML exacto de ese día.
2. **Rama `web` = La Pantalla de Proyección Efímera:**
   - La rama `web` no necesita recordar el pasado. Solo necesita mostrar el presente.
   - Tratarla como un commit único con `--amend` y `--force` es la técnica más limpia que existe: **cero grasa, cero residuos históricos, tamaño mínimo perpetuo en IONOS**.

---

## 6. El Flujo de Trabajo Definitivo para Cada Cambio

A partir de ahora, cada vez que edites el libro y quieras publicarlo en la web:

### En tu ordenador local:
```bash
# 1. Asegúrate de estar en main y generar el nuevo HTML
git checkout main
python scripts/build.py        # (o el script de compilación que uses)

# 2. Copias el nuevo HTML a un temporal seguro
cp -r output/html /tmp/libro_web_temp

# 3. Te pasas a la rama web, vacías y copias la nueva foto
git checkout web
git rm -rf .
cp -r /tmp/libro_web_temp/. .
rm -rf /tmp/libro_web_temp

# 4. Sobrescribes el commit único con --amend
git add .
git commit --amend -m "Publicación estática para servidor web (actualizada $(date +%Y-%m-%d))"

# 5. Subes a las bravas con --force
git push origin web --force

# 6. Vuelves a main para seguir trabajando
git checkout main
```

*(Opcional: Si este cambio representa una versión señalada, marcas el tag en main: `git tag v1.0.1 && git push origin v1.0.1`).*

### En el servidor IONOS:
En la carpeta pública de tu web:
```bash
git fetch --depth 1 origin web
git reset --hard origin/web
```
En apenas 2 segundos, tu web estará sincronizada, limpia y ocupando el mínimo espacio posible.
