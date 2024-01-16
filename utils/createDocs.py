import json
from utils.validateSchema import validate

schema="../Saved/schema.json"

"""this file is used to create Documentation for the json schema"""

def readJson(inFile):
    try:
        with open (inFile,'r') as f:
            data=json.load(f)
        return data
    except:
        print("Error reading json file. Check for the existence of the file.")

def create(inFile,outFile,schema):

    markdownContent=""""""
    markdownContent+="# testing \n\n"

    try:
        data=readJson(inFile)
        if(validate(schema['properties'],data)):
            for key,value in data.items():
                if(type(value)!=dict):
                    markdownContent+=f"## {key} : {value} \n"
                    markdownContent+="\n"
                else:
                    markdownContent+=f"## {key}: \n"
                    for item,itemValue in value.items():
                        markdownContent += f"   -**{item}**: {itemValue} \n"
                        markdownContent+="\n"

            try:
                with open(outFile, 'w') as file:
                    file.write(markdownContent)
                    print("Successfully created the Markdown file!")
            except:
                print("Error while writing to Output.md")
        else:
            print("Not Successful.")
    except:
        print("Failed!")

