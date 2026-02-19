# Skill: Motor de Libros Multilingües

Este "Skill" permite generar libros web multilingües con la misma arquitectura que "Mi amigo Jesucristo".

## Estructura
1. **Contenido**: Pon tus textos en un JSON siguiendo el formato de `translations.json`.
2. **Enlaces**: Configura tus Spotify, Ko-fi y redes en `enlaces.json`.
3. **Generación**: Ejecuta el script para construir todos los HTML.

## Cómo usar el Agente para tu próximo libro:
Pasa este prompt a tu asistente:
> "He desarrollado una arquitectura de libros en `/Users/fjbanezares/libro sobre mi amigo Jesucristo/`. 
> Úsala como base (Skill) para mi nuevo libro: [Título].
> Copia la lógica de `translate_all_chapters.py` pero adapta el diseño a estos nuevos colores: [Colores]."

## Beneficios
- **Escalabilidad**: Traduce a +10 idiomas de forma automática.
- **Mantenibilidad**: Cambia un enlace en un sitio y se actualiza en todo el libro.
- **SEO**: Estructura preparada para buscadores.
