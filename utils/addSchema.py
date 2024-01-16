"""File is used for reading and saving the schema files."""

import json
import os
from utils.validateSchema import validateSchema

def readJson(inFile):
    try:
        with open (inFile,'r') as f:
            data=json.load(f)
            validateSchema(data) #this is for validating the schema file. Code to be added soon. 
        return data
        
    except:
        print("Error reading json file. Check for the existence of the file.")

def saveSchema(inFile):
    try:
        data=readJson(inFile)
        if not os.path.exists('Saved'):
            os.makedirs('Saved')

        with open(f"Saved/schema.json","w") as f:
            json.dump(data, f) 
    except:
        print("Error saving schema file.")