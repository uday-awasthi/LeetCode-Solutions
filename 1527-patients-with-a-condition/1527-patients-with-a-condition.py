import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients[
        patients["conditions"].str.contains(r"(^| )DIAB1", regex=True)
    ]
    
    return result[["patient_id", "patient_name", "conditions"]]