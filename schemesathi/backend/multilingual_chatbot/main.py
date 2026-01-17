from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from .services.chatbot_service import chatbot_service
from .translation_middleware import process_input_translation, process_output_translation
from .utils.languages import is_supported, SUPPORTED_LANGUAGES

app = FastAPI(
    title="Multilingual Chatbot API",
    description="A chatbot system that processes logic in English using translation middleware.",
    version="1.0.0"
)

class ChatbotRequest(BaseModel):
    message: str
    user_language: str

class ChatbotResponse(BaseModel):
    english_response: str
    translated_response: str

@app.get("/")
async def health_check():
    return {
        "status": "online",
        "supported_languages": SUPPORTED_LANGUAGES
    }

@app.post("/chatbot", response_model=ChatbotResponse)
async def chat_endpoint(request: ChatbotRequest):
    """
    Multilingual Chatbot Endpoint.
    Flow: 
    1. Input Translation (Middleware) 
    2. Core Logic (English only) 
    3. Output Translation (Middleware)
    """
    
    # 0. Validation
    if not is_supported(request.user_language):
        raise HTTPException(status_code=400, detail=f"Language '{request.user_language}' is not supported.")

    try:
        # 1. INPUT MIDDLEWARE: Translate any incoming language -> English
        english_input = await process_input_translation(request.message, request.user_language)
        
        # 2. CORE CHATBOT LOGIC: Operates ONLY in English
        # This part of the code doesn't care about the user's original language.
        english_output = await chatbot_service.get_response(english_input)
        
        # 3. OUTPUT MIDDLEWARE: Translate English response -> User's selected language
        translated_output = await process_output_translation(english_output, request.user_language)
        
        return ChatbotResponse(
            english_response=english_output,
            translated_response=translated_output
        )

    except Exception as e:
        # Production-style error handling
        raise HTTPException(status_code=500, detail=f"An error occurred during processing: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
