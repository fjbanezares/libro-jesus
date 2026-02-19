---
name: multilingual-book-engine
description: A system to generate elegant, multilingual web books with integrated Spotify and donation links.
---

# Multilingual Book Engine Skill

Use this skill to replicate the architecture and generation logic of the project "Mi amigo Jesucristo".

## Core Capabilities
- **Multi-language Generation**: Automated HTML generation for 11+ languages using a central JSON.
- **Dynamic Content Embedding**: Integration of language-specific Spotify tracks and albums.
- **Integrated Call-to-Actions**: Modular donation buttons (Ko-fi/PayPal) and Linktree navigation.
- **RTL Support**: Full support for Right-to-Left languages like Arabic.

## Project Structure to Replicate
1. `translations.json`: The central data store for all translated text (Titles, H1, Body).
2. `enlaces.json`: Configuration for external links (Spotify, Donation, Social).
3. `translate_all_chapters.py`: The generation script.
4. `output/html/`: Target directory for the generated web book.

## How to use in a new project
When starting a new book, tell the agent:
> "I want to create a new book using the Multilingual Book Engine from `/Users/fjbanezares/libro sobre mi amigo Jesucristo/`. 
> 1. Copy the logic from `translate_all_chapters.py`.
> 2. Create a fresh `translations.json` for the new content.
> 3. Use the same `enlaces.json` structure for links.
> 4. Keep the multilingual chapters logic but apply these new brand colors: [Color Palette]."

## Technical Recommendations
- **Avoid hardcoding**: Always use the JSON files for text and URLs.
- **CSS Modularity**: Keep the base styles in the generation script or a separate `base.css` that is injected.
- **Image Handling**: Store chapter and footer images in a dedicated `images/` folder with consistent naming.
