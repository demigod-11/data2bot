import json 
import argparse 

def parse_json(file : str) -> dict:
    '''
        opens and loads Json file to python (raise error if any)
    '''
    try:
        with open(file) as f:
            return json.load(f)
  
    except Exception as e:
        raise e

def clean_data(data : dict) -> dict:
    '''
        returns the value of key message in data
    '''
    try:        
        return data['message']
    except Exception as e:
        raise e

def hold_schema(dType: str) -> dict:
    '''
        holds schema of Json
    '''
    return {
        "type": dType,
        "tag": "",
        "description": "",
        "required": False}

# comment out this code 
# if requirement is specific to just STRING ARRAY ENUM and INTEGER 
# then comment the create_schema function underneath this.


# def create_schema(document : dict) -> dict:
#     if type(document) != dict:
#         raise Exception('')
#     result = {}
#     for key, val in document.items():
#         if type(val) == str:
#             result[key] = hold_schema('string')
#         elif type(val) == int:
#             result[key] = hold_schema('integer')
        
#         elif type(val) == list:
#             if len(val) == 0:
#                 pass
#             elif type(val[0]) == str:
#                 result[key] = hold_schema('enum')
#             elif type(val[0]) == dict:
#                 result[key] = hold_schema('array')
            

#     return result 

    
def create_schema(document : dict) -> dict:
    '''
        Creates schema for each key with their coresponding datatype
    '''
    result = {}
    if type(document) != dict:
        raise Exception("Invalid datatype")

    for key, val in document.items():
        if type(val) == str:
            result[key] = hold_schema('string')
        elif type(val) == int:
            result[key] = hold_schema('integer')
        
        elif type(val) == float:
            result[key] = hold_schema('number')
        
        elif type(val) == None:
            result[key] = hold_schema('null')
            
        elif type(val) == bool:
            result[key] = hold_schema('boolean')
        
        elif type(val) == list:
            if len(val) == 0:
                result[key] = hold_schema('array')
            elif type(val[0]) == str:
                result[key] = hold_schema('enum')
            elif type(val[0]) == dict:
                result[key] = hold_schema('array')
            else:
                result[key] = hold_schema('array')
        elif type(val) == dict:
            result[key]  =  hold_schema('object')
            result[key]["properties"] = create_schema(val)
        else:
            raise Exception("Invalid data type")
            
    return result 

def WritetoJson(document: dict, file: str) -> int:
    '''
        Write schema into a Json File
    '''
    try: 
        with open(file, 'w') as f:
            json.dump(document, f, indent=4)
            return 0
    except Exception as e:
        raise e

def run():
    # Command line arguments
    parser = argparse.ArgumentParser(description='Extract from Json source transform load to Json File')
    parser.add_argument('--source', required=True, help='Specify the Json source File name in data directory')
    parser.add_argument('--sink', required=True, help='Specify the destination Json File name would be saved in Schema directory')

    opts  = parser.parse_args()

    # Static source and sink
    source = './data/{0}.json'.format(opts.source)
    sink = './schema/{0}.json'.format(opts.sink)

    # running pipeline
    dataset = parse_json(source)
    cleaned_data = clean_data(dataset)
    WritetoJson(create_schema(cleaned_data), sink)

    return 0

    

if __name__ == '__main__':
    print("Creating Schema ...")
    run()
    print("Done")