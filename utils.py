from os.path import expanduser
import json

SETTINGS_FILE = expanduser("~") + "/.uvashell"

def write_file(path, contents):
    with open(path, "w") as f:
        f.write(contents)

def merge_dicts(d1, d2):
    for k in d2.keys():
        d1[k] = d2[k]
    return d1

def get_username():
    with open(SETTINGS_FILE, "r") as f:
        data = json.loads(f.read())
        return data['username']

def get_language():
    with open(SETTINGS_FILE, "r") as f:
        data = json.loads(f.read())
        return data['language']

def set_username(username):
    with open(SETTINGS_FILE, "r+") as f:
        data = json.load(f)
        data['username'] = username
        write_file(SETTINGS_FILE, json.dumps(data))

def set_language(language):
    with open(SETTINGS_FILE, "r+") as f:
        data = json.load(f)
        data['language'] = language
        write_file(SETTINGS_FILE, json.dumps(data))
