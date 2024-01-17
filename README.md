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

<h3>Usage of the tool:</h3>

1. Adding a schema 
```
python main.py --addSchema selectedSchema.json
```

2. Validating a user input and creating a documentation file for the same
```
python main.py --createDocs test.json,output.md
```  
This will create a ```output.md``` if the user file matches the schema description

3. Updating a schema object
```
python main.py --updateSchema update.json
```

<hr>

