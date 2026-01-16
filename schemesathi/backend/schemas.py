from pydantic import BaseModel
from typing import Optional, List, Any
from datetime import datetime

class SchemeBase(BaseModel):
    name: str
    ministry: Optional[str] = None
    description: Optional[str] = None
    eligibility: Optional[str] = None
    benefits: Optional[str] = None
    is_central: bool = True
    state_name: Optional[str] = None

class SchemeCreate(SchemeBase):
    scheme_code: Optional[str] = None
    last_updated_ogd: Optional[datetime] = None
    raw_data: Optional[dict] = None

class Scheme(SchemeBase):
    id: int
    scheme_code: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class PaginatedSchemes(BaseModel):
    total: int
    page: int
    size: int
    items: List[Scheme]
