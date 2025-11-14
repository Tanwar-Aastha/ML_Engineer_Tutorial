"""
Creating an end-point such that
if anyone hit it 'hello world' will appear.


NOTE: TO RUN THE FILE:
uvicorn <file_name>:<object_name> --reload
"""

# Importing fastapi class from fastapi library
from fastapi import FastAPI

# Step 1: Creating a fastapi object
app = FastAPI()

# Step 2: Defining the end-point for which defining a route
@app.get("/")
# Step3: Creating a method for this end-point
def hello():
    return {"message":"Hello World"}


# Creating another end-point
@app.get("/about")
def about():
    return {"message":"Hii! Here I am learning AI :)"}
