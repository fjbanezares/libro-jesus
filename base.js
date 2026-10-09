document.addEventListener('DOMContentLoaded', () => {
    const languageSelect = document.getElementById('language-select');
    const languages = document.querySelectorAll('.language');

    window.setLanguage = function (lang) {
        languages.forEach(el => {
            if (el.classList.contains(lang)) {
                el.style.display = 'block';
            } else {
                el.style.display = 'none';
            }
        });
        localStorage.setItem('preferred-language', lang);
        if (languageSelect) {
            languageSelect.value = lang;
        }
    }

    if (languageSelect) {
        languageSelect.addEventListener('change', (e) => {
            setLanguage(e.target.value);
        });
    }

    // Initialize from localStorage or default to spanish
    const savedLang = localStorage.getItem('preferred-language') || 'spanish';
    setLanguage(savedLang);
});
