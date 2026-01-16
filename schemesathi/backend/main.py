from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="SchemeSathi Backend", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to SchemeSathi Backend"}

# Import routers
from .routers import schemes, admin
app.include_router(schemes.router)
app.include_router(admin.router)
