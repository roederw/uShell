from datetime import datetime, timedelta
import json
import os

path = os.path.dirname(os.path.realpath(__file__)) + "/"

def put(code, obj, expires_in_hours):
    expires = datetime.now() + timedelta(hours = expires_in_hours)
    data = {
        "expires": expires.toordinal(),
        "data": obj
    }
    f = open(path + "cache/" + code + ".json", "w")
    f.write(json.dumps(data))
    f.close()

def get(code):
    try:
        d = json.loads(open(path + "cache/" + code + ".json", "r").read())
    except:
        return False

    if datetime.now() > datetime.fromordinal(d["expires"]):
        return False
    return d["data"]
