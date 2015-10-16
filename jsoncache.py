from datetime import datetime, timedelta
import json

def put(code, obj, expires_in_hours):
    expires = datetime.now() + timedelta(hours = expires_in_hours)
    data = {
        "expires": expires.toordinal(),
        "data": obj
    }
    f = open("cache/" + code + ".json", "w")
    f.write(json.dumps(data))
    f.close()

def get(code):
    try:
        d = json.loads(open("cache/" + code + ".json", "r").read())
    except:
        return False

    if datetime.now() > datetime.fromordinal(d["expires"]):
        return False
    return d["data"]
