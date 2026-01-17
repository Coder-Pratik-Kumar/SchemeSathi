import asyncio
import json
from httpx import AsyncClient, ASGITransport
from multilingual_chatbot_v2.main import app

async def test_v2():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        test_cases = [
            ("Hello", "en"),
            ("नमस्ते", "hi"),
            ("योजना", "hi"),
            ("नमस्कार", "mr"),
            ("வணக்கம்", "ta"),
            ("হ্যালো", "bn")
        ]
        
        for msg, lang in test_cases:
            print(f"\n>>> Input: '{msg}' (Language: {lang})")
            response = await ac.post("/chatbot", json={
                "message": msg,
                "user_language": lang
            })
            print(f"Status: {response.status_code}")
            print(f"Body: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")

if __name__ == "__main__":
    asyncio.run(test_v2())
