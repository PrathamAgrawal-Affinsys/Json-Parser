def validate(schema,data):
    isValid=True  

    for key,item in schema.items():
        if((key not in data.keys()) and (schema[key]['required'])):
            isValid=False
            print(f"{key} not Found")
            break
    
        if (key in data.keys()) and (schema[key]['type']=="integer" and type(data[key])!=int):
            isValid=False
            print(f"{key} is not suited for integer")
        
        if (key in data.keys()) and (schema[key]['type']=="string" and type(data[key])!=str):
            isValid=False
            print(f"{key} is not suited for String")
    
    for key in data.keys():
        if(key not in schema.keys()):
            isValid=False
            print(f"{key} is not in schema!")
    
    return isValid