import requests
import os
from datetime import datetime

# Placeholder for OGD API Endpoint
# You would typically find this on https://data.gov.in/
OGD_BASE_URL = os.getenv("OGD_BASE_URL", "https://api.data.gov.in/resource/YOUR_RESOURCE_ID")
OGD_API_KEY = os.getenv("OGD_API_KEY", "YOUR_API_KEY")

def fetch_schemes_from_ogd():
    """
    Fetches scheme data from OGD Platform India.
    This is a simulation since actual OGD API requires specific resource IDs.
    """
    try:
        # In a real scenario, we would make a request like:
        # params = {
        #     "api-key": OGD_API_KEY,
        #     "format": "json",
        #     "limit": 100
        # }
        # response = requests.get(OGD_BASE_URL, params=params)
        # response.raise_for_status()
        # data = response.json()
        
        # MOCK DATA for demonstration purposes if API fetch fails or is not configured
        print("Simulating OGD Fetch...")
        mock_schemes = [
            {
                "scheme_code": "SC001",
                "name": "Pradhan Mantri Awas Yojana",
                "ministry": "Ministry of Housing and Urban Affairs",
                "description": "A scheme to provide affordable housing to the urban poor.",
                "eligibility": "Annual income less than 3 lakhs.",
                "benefits": "Financial assistance for house construction.",
                "is_central": True,
                "state_name": None,
                "last_updated_ogd": datetime.now()
            },
            {
                "scheme_code": "SC002",
                "name": "Ayushman Bharat",
                "ministry": "Ministry of Health and Family Welfare",
                "description": "National Health Protection Scheme.",
                "eligibility": "Specific socio-economic criteria.",
                "benefits": "Health insurance coverage up to 5 lakhs.",
                "is_central": True,
                "state_name": None,
                "last_updated_ogd": datetime.now()
            }
        ]
        return mock_schemes

    except Exception as e:
        print(f"Error fetching from OGD: {e}")
        return []

def normalize_scheme_data(raw_data):
    """
    Normalizes OGD data into our Scheme schema format.
    """
    # In a real implementation, this would handle field mapping.
    # Since we are using mock data that matches our schema, we pass it through.
    return raw_data
