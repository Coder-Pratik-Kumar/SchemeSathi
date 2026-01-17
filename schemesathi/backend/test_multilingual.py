import asyncio
from multilingual_chatbot.main import app
from httpx import AsyncClient, ASGITransport

async def test_chatbot():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        print("--- Testing English ---")
        response = await ac.post("/chatbot", json={
            "message": "Hello",
            "user_language": "en"
        })
        print(f"Status: {response.status_code}")
        print(f"Body: {response.json()}")

        print("\n--- Testing Hindi ---")
        response = await ac.post("/chatbot", json={
            "message": "नमस्ते",
            "user_language": "hi"
        })
        print(f"Status: {response.status_code}")
        print(f"Body: {response.json()}")

        print("\n--- Testing Marathi ---")
        response = await ac.post("/chatbot", json={
            "message": "नमस्कार",
            "user_language": "mr"
        })
        print(f"Status: {response.status_code}")
        print(f"Body: {response.json()}")

        print("\n--- Testing Invalid Language ---")
        response = await ac.post("/chatbot", json={
            "message": "Hello",
            "user_language": "fr"
        })
        print(f"Status: {response.status_code}")
        print(f"Body: {response.json()}")

if __name__ == "__main__":
    asyncio.run(test_chatbot())
