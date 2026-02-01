from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator
import joblib
import numpy as np
import os

# ==============================
# Load ML model (safe path)
# ==============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "Lung_Cancer_Prediction_Model.joblib")

if not os.path.exists(MODEL_PATH):
    raise RuntimeError("❌ Lung_Cancer_Prediction_Model.joblib file not found")

model = joblib.load(MODEL_PATH)

# ==============================
# FastAPI app
# ==============================
app = FastAPI(
    title="Lung Cacer Prediction API",
    version="1.0"
)

# ==============================
# CORS (Frontend connect)
# ==============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # production এ specific domain দিবে
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# Input Schema with STRICT validation
# ==============================
class Lung_Cancer_Input(BaseModel):
    GENDER: int = Field(..., gt=0, le=1)
    AGE: int = Field(..., ge=0, description="Age must be > 0")
    SMOKING: int = Field(..., ge=1, le=2)
    YELLOW_FINGERS: int = Field(..., gt=1, le=2)
    ANXIETY: int = Field(..., ge=1, le=2)
    PEER_PRESSURE: int = Field(..., ge=1, le=2)
    CHRONIC_DISEASE: int = Field(..., ge=1, le=2)
    FATIGUE: int = Field(..., gt=1, le=2)
    ALLERGY: int = Field(..., ge=1, le=2)
    WHEEZING: int = Field(..., ge=1, le=2)
    ALCOHOL_CONSUMING: int = Field(..., ge=1, le=2)
    COUGHING: int = Field(..., ge=1, le=2)
    SHORTNESS_OF_BREATH: int = Field(..., ge=1, le=2)
    SWALLOWING_DIFFICULTY: int = Field(..., ge=1, le=2)
    CHEST_PAIN: int = Field(..., ge=1, le=2)

    # Blank / empty check
    @field_validator("*", mode="before")
    @classmethod
    def no_blank_value(cls, v):
        if v is None or v == "":
            raise ValueError("Field cannot be blank")
        return v

# ==============================
# Routes
# ==============================
@app.get("/")
def health():
    return {"status": "API running successfully"}

@app.post("/predict")
def predict(data: Lung_Cancer_Input):

    values = list(data.model_dump().values())


    features = np.array([values])

    prediction = model.predict(features)[0]

    return {
        "prediction": int(prediction),
        "result": "Lung Cancer Detected" if prediction == 1 else "No Lung Cancer"
    }
