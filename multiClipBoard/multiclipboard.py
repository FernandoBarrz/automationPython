#!/usr/bin/env python3


from ast import Try
import sys
import json

from simplejson import load
import pyperclip as pc

SAVED_DATA = 'clipboard.json'

def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:

    data = load_data(SAVED_DATA)

    if sys.argv[1] == 'save':
        key = input('Enter a key: ')
        data[key] = pc.paste()
        save_items(SAVED_DATA, data)
        print("Data has been Saved")
    elif sys.argv[1] == 'load':
        key = input('Enter a key: ')
        if key in data: 
            pc.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print("Key doesn't exist")
    elif sys.argv[1] == 'list':
        print(data)
    else:
        print('Bad input')
else:
    print(f'Program uses exactly one argument')



