import asyncio
import json
from httpx import AsyncClient, ASGITransport
from main import app

async def test_scheme_translation():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        print("--- Testing /schemes/eligible with Hindi ---")
        user_data = {
            "age": 25,
            "income": 100000,
            "caste": "General",
            "occupation": "Farmer",
            "state": "Maharashtra",
            "language": "hi"
        }
        response = await ac.post("/schemes/eligible", json=user_data)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            schemes = response.json()
            if schemes:
                print(f"First Scheme Name: {schemes[0]['schemeName']}")
                print(f"Eligibility: {schemes[0]['eligibility']}")
            else:
                print("No eligible schemes found for test user.")
        else:
            print(f"Error: {response.text}")

        print("\n--- Testing /schemes with Marathi ---")
        response = await ac.get("/schemes", params={"skip": 0, "limit": 1, "lang": "mr"})
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            if data['items']:
                print(f"First Scheme Name: {data['items'][0]['schemeName']}")
                print(f"Ministry: {data['items'][0]['ministry']}")
            else:
                print("No schemes found.")
        else:
            print(f"Error: {response.text}")

if __name__ == "__main__":
    asyncio.run(test_scheme_translation())
