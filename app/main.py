from datetime import datetime
from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi import UploadFile, File, HTTPException
from app.s3_service import upload_file_to_s3

# Import database collection and simulation engine
from app.database import history_collection
from app.simulator import run_assembly_simulation

# Initialize FastAPI application
app = FastAPI(title="Cloud Assembly Simulator", version="1.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to Cloud Assembly Simulator API"}


# Endpoint 1: Upload assembly file, run simulator, and save results to MongoDB
@app.post("/upload-assembly")
async def upload_assembly_file(file: UploadFile = File(...)):
    # 1. Read binary content asynchronously and decode bytes to UTF-8 string
    content = await file.read()
    code_text = content.decode("utf-8")

    # 2. Execute assembly code using our custom virtual CPU simulator
    simulation_result = run_assembly_simulation(code_text)

    # 3. Construct document dictionary to be stored in MongoDB Atlas
    record = {
        "filename": file.filename,
        "code_text": code_text,
        "simulation": simulation_result,
        "created_at": datetime.utcnow(),  # Timestamp in UTC
    }

    # 4. Insert document asynchronously into MongoDB history collection
    insert_result = await history_collection.insert_one(record)

    # 5. Return JSON response including generated MongoDB ObjectId as string
    return {
        "id": str(insert_result.inserted_id),
        "filename": file.filename,
        "simulation": simulation_result,
        "saved_to_db": True,
    }


# Endpoint 2: Retrieve the latest 10 simulation runs from MongoDB
@app.get("/history")
async def get_simulation_history():
    # 1. Query MongoDB: sort by creation date descending (-1) and limit to 10 records
    cursor = history_collection.find().sort("created_at", -1).limit(10)
    history = []

    # 2. Asynchronously iterate over documents in cursor
    async for document in cursor:
        # Convert ObjectId to a string for JSON compatibility
        document["_id"] = str(document["_id"])
        history.append(document)

    # 3. Return execution history as JSON
    return {"history": history}

@app.post("/upload-to-s3/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_url = await upload_file_to_s3(file)
        record = {
            "filename": file.filename,
            "file_url": file_url,
            "status": "uploaded"
        }
        await history_collection.insert_one(record)
        
        return {"message": "File uploaded successfully", "file_url": file_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))