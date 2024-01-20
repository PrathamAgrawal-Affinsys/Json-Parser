import argparse
from utils.models import Schema

parser = argparse.ArgumentParser()

# def listString(arg):
#     return list(map(str, arg.split(',')))

parser.add_argument("--addSchema", type=str, help="The name of the schema to add.")
parser.add_argument("--createDocs", type=str, help="The name of the data you want to create [comma] the name of the output markdown file ")
parser.add_argument("--updateSchema", type=str, help="The name of the file you want to update the schema from.")

args = parser.parse_args()



if(__name__=="__main__"):

    schemaObject=Schema()

    if(args.addSchema!=None and args.createDocs==None and args.updateSchema==None):
        schemaObject.saveSchema(args.addSchema)
        
    elif(args.createDocs!=None and args.addSchema==None and args.updateSchema==None ):
        schemaObject.validateUserFile(args.createDocs[0],'./Saved/schema.json')

    elif(args.createDocs==None and args.addSchema==None and args.updateSchema!=None):
        schemaObject.update(args.updateSchema,"./Saved/schema.json")
        
    else:
        print("Not able to read and understand the arguements passed.")

