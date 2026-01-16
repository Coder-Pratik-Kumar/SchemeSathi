from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import or_

def get_scheme(db: Session, scheme_id: int):
    return db.query(models.Scheme).filter(models.Scheme.id == scheme_id).first()

def get_schemes(db: Session, skip: int = 0, limit: int = 10, search: str = None):
    query = db.query(models.Scheme)
    if search:
        query = query.filter(
            or_(
                models.Scheme.name.ilike(f"%{search}%"),
                models.Scheme.ministry.ilike(f"%{search}%")
            )
        )
    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return total, items

def create_scheme(db: Session, scheme: schemas.SchemeCreate):
    db_scheme = models.Scheme(**scheme.dict())
    db.add(db_scheme)
    db.commit()
    db.refresh(db_scheme)
    return db_scheme

def update_scheme(db: Session, scheme_id: int, scheme: schemas.SchemeCreate):
    db_scheme = get_scheme(db, scheme_id)
    if not db_scheme:
        return None
    
    update_data = scheme.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_scheme, key, value)
    
    db.commit()
    db.refresh(db_scheme)
    return db_scheme

def upsert_scheme_by_code(db: Session, scheme_code: str, scheme_data: schemas.SchemeCreate):
    existing_scheme = db.query(models.Scheme).filter(models.Scheme.scheme_code == scheme_code).first()
    if existing_scheme:
        # Update
        for key, value in scheme_data.dict(exclude_unset=True).items():
            setattr(existing_scheme, key, value)
        db.commit()
        db.refresh(existing_scheme)
        return existing_scheme
    else:
        # Create
        return create_scheme(db, scheme_data)
