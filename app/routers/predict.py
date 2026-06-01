from fastapi import APIRouter, Request 
from app.schemas.iris import IrisInput, IrisOutput
import logging

# Set up the Cash Register (Logger)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/predict", response_model=IrisOutput)
def predict(body: IrisInput, request: Request): 
    
    # 1. Gather the raw ingredients (the 4 numbers from the customer)
    features = [[
        body.sepal_length, 
        body.sepal_width, 
        body.petal_length, 
        body.petal_width
    ]]
    
    # 2. Look at the Kitchen Counter and ask the AI Brain to predict!
    prediction_number = request.app.state.model.predict(features)[0]
    
    # 3. Translate the computer number (0, 1, or 2) into human words
    species_names = ["Iris Setosa", "Iris Versicolor", "Iris Virginica"]
    final_answer = species_names[prediction_number]
    
    # 4. 📝 PRINT THE RECEIPT! (Log the real answer, not the fake one!)
    logger.info(f"Prediction requested. Input: {body.model_dump()} | Output: {final_answer}")
    
    # 5. Serve the plate to the customer!
    return IrisOutput(prediction=final_answer)