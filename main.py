# src/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cargo Stowage Management System", version="1.0")

# Allow all CORS origins for testing purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def read_root():
    return {"message": "Cargo Stowage API is running 🚀"}

# Placeholder for actual endpoints
@app.get("/api/placement")
def get_placement():
    return {"message": "Optimal placement will be computed here."}

@app.get("/api/search")
def search_item():
    return {"message": "Search endpoint will go here."}

@app.get("/api/retrieve")
def retrieve_item():
    return {"message": "Item retrieval logic will be implemented here."}