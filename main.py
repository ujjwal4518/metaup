from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.presentation import router as presentation_router

app = FastAPI()

# Root health check route
@app.get("/")
async def root():
    return {"status": "ok", "message": "FastAPI is running 🚀"}

# Mount static folders if needed later
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/output", StaticFiles(directory="output"), name="output")

# Include routes
app.include_router(presentation_router)
