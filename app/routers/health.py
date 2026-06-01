from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks

# Give this waiter a walkie-talkie
router = APIRouter()

@router.get("/")
def root():
    return {"status": "ok"}


