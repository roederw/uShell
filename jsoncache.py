from datetime import datetime, timedelta
import json
import os

'''

A simple persistent cache manager for JSON objects

'''

path = os.path.dirname(os.path.realpath(__file__)) + "/"

# Adds an object to the cache with a specified code and
# sets its expiration time
def put(code, obj, expires_in_hours):
    expires = datetime.now() + timedelta(hours = expires_in_hours)
    data = {
        "expires": expires.toordinal(),
        "data": obj
    }
    f = open(path + "cache/" + code + ".json", "w")
    f.write(json.dumps(data))
    f.close()

# Retrevies an object from the cache
# If the object cannot be found OR the object has expired false will be returned
# Otherwise you will recieve the parsed object back
def get(code):
    try:
        d = json.loads(open(path + "cache/" + code + ".json", "r").read())
    except:
        return False

    if datetime.now() > datetime.fromordinal(d["expires"]):
        return False
    return d["data"]
