from utils.createDocs import create
from utils.addSchema import saveSchema

import json
import argparse

parser = argparse.ArgumentParser()

def listString(arg):
    return list(map(str, arg.split(',')))


parser.add_argument("--addSchema", type=str, help="The name of the schema to add.")
# parser.add_argument("--validateSchema", type=str, help="The name of the schema to validate with.")
parser.add_argument("--createDocs", type=listString, help="The name of the schema to add.")
args = parser.parse_args()
# print(args)

if(args.addSchema!=None):
    saveSchema(args.addSchema)

if(args.createDocs!=None):
    with open('./Saved/schema.json', 'r') as f:
        schema=json.load(f)

    create(args.createDocs[0],args.createDocs[1],schema)
