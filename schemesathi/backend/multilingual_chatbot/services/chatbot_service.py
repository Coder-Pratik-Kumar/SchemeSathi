class ChatbotService:
    """
    Core Chatbot Logic.
    CRITICAL CONSTRAINT: This service ONLY processes English text.
    It is language-agnostic regarding the end-user.
    """
    
    def __init__(self):
        # In a real app, this might initialize an LLM client (OpenAI, LangChain, etc.)
        pass

    async def get_response(self, english_message: str) -> str:
        """
        Takes an English message and returns an English response.
        """
        msg = english_message.lower()
        
        if "hello" in msg or "hi" in msg:
            return "Hello! I am your assistant. How can I help you with government schemes today?"
        
        if "scheme" in msg or "yojana" in msg:
            return "You are eligible for the Prime Minister's Housing Scheme."
        
        # Default fallback response in English
        return "I'm sorry, I couldn't find specific information on that. Could you please provide more details about the scheme you are looking for?"

# Singleton instance for the application
chatbot_service = ChatbotService()
