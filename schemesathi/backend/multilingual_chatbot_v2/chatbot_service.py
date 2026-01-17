class ChatbotService:
    """
    Core Chatbot Logic (English Only).
    This logic never sees non-English text.
    """
    
    async def process_query(self, english_text: str) -> str:
        text = english_text.lower()
        
        if "hello" in text or "hi" in text:
            return "Hello! This is SchemeSathi assistant."
        
        if "scheme" in text or "yojana" in text:
            return "You are eligible for the Housing Scheme."
        
        return "I can help you with eligibility check. Please specify the scheme name."

chatbot_service = ChatbotService()
