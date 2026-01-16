from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/schemes",
    tags=["schemes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=schemas.PaginatedSchemes)
def read_schemes(skip: int = 0, limit: int = 10, search: str = None, db: Session = Depends(get_db)):
    total, items = crud.get_schemes(db, skip=skip, limit=limit, search=search)
    return {"total": total, "page": (skip // limit) + 1, "size": limit, "items": items}

@router.get("/{scheme_id}", response_model=schemas.Scheme)
def read_scheme(scheme_id: int, db: Session = Depends(get_db)):
    db_scheme = crud.get_scheme(db, scheme_id=scheme_id)
    if db_scheme is None:
        raise HTTPException(status_code=404, detail="Scheme not found")
    return db_scheme
