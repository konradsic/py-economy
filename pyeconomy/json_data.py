"""
MIT License

Copyright (c) 2022 Konrad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import typing as t
import os

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
    with open("./economy/" + file, 'r') as f:
        json_file = json.load(f)
    return json_file

def save_json_file(file: str, keys: dict):
    """
    Saves json file
     
    Arguments
    ---------
        file: :class:`str`
            A file to save.
        keys: :class:`dict`
            A file to save.
    
    Returns
    ---------
        new_file: :class:`dict`
            JSON object as a python dictionary.
    """
    with open("./economy/" + file, 'w') as f:
        json.dump(keys, f)
    with open("./economy/" + file, "r") as f:
        new_file = json.load(f)
    return new_file
        

def create_economy_files() -> None:
    """
    Creates required JSON files. 
    
    Returns
    ---------
        None
    """
    files = ["economy_data.json", "config.json"]
    try:
        os.mkdir("./economy")
    except:
        pass
    for file in files:
        with open("./economy/" + file, 'w') as f:
            f.write("{}")
    return None
