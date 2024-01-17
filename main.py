from utils.createDocs import create
from utils.addSchema import saveSchema
from utils.updateSchema import update
import json
import argparse

parser = argparse.ArgumentParser()

def listString(arg):
    return list(map(str, arg.split(',')))

parser.add_argument("--addSchema", type=str, help="The name of the schema to add.")
parser.add_argument("--createDocs", type=listString, help="The name of the data you want to create [comma] the name of the output markdown file ")
parser.add_argument("--updateSchema", type=str, help="The name of the file you want to update the schema from.")

args = parser.parse_args()
# print(args)


if(__name__=="__main__"):

    if(args.addSchema!=None and args.createDocs==None and args.updateSchema==None):
        saveSchema(args.addSchema)

    elif(args.createDocs!=None and args.addSchema==None and args.updateSchema==None ):
        try:
            with open('./Saved/schema.json', 'r') as f:
                schema=json.load(f)
            create(args.createDocs[0],args.createDocs[1],schema)
        except:
            print("Not able to open the Schema!")


    elif(args.createDocs==None and args.addSchema==None and args.updateSchema!=None):
        try:
            with open('./Saved/schema.json', 'r') as f:
                schema=json.load(f)
                try:
                    with open(args.updateSchema, 'r') as f:
                        updateSchema=json.load(f)
                    updateSchema=update(updateSchema,schema)

                    try:
                        with open(f"Saved/schema.json","w") as f:
                                json.dump(updateSchema, f)
                        print("Schema updated successfully.")
                    except:
                        print("Not able to write the schema file for updation.")
                except:
                    print(f"Not able to open the {args.updateSchema}!")
        except:
            print("Not able to open the Schema!")
        
    else:
        print("Not able to read and understand the arguements passed.")
