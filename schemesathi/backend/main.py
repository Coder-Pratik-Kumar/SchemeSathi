from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
from firebase_config import get_firestore_db
from models import SchemeResponse, UserProfile, PaginatedSchemes, ChatRequest
import firebase_admin
from services.llm_service import generate_answer_from_llm, get_scheme_context
from services.translation_service import translate_text, translate_object
import traceback

app = FastAPI(title="SchemeSathi Backend", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to SchemeSathi Backend (Firestore Edition)"}

def map_firestore_to_schema(doc) -> dict:
    data = doc.to_dict()
    data['id'] = doc.id
    # Synthesize 'eligibility' text for UI display
    min_age = data.get('minAge', 0)
    max_age = data.get('maxAge', 100)
    income = data.get('incomeLimit', 0)
    caste = data.get('eligibleCaste', ['All'])
    data['eligibility'] = f"Age: {min_age}-{max_age}, Income < {income}, Caste: {caste}"
    
    # Determine is_central
    data['is_central'] = (data.get('state') == 'All India')
    
    # ministry default
    data['ministry'] = "Government Dept"
    
    # Ensure all fields for LLM are present
    data['requiredDocuments'] = data.get('requiredDocuments', 'Not specified')

    return data

@app.get("/schemes", response_model=PaginatedSchemes)
async def read_schemes(skip: int = 0, limit: int = 10, search: Optional[str] = None, lang: str = "en"):
    try:
        db = get_firestore_db()
        schemes_ref = db.collection("schemes")
        
        # Firestore doesn't support easy full-text search or offset-based pagination natively without indices.
        # For Hackathon scale (small dataset), we will fetch all and filter in memory.
        docs = schemes_ref.stream()
        all_items = []
        for doc in docs:
            mapped_data = map_firestore_to_schema(doc)
            all_items.append(mapped_data)
            
        # Search Filter
        if search:
            search_lower = search.lower()
            all_items = [i for i in all_items if search_lower in i['name'].lower()]

        # Pagination
        total = len(all_items)
        start = skip
        end = skip + limit
        # Translation
        if lang != "en":
            translated_items = []
            for item in paginated_items:
                translated_item = await translate_object(
                    item, 
                    ["name", "ministry", "eligibility", "benefits", "description"],
                    "en", 
                    lang
                )
                translated_items.append(SchemeResponse(**translated_item))
            paginated_items_final = translated_items
        else:
            paginated_items_final = [SchemeResponse(**i) for i in paginated_items]
        
        return {
            "total": total,
            "page": (skip // limit) + 1,
            "size": limit,
            "items": paginated_items_final
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/schemes/eligible", response_model=List[SchemeResponse])
async def check_eligibility(user: UserProfile):
    try:
        db = get_firestore_db()
        schemes_ref = db.collection("schemes")
        docs = schemes_ref.stream()
        
        eligible_schemes = []
        for doc in docs:
            data = doc.to_dict()
            
            # --- Rule-Based Logic ---
            scheme_state = data.get("state", "All India")
            if scheme_state != "All India" and scheme_state != user.state:
                continue
                
            scheme_castes = data.get("eligibleCaste", ["All"])
            if "All" not in scheme_castes and user.caste not in scheme_castes:
                continue

            scheme_occupations = data.get("occupation", ["All"])
            if "All" not in scheme_occupations and user.occupation not in scheme_occupations:
                continue

            min_age = data.get("minAge", 0)
            max_age = data.get("maxAge", 100)
            if not (min_age <= user.age <= max_age):
                continue
                
            income_limit = data.get("incomeLimit", 0)
            if income_limit > 0 and user.income > income_limit:
                continue
            
            # Map to UI Schema
            mapped_data = map_firestore_to_schema(doc)
            
            # --- Multilingual Support ---
            # Translate specific fields before returning
            if user.language != "en":
                # Translate Name, Ministry, Eligibility text, and Benefits
                translated_data = await translate_object(
                    mapped_data, 
                    ["name", "ministry", "eligibility", "benefits", "description"],
                    "en", 
                    user.language
                )
                eligible_schemes.append(SchemeResponse(**translated_data))
            else:
                eligible_schemes.append(SchemeResponse(**mapped_data))
            
        return eligible_schemes

    except Exception as e:
        print(f"Chat Error: {e}")
        traceback.print_exc()
        # STEP 1: Return real error for debugging
        return {
            "error": str(e),
            "error_type": type(e).__name__
        }

@app.post("/chat")
async def chat_with_bot(request: ChatRequest):
    # STEP 2: Add Hard Logs
    print("CHAT API HIT")
    print("User message:", request.message)
    print("Scheme ID:", request.scheme_id)
    print("Language:", request.language)

    try:
        # 1. INPUT TRANSLATION: Translate incoming message to English
        english_message = await translate_text(request.message, request.language, "en")
        print("English Message:", english_message)

        db = get_firestore_db()
        scheme_ref = db.collection("schemes").document(request.scheme_id)
        doc = scheme_ref.get()
        
        if not doc.exists:
            # Handle missing scheme gracefully but explicitly for debug
            return {"response": "Scheme details are not available yet. Please try again later."}
            
        scheme_data = map_firestore_to_schema(doc)
        print("Scheme data:", scheme_data) # Log scheme data
        
        # Prepare Context
        context = get_scheme_context(scheme_data)
        
        print("CALLING LLM SERVICE NOW")
        # 2. CORE LOGIC: Get LLM answer in English
        answer = generate_answer_from_llm(context, english_message, request.history)
        print("LLM RESPONSE (EN):", answer)
        
        # 3. OUTPUT TRANSLATION: Translate English answer back to User Language
        translated_answer = await translate_text(answer, "en", request.language)
        print("Translated Response:", translated_answer)

        return {
            "english_response": answer,
            "translated_response": translated_answer,
            "response": translated_answer # Unified field for UI
        }

    except Exception as e:
        print(f"Chat Error: {e}")
        traceback.print_exc()
        # STEP 1: Return real error for debugging
        return {
            "error": str(e),
            "error_type": type(e).__name__
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
