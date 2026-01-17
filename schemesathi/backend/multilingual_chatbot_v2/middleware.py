import json
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, StreamingResponse
from .translation_service import translation_service

class TranslationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.url.path != "/chatbot" or request.method != "POST":
            return await call_next(request)

        # 1. INPUT TRANSLATION (BEFORE)
        body = await request.body()
        data = json.loads(body)
        
        user_lang = data.get("user_language", "en")
        message = data.get("message", "")
        
        # Store for later use in output translation
        request.state.user_language = user_lang
        
        # Translate to English if needed
        english_message = message
        if user_lang != "en":
            english_message = await translation_service.translate(message, user_lang, "en")
        
        # Replace body with English version for the route handler
        data["message"] = english_message
        new_body = json.dumps(data).encode("utf-8")
        
        # Update request body stream
        async def receive():
            return {"type": "http.request", "body": new_body}
        request._receive = receive

        # 2. CALL ROUTE HANDLER
        response = await call_next(request)

        # 3. OUTPUT TRANSLATION (AFTER)
        if isinstance(response, Response) and not isinstance(response, StreamingResponse):
            response_body = b"".join([chunk async for chunk in response.body_iterator])
            resp_data = json.loads(response_body)
            
            english_response = resp_data.get("english_response", "")
            
            # Translate English -> User Language
            translated_response = english_response
            if user_lang != "en":
                translated_response = await translation_service.translate(english_response, "en", user_lang)
            
            # Inject translated response into the API result
            resp_data["translated_response"] = translated_response
            
            return Response(
                content=json.dumps(resp_data),
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type
            )
        
        return response
