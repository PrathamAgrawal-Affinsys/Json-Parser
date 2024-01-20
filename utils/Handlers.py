from .Validators import Validator
import os 
import json

class Handler:
    def __init__(self):
        self.validator = Validator()

    def readSchemaFile(self, fileName):
        try:
            data=self.validator.readValidateJson(fileName,"Invalid JSON to be added as schema!")
            return data
        except Exception as e:
            print(e)
            print("Error in saving the schema file.")
            return {}


    def saveSchemaFile(self, data):
        try:
            if not os.path.exists('Saved'):
                os.makedirs('Saved')

            with open(f"Saved/schema.json","w") as f:
                json.dump(data, f) 
        except:
            print("Error Saving the schema file.")