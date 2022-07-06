# data2struct

Reads a JSON file sniffs the schema of the JSON file into another JSON file.

## Dependecies

The program has no dependency save python >= 3.6


## Usage

The program runs on the command line. Entry point is via main.py.
navigate to dir example cd python_engineer_experienced_professional
two arguments are required../data/input_src.json
the source : -> Name of the file for which we want a schema. It is assumed the file lives in the folder (data)
The path to the file as well as the extension name is not required e.g file in will be given as input_src
the sink : -> Name of the file which we want to dump the resulting schema in. The resulting file will live in the folder schema
The path to the file as well as the extension name is not required e.g to dump result in ./schema/output_src.json all we need is input_src

## Example Execution(main.py)

python main.py --source data_1 --sink schema_1
loads file from /data/data_1.json dumps result in /schema/schema_1.json

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License

Mars Software

