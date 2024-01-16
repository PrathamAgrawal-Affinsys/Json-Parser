"""File is used for reading and saving the schema files."""

import json
import os
def readJson(inFile):
    try:
        with open (inFile,'r') as f:
            data=json.load(f)
        return data
        
    except:
        print("Error reading json file. Check for the existence of the file.")

def saveSchema(inFile):
    try:
        data=readJson(inFile)
        if not os.path.exists('Saved'):
            os.makedirs('Saved')

        with open(f"Saved/updated.json","w") as f:
            json.dump(data, f) 
    except:
        print("Error saving schema file.")