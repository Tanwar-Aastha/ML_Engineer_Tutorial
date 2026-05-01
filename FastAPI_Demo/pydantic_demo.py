# PYDANTIC => used for data validation in FastAPI
# it solves the problems of `Type-validation` and `data validation`

# loading libraries
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Optional


class Patient(BaseModel):
    # defining the data schema
    name: str
    email: EmailStr
    age: int
    weight: float
    married: Optional[bool] = False
    allergies: Optional[List[str]] = None # allergies will have a list of strings (keeping it Optional)
    contact_details: Dict[str, str]    # will store dictionary (key is string & value is string)


    # creating a field validator
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        """
        This class method will validate the email. If it is valid or not.
        input: value: str
        output: str
        """
        domain_options = ['icici.com', 'sbi.com']        

        domain_value = value.split("@")[-1]

        if domain_value not in domain_options:
            raise ValueError("Not a valid domain!")
        else:
            return value



# Defining a function
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.weight)
    print(patient.contact_details)
    print("Inserted !!")

# Defining raw data
patient_info = {"name":"Abc", 
                "age":20, 
                "weight":70.1,
                # "married":True,
                # "allergies":["pollen","dust"],
                "contact_details":{"email":"abc@gmail.com","phone":"22342312"}}

# Creating the Patient class object
patient1 = Patient(**patient_info)


# Calling the fucntion
insert_patient_data(patient1)