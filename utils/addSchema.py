"""File is used for reading and saving the schema files."""

import json
import os

def readValidateJson(inFile):
    with open(inFile) as file:    
        try:
            return json.load(file) 
        except json.decoder.JSONDecodeError:
            print("Invalid JSON to be added as schema!") 
            return {}


def saveSchema(inFile):
    try:
        data=readValidateJson(inFile)
        if not os.path.exists('Saved'):
            os.makedirs('Saved')

        with open(f"Saved/schema.json","w") as f:
            json.dump(data, f) 
    except:
        print("Error saving schema file.")