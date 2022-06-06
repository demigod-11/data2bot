# Objective
This program:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

# DEPENDENCIES
- The program has no dependency save python >= 3.6 

# Additional informations for test cases
- Padding: All attributes in the output JSON schema  are padded with "tag" : "" and "description" key/value
- The output JSON schema sets all properties "required": false
- The schema output captures ONLY the attributes within the "message" key of the input JSON source data. 
- For data types of the JSON schema:
STRING: program should identify what is a string and map accordingly in JSON schema output
INTEGER: program should identify what is an integer and map accordingly in JSON schema output
ENUM: When the value in an array is a string, the program should map the data type as an ENUM 
ARRAY: When the value in an array is another JSON object, the program should map the data type as an ARRAY 

## EVERY Other valid JSON Data Type ( STRING, NUMBER, BOOLEAN, NULL, ARRAY (including empty arrays ([]), and JSON Objects))
- All other valid JSON Data Types are interpreted as their corresponding JSON data type in the output schema type 
    - example the type of <strong>[]</strong> is interpreted as "array" 
    - type of <strong>False</strong> is interpreted as "boolean"
    - type of <strong>{ "name" : "data2bot"}</strong> is interpreted as "object"

## PLEASE NOTE
- THERE IS A FUNCTION IN main.py THAT MAPS OUT ONLY TO THE PROPERTIES STATED IN PROBLEM.md i.e (STRING , NUMBER, INTEGER AND ENUM) HENCE THEY ARE TWO create_schema.py FUNCTIONS, IF THATS THE DESIRED OUTCOME KINDLY COMMENT OUT THE FUNCTION create_schema.py AND COMMENT THE FUNCTION create_schema.py BELOW IT.

# Calling the function
- The program runs on the command line. Entry point is via main.py.
- navigate to dir example <strong>cd python_engineer_experienced_professional</strong>
- Two arguments are required.<strong>./data/input_src.json</strong>
    * the source : -> Name of the file for which we want a schema. It is assumed the file lives in the folder (data)
        - The path to the file as well as the extension name is not required e.g file in  will be given as <strong>input_src</strong>
    * the sink : -> Name of the file which we want to dump the resulting schema in. The resulting file will live in the folder schema
        - The path to the file as well as the extension name is not required e.g to dump result in <strong>./schema/output_src.json</strong> all we need is <strong>input_src</strong>

## Example Execution(main.py)
- python <strong>main.py</strong> --source <strong>data_1</strong> --sink <strong>schema_1</strong>
* loads file from <strong>/data/data_1.json</strong> dumps result in <strong>/schema/schema_1.json</strong>

## Example Execution(main_test.py)
- python main_test.py
- imports variables to run test from <strong>test_data.py</strong> and units to test from <strong>main.py</strong>
