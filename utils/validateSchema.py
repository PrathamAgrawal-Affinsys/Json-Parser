def validateSchema(schema):
    pass



def validate(schema,data):
    isValid=True  

    for key,item in schema.items():
        if((key not in data.keys()) and (schema[key]['required'])):
            isValid=False
            print(f"{key} not Found")
            
    
        if (key in data.keys()) and (schema[key]['type']=="integer" and type(data[key])!=int):
            isValid=False
            print(f"{key} is not suited for integer")
            
        
        if (key in data.keys()) and (schema[key]['type']=="string" and type(data[key])!=str):
            isValid=False
            print(f"{key} is not suited for String")
            
    
        if("properties" in schema[key]  and key in data.keys()):
            nestedSchema=schema[key]['properties']
            nestedData=data[key]
            for nKey,itemValue in nestedSchema.items():
                if(nKey not in nestedData.keys() and (nestedSchema[nKey]['required'])):
                    isValid=False
                    print(f"{nKey} not Found!")
                    
                    
                if(nKey in nestedData.keys() and (nestedSchema[nKey]['type']=="integer") and type(nestedData[nKey])!=int):
                    isValid=False
                    print(f"{nKey} is not suited for integer")
                    

                if(nKey in nestedData.keys() and (nestedSchema[nKey]['type']=="string") and type(nestedData[nKey])!=str):
                    isValid=False
                    print(f"{nKey} is not suited for string")
                    
                
            for nKey in nestedData.keys():
                if(nKey not in nestedSchema.keys()):
                    isValid=False
                    print(f"{nKey} is not in schema")
                    
    
    for key in data.keys():
        if(key not in schema.keys()):
            isValid=False
            print(f"{key} is not in schema!")
    
    return isValid