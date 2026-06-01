from pydantic import BaseModel, Field

#Give bouncer some rules to check the guests (Pydantic model)
class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

class IrisOutput(BaseModel):
    # We promise to only send back a string called "prediction"
    prediction: str