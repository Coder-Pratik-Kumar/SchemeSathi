from fastapi import FastAPI, Body
from pydantic import BaseModel
from .middleware import TranslationMiddleware
from .chatbot_service import chatbot_service

app = FastAPI(title="Multilingual Chatbot v2")

# Add the Translation Middleware
app.add_middleware(TranslationMiddleware)

class ChatbotRequest(BaseModel):
    message: str
    user_language: str

class ChatbotResponse(BaseModel):
    english_response: str
    translated_response: str = "" # Will be populated by middleware

@app.post("/chatbot", response_model=ChatbotResponse)
async def chat_handler(request: ChatbotRequest):
    """
    Route handler only sees English.
    All translation happens in middleware.
    """
    # Middleware has already translated request.message to English
    response_text = await chatbot_service.process_query(request.message)
    
    # Middleware will intercept this and add 'translated_response'
    return ChatbotResponse(
        english_response=response_text
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
