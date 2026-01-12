import pandas as pd
import numpy as np
import joblib
import warnings
import datetime

# Silence version warnings for a clean output
warnings.filterwarnings("ignore")

# 1. Load the models
try:
    class_model = joblib.load('Class_model.joblib')
    stage_model = joblib.load('Stage_model.joblib')
except:
    pass 

FEATURES_ORDER = [
    'BloodPressure', 'BloodPressureLimit', 'SpecificGravity', 'Albumin', 'RedBloodCells', 
    'SugarLevel', 'PusCell', 'PusCellClumps', 'Bacteria', 'BloodGlucoseRandom', 'BloodUrea', 
    'Sodium', 'SerumCreatinine', 'Potassium', 'Hemoglobin', 'PackedCellVolume',
    'RedBloodCellCount','WhiteBloodCellCount', 'Hypertension', 'DiabetesMellitus',
    'CoronaryArteryDisease', 'Appetite', 'PedaEdema', 'Anemia','GlomerularRatio', 'Age'
]

def reni_predict_tool(data: dict):
    """
    Analyzes clinical data to detect Chronic Kidney Disease (CKD).
    Expects a dictionary with the 26 clinical variables.
    """
    try:
        # 2. Sort data exactly as the model expects
        input_values = [data[f] for f in FEATURES_ORDER]
        input_matrix = np.array([input_values])

        # 3. Predictions
        is_affected = int(class_model.predict(input_matrix)[0])
        stage = int(stage_model.predict(input_matrix)[0]) if is_affected == 1 else 0
        
        # 4. Result for the Agent
        return {
            "status": "AFFECTED" if is_affected == 1 else "NOT AFFECTED",
            "stage": stage,
            "confidence_note": "Result based on trained Machine Learning models.",
            "medical_summary": f"Diagnosis: {'Patient with CKD' if is_affected == 1 else 'Patient without CKD'}. Stage: {stage}"
        }
    except Exception as e:
        return {"error": f"Missing data or incorrect format: {str(e)}"}