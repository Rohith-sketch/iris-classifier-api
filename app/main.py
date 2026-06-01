from fastapi import FastAPI
from contextlib import asynccontextmanager
import joblib
from app.routers import health, predict

# 1. The Morning Prep Function (Lifespan)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- BEFORE THE DOORS OPEN ---
    print("🌅 MORNING PREP: Loading the AI Brain from the basement...")
    
    # We load the joblib file and put it on the shared Kitchen Counter (app.state)
    app.state.model = joblib.load("model.joblib")
    
    print("✅ PREP COMPLETE: Doors are unlocked!")
    
    yield # <-- This yield means "The restaurant is now open for business!"
    
    # --- AFTER THE RESTAURANT CLOSES ---
    print("🌙 CLOSING TIME: Sweeping the floors and shutting down.")


# 2. Hire the Manager, and tell them to do the Morning Prep!
app = FastAPI(title="Iris Classifier - Day 4", lifespan=lifespan)

# 3. Connect the Walkie-Talkies
app.include_router(health.router)
app.include_router(predict.router)
