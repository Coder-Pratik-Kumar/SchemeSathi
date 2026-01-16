from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, JSON
from sqlalchemy.sql import func
from .database import Base

class Scheme(Base):
    __tablename__ = "schemes"

    id = Column(Integer, primary_key=True, index=True)
    scheme_code = Column(String, unique=True, index=True, nullable=True) # ID from OGD
    name = Column(String, index=True, nullable=False)
    ministry = Column(String, index=True, nullable=True)
    description = Column(Text, nullable=True)
    eligibility = Column(Text, nullable=True) # Storing as text for now, could be JSON
    benefits = Column(Text, nullable=True)
    is_central = Column(Boolean, default=True) # True for Central, False for State
    state_name = Column(String, nullable=True) # If state scheme
    last_updated_ogd = Column(DateTime, nullable=True) # Date from OGD
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Raw data storage for LLM or reprocessing
    raw_data = Column(JSON, nullable=True)
