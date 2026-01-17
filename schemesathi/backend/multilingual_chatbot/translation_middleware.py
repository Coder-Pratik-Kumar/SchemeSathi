from .services.translation_service import translate_text
from .utils.languages import is_supported

async def process_input_translation(message: str, user_language: str) -> str:
    """
    Middleware function logic for input translation.
    Ensures that the chatbot logic receives ONLY English text.
    """
    if not is_supported(user_language):
        # Default to no translation or handle error? 
        # For this design, we assume the frontend sends a valid code.
        return message

    if user_language == "en":
        return message

    # Translate User Language -> English
    english_text = await translate_text(message, user_language, "en")
    return english_text

async def process_output_translation(english_response: str, target_language: str) -> str:
    """
    Middleware function logic for output translation.
    Translates the chatbot's English response back to the user's preferred language.
    """
    if not is_supported(target_language) or target_language == "en":
        return english_response

    # Translate English -> Target Language
    translated_text = await translate_text(english_response, "en", target_language)
    return translated_text
