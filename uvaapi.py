from bs4 import BeautifulSoup
from urllib import urlopen
import requests
import json
import jsoncache
import constants

'''

A wrapper for functions which interface with www.uhunt.felix-halim.net/api

'''

# Make a get request to a given endpoint in the API
def api_get(endpoint):
    return requests.get("http://uhunt.felix-halim.net/api/" + endpoint).text.strip()

# Build a problem dictionary, will only actually make request once
# every 24 hours
def fetch_problems():
    if not jsoncache.get("problems"):
        p = json.loads(api_get("p"))
        nd = {}
        for i in p:
            nd[i[0]] = {"problem_number": i[1], "title": i[2]}
        jsoncache.put("problems", nd, 24)
    return jsoncache.get("problems")

problems = fetch_problems()

# Convert a UVa username to a uid (needed for other endpoints)
def get_uid(username):
    return api_get("uname2uid/" + username)

# Convert a Uva problem number to a pid (needed for other endpoints)
def get_pid(problem_num):
    return json.loads(api_get("p/num/" + problem_num))['pid']

def get_problem_name(problem_num):
    return json.loads(api_get("p/num/" + problem_num))['title']

# Takes a submission and converts it to a readable format
def _clean_sub(sub):
    cleaned = {
        "problem": problems[str(sub[1])],
        "verdict": constants.verdicts[sub[2]],
        "runtime": str(sub[3]) + "ms",
        "language": constants.language[sub[5]],
        "submission_id": sub[0]
    }
    return cleaned

# Retrieves the last n submissions for a given user
def submissions(uid, n):
    subs = reversed(json.loads(api_get("subs-user-last/" + uid + "/"+str(n)))["subs"])
    return map(_clean_sub, subs)

def leaderboard(problem_num, n):
    leaders = json.loads(api_get("p/rank/" + str(get_pid(problem_num)) + "/1/" + str(n)))
    return leaders

def user_submissions(user, n = 10):
    uid = get_uid(user)
    subs = reversed(json.loads(api_get("subs-user-last/" + uid + "/" + str(n)))["subs"])
    return map(_clean_sub, subs)

def user_submissions_problem(user, problem_num):
    uid = get_uid(user)
    subs = reversed(json.loads(api_get("subs-pids/" + uid + "/" + str(get_pid(problem_num)) + "/0"))[uid]["subs"])
    return map(_clean_sub, subs)
