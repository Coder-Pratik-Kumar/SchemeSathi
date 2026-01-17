import asyncio

class TranslationService:
    """
    Pluggable Translation Service. 
    Can be easily swapped for Google/Azure/IndicTrans.
    """
    
    MOCK_DATA = {
        # Non-English -> English
        ("नमस्ते", "hi", "en"): "Hello",
        ("योजना", "hi", "en"): "scheme",
        ("नमस्कार", "mr", "en"): "Hello",
        ("வணக்கம்", "ta", "en"): "Hello",
        ("হ্যালো", "bn", "en"): "Hello",
        
        # English -> Non-English
        ("Hello! This is SchemeSathi assistant.", "en", "hi"): "नमस्ते! यह स्कीमसाथी सहायक है।",
        ("Hello! This is SchemeSathi assistant.", "en", "mr"): "नमस्कार! हे स्कीमसाथी सहाय्यक आहे.",
        ("Hello! This is SchemeSathi assistant.", "en", "ta"): "வணக்கம்! இது ஸ்கீம்சாதி உதவியாளர்.",
        ("Hello! This is SchemeSathi assistant.", "en", "bn"): "হ্যালো! এটি স্কিমসাথী সহকারী।",
        
        ("You are eligible for the Housing Scheme.", "en", "hi"): "आप आवास योजना के लिए पात्र हैं।",
        ("You are eligible for the Housing Scheme.", "en", "mr"): "तुम्ही गृहनिर्माण योजनेसाठी पात्र आहात.",
        ("You are eligible for the Housing Scheme.", "en", "ta"): "வீட்டுவசதித் திட்டத்திற்கு நீங்கள் தகுதியுடையவர்.",
        ("You are eligible for the Housing Scheme.", "en", "bn"): "আপনি আবাসন প্রকল্পের জন্য যোগ্য।",
    }

    async def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        if source_lang == target_lang:
            return text
        
        await asyncio.sleep(0.05)  # Simulate network latency
        
        # Mock lookup
        key = (text, source_lang, target_lang)
        if key in self.MOCK_DATA:
            return self.MOCK_DATA[key]
        
        # Dynamic mockup if not in dictionary
        if target_lang == "en":
            return text  # Assuming English or unknown
        return f"[Translated to {target_lang}] {text}"

translation_service = TranslationService()
