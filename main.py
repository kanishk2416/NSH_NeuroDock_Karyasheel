from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import pandas as pd
import uuid
import os

app = FastAPI(title="Cargo Stowage Optimization - NSH 2025", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage
session_data = {
    "items": None,
    "containers": None,
    "placement_result": None,
    "output_file": "output_solution.csv"
}

class PlacementResponse(BaseModel):
    status: str
    placed_items: int
    output_file: str

@app.get("/")
def read_root():
    return {"message": "Cargo Stowage API is running 🚀"}

@app.post("/api/placement", response_model=PlacementResponse, summary="Compute optimal placement")
async def compute_placement(
    input_items: UploadFile = File(..., description="CSV of items"),
    containers: UploadFile = File(..., description="CSV of containers")
):
    try:
        items_df = pd.read_csv(input_items.file)
        containers_df = pd.read_csv(containers.file)

        # Add volume calculation
        items_df["volume"] = items_df["length"] * items_df["width"] * items_df["height"]
        containers_df["volume"] = containers_df["length"] * containers_df["width"] * containers_df["height"]

        # Sort items largest to smallest
        items_df = items_df.sort_values(by="volume", ascending=False)
        containers_df = containers_df.sort_values(by="volume")

        placement = []
        for _, item in items_df.iterrows():
            placed = False
            for _, container in containers_df.iterrows():
                if container["volume"] >= item["volume"]:
                    placement.append({
                        "item_id": item["item_id"],
                        "container_id": container["container_id"]
                    })
                    # reduce container volume
                    container["volume"] -= item["volume"]
                    placed = True
                    break
            if not placed:
                placement.append({
                    "item_id": item["item_id"],
                    "container_id": "UNPLACED"
                })

        placement_df = pd.DataFrame(placement)
        placement_df.to_csv(session_data["output_file"], index=False)

        # Store data for later use
        session_data["items"] = items_df
        session_data["containers"] = containers_df
        session_data["placement_result"] = placement_df

        return {
            "status": "success",
            "placed_items": (placement_df["container_id"] != "UNPLACED").sum(),
            "output_file": session_data["output_file"]
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/api/download", summary="Download the solution CSV")
def download_solution():
    if session_data["placement_result"] is None:
        return JSONResponse(status_code=404, content={"error": "No solution file found. Please run /api/placement first."})
    return FileResponse(session_data["output_file"], media_type="text/csv", filename="solution.csv")

@app.get("/api/search", summary="Search for an item")
def search_item(item_id: str = Query(..., description="ID of the item to search for")):
    if session_data["placement_result"] is None:
        return JSONResponse(status_code=404, content={"error": "No placement data found."})
    row = session_data["placement_result"][session_data["placement_result"]["item_id"] == item_id]
    if row.empty:
        return {"item_id": item_id, "status": "Not found"}
    return {"item_id": item_id, "status": "Found", "container_id": row["container_id"].values[0]}

@app.get("/api/retrieve", summary="Get retrieval info for an item")
def retrieve_item(item_id: str = Query(..., description="ID of the item to retrieve")):
    if session_data["placement_result"] is None:
        return JSONResponse(status_code=404, content={"error": "No placement data found."})
    row = session_data["placement_result"][session_data["placement_result"]["item_id"] == item_id]
    if row.empty:
        return {"item_id": item_id, "status": "Not found"}
    return {"item_id": item_id, "status": "Retrievable", "location": f"Container: {row['container_id'].values[0]}"}
