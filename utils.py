from os.path import expanduser
import json

def write_file(path, contents):
    with open(path, "w") as f:
        f.write(contents)

def merge_dicts(d1, d2):
    for k in d2.keys():
        d1[k] = d2[k]
    return d1
