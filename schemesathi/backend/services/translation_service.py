import asyncio

# Mock translation data for demo/hackathon
MOCK_TRANSLATIONS = {
    # Scheme names
    ("PM Kisan Samman Nidhi", "en", "hi"): "पीएम किसान सम्मान निधि",
    ("Pradhan Mantri Awas Yojana", "en", "hi"): "प्रधानमंत्री आवास योजना",
    ("Ujjwala Yojana", "en", "hi"): "उज्ज्वला योजना",
    
    # Common UI fields
    ("Age: 18-60, Income < 250000, Caste: ['All']", "en", "hi"): "आयु: 18-60, आय < 250,000, जाति: ['सभी']",
    ("Age: 18-60, Income < 250000, Caste: ['All']", "en", "mr"): "वय: 18-60, उत्पन्न < 250,000, जात: ['सर्व']",
    
    # Generic translated response if not found
    # (In real deployment, this would call Google Translate / Azure)
}

async def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    Translates text from source_lang to target_lang.
    Pluggable layer for Google Translate, Azure, or IndicTrans API.
    """
    if not text or source_lang == target_lang:
        return text
    
    # Simulated API latency
    await asyncio.sleep(0.01)
    
    # Check mock dictionary
    translated = MOCK_TRANSLATIONS.get((text, source_lang, target_lang))
    if translated:
        return translated
    
    # Fallback for hackathon demo: append [lang] to show it's "processed"
    return f"[{target_lang}] {text}"

async def translate_object(obj: dict, fields_to_translate: list, source_lang: str, target_lang: str) -> dict:
    """
    Translates specific fields within a dictionary.
    """
    if source_lang == target_lang:
        return obj
        
    for field in fields_to_translate:
        if field in obj and isinstance(obj[field], str):
            obj[field] = await translate_text(obj[field], source_lang, target_lang)
    return obj
