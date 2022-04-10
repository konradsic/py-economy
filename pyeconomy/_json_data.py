import json
import typing as t

def load_json_file(file : str) -> t.Dict[str, str]:
    """
    Loads json file
     
    Arguments
    ---------
        file: :class:`str`
            A file to load.
    
    Returns
    ---------
        json_file: :class:`dict`
            JSON object as a python dictionary.
    """
    with open(file, 'r') as f:
        json_file = json.load(f)
    return json_file

def create_economy_files(directory) -> None:
    dir = directory
    if not dir.endswith('/'):
        dir = dir + "/"
    files = ["economy_data.json", "config.json"]
    for file in files:
        with open(dir + file, 'w') as f:
            json.dump({}, f)
    return None