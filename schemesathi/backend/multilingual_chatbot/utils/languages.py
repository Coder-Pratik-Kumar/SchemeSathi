SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "ta": "Tamil",
    "bn": "Bengali"
}

def get_language_name(lang_code: str) -> str:
    return SUPPORTED_LANGUAGES.get(lang_code, "Unknown")

def is_supported(lang_code: str) -> bool:
    return lang_code in SUPPORTED_LANGUAGES
