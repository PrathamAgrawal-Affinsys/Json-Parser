"""This file is used for updating the schema object."""

def update(newFile,schema):
    if("add" in newFile.keys()):
        addM=newFile["add"]["properties"]
        for key,value in addM.items():
            schema['properties'][key]=value


    if("remove" in newFile.keys()):
        for item in newFile["remove"]:
            del schema['properties'][item]

    if("update" in newFile.keys()):
        for key,value in newFile["update"]["properties"].items():
            if(key not in schema['properties'].keys()):
                print(f"Warning:{key} not found in schema.")
            else:
                for nKey,nValue in value.items():
                    schema['properties'][key][nKey]=nValue
    return schema