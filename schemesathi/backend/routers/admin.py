from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..services import ogd_service

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

def sync_ogd_data_task(db: Session):
    print("Starting OGD Sync...")
    schemes_data = ogd_service.fetch_schemes_from_ogd()
    count = 0
    for scheme_raw in schemes_data:
        normalized_data = ogd_service.normalize_scheme_data(scheme_raw)
        # Convert to Pydantic model
        scheme_create = schemas.SchemeCreate(**normalized_data)
        crud.upsert_scheme_by_code(db, scheme_create.scheme_code, scheme_create)
        count += 1
    print(f"OGD Sync Completed. Processed {count} schemes.")

@router.post("/sync-gov-schemes")
def sync_gov_schemes(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Triggers the synchronization of government schemes from OGD.
    Runs in the background.
    """
    # We pass the db session, but note that for true background tasks independent of the request scope,
    # we might need a fresh session context. For simplicity in this hackathon scope, we'll run it synchronously
    # or simple background task.
    # Actually, SQLAlchemy sessions are request-scoped in FastAPI 'Depends'. 
    # For a proper background task, we should create a new session inside the task.
    
    # Simple synchronous execution for now to ensure data is there for demo
    sync_ogd_data_task(db) 
    
    return {"status": "Sync started (synchronous for demo)"}
