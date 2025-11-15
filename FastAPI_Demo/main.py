# Creating the patients api
from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

# function to load json data
def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)

    return data


@app.get("/")
def hello():
    return {"message":"Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient's records."}


@app.get("/view")
def view():
    """This will fetch all the data"""
    data = load_data()
    return data


@app.get("/patients/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    data = load_data()        # loading all the data
    if patient_id in data:    # checking if patient_id key present in data
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort(sort_by: str = Query(..., description="Sort on the basis of height, weight and bmi"),
         order: str = Query("asc", description="sort in asc or desc order")):

    valid_fields = ["height", "weight", "bmi"]

    # Checking the values of sort_by & order parameters
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid field select from {valid_fields")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid field select asc or desc")

    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda  x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data