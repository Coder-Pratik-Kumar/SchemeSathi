import asyncio

# Mock translation dictionary for demonstration purposes
# In a real scenario, this would call Google Translate, Azure, or IndicTrans API.
MOCK_TRANSLATIONS = {
    # Non-English to English (Input)
    ("नमस्ते", "hi", "en"): "Hello",
    ("नमस्कार", "mr", "en"): "Hello",
    ("வணக்கம்", "ta", "en"): "Hello",
    ("হ্যালো", "bn", "en"): "Hello",
    ("मुझे योजनाओं के बारे में बताएं", "hi", "en"): "Tell me about schemes",
    ("योजनांबद्दल सांगा", "mr", "en"): "Tell me about schemes",
    
    # English to Non-English (Output)
    ("Hello! I am your assistant. How can I help you with government schemes today?", "en", "hi"): "नमस्ते! मैं आपका सहायक हूँ। आज मैं सरकारी योजनाओं में आपकी क्या सहायता कर सकता हूँ?",
    ("Hello! I am your assistant. How can I help you with government schemes today?", "en", "mr"): "नमस्कार! मी तुमचा सहाय्यक आहे. आज मी तुम्हाला सरकारी योजनांबद्दल कशी मदत करू शकतो?",
    ("Hello! I am your assistant. How can I help you with government schemes today?", "en", "ta"): "வணக்கம்! நான் உங்கள் உதவியாளர். இன்று அரசு திட்டங்களுக்கு நான் உங்களுக்கு எப்படி உதவ முடியும்?",
    ("Hello! I am your assistant. How can I help you with government schemes today?", "en", "bn"): "হ্যালো! আমি আপনার সহকারী। আজ আমি আপনাকে সরকারি প্রকল্পের বিষয়ে কীভাবে সাহায্য করতে পারি?",
    
    ("You are eligible for the Prime Minister's Housing Scheme.", "en", "hi"): "आप प्रधानमंत्री आवास योजना के लिए पात्र हैं।",
    ("You are eligible for the Prime Minister's Housing Scheme.", "en", "mr"): "तुम्ही प्रधानमंत्री आवास योजनेसाठी पात्र आहात.",
}

async def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    Translates text from source_lang to target_lang.
    This is a pluggable layer. Replace the mock logic with a real API call.
    """
    if source_lang == target_lang:
        return text
    
    # Simulate API latency
    await asyncio.sleep(0.1)
    
    # Lookup in mock dictionary, return original if not found (for demo)
    translated = MOCK_TRANSLATIONS.get((text, source_lang, target_lang))
    
    if translated:
        return translated
    
    # Fallback/Mock behavior: if not in dict, just return a dummy string to show it was "processed"
    if target_lang != "en":
        return f"[Translated to {target_lang}] {text}"
    else:
        return text # If translating to English and not found, return as is for chatbot to handle
