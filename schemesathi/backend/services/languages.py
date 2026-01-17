SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "ta": "Tamil",
    "bn": "Bengali"
}

def is_supported(lang_code: str) -> bool:
    return lang_code in SUPPORTED_LANGUAGES
