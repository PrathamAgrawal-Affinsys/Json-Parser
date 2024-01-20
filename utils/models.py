from .Validators import Validator
from .Handlers import Handler

class Schema:
    def __init__(self):
        print("Schema class called.")
        self.validator=Validator()
        self.handler=Handler()


    def saveSchema(self,fileName):
        data=self.handler.readSchemaFile(fileName)
        self.handler.saveSchemaFile(data)


    def update(self,updateFile,schemaFile):
        
        schema=self.validator.readValidateJson(schemaFile,"Error reading the json schema.")
        updatedSchema=self.validator.readValidateJson(updateFile,"error reading the json file for the newly updated schema.")
        
        if("add" in updatedSchema.keys()):
            addM=updatedSchema["add"]["properties"]
            print(addM)
            for key,value in addM.items():
                schema['properties'][key]=value


        if("remove" in updatedSchema.keys()):
            for item in updatedSchema["remove"]:
                del schema['properties'][item]

        if("update" in updatedSchema.keys()):
            for key,value in updatedSchema["update"]["properties"].items():
                if(key not in schema['properties'].keys()):
                    print(f"Warning:{key} not found in schema.")
                else:
                    for nKey,nValue in value.items():
                        schema['properties'][key][nKey]=nValue

        
        self.handler.saveSchemaFile(schema)

    def create(self,data,outFile="output.md"):

        markdownContent=""""""
        markdownContent+="# testing \n\n"

        try:
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
        except:
            print("Failed!")

    def validateUserFile(self, userFile,schemaFile):

        schema=self.validator.readValidateJson(schemaFile,"Error reading the json schema.")
        userInput=self.validator.readValidateJson(userFile,"error reading the json file for the User Input.")

        if(self.validator.validateUser(schema['properties'],userInput)):
            self.create(userInput)


        

    



