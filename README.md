<h1 align="Center">Json-Parser</h1>
<hr>

This tool can be used to add, update schema files. Validating an user input file (json response) is also a functionality. 

<h3>Following are the project features:</h3>

1. Add Schema:

<ul>
<li>Allow users to add a new JSON schema to the tool.</li>
<li>Validate the added schema for correctness.</li>
<li>Provide feedback on successful addition or errors in the new schema.</li>
</ul>

2. Create Documentation (with Internal Schema Validation):
<ul>
<li>Generate human-readable documentation from a selected JSON schema.</li>
<li>Internally validate the provided schema to ensure its correctness.</li>
<li>Display detailed error messages if the schema is invalid. </li>
<li>Save documentation to a file or display it on the console.</li>
</ul>

3. Update Schema:
<ul>
<li>Enable users to update an existing JSON schema.</li>
<li>Validate the updated schema for correctness.</li>
<li>Allow operations such as adding, modifying, or removing properties and constraints.</li>
<li>Provide feedback on the success of the update or errors in the updated schema.</li>
</ul>

<hr>

<h3>Examples of structure for json files:</h3>

1. Sample Json Schema structure:
   
```
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Example Schema",
  "description": "An example JSON schema",
  "type": "object",
  "properties": {
    "property1": {
      "type": "string",
      "description": "Description of property1"
    },
    "property2": {
      "type": "integer",
      "minimum": 0,
      "description": "Description of property2"
    },
    "property3": {
      "type": "boolean",
      "description": "Description of property3"
    }
    // Add more properties as needed
  },
  "required": ["property1", "property2"],
  "additionalProperties": false
}
```
2. Sample structure for updation

```
{
  "add": {
    "properties": {
      "newProperty": {"type": "string"}
    }
  },
  "remove": ["oldProperty"],
  "update": {
    "properties": {
      "existingProperty": {"description": "Updated description"}
    }
  }
}
```

<h3>Usage of the tool:</h3>

1. Adding a schema 
```
python main.py --addSchema Schema.json
```

2. Validating a user input and creating a documentation file for the same
```
python main.py --createDocs userInput.json
```  
This will create a ```output.md``` if the user file matches the schema description

3. Updating a schema object
```
python main.py --updateSchema update.json
```

<hr>

