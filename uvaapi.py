import requests
import json
import jsoncache

problems = jsoncache.get("problems")

def rebuild_problems():
    p = json.loads(api_get("p"))
    nd = {}
    for i in p:
        nd[i[0]] = {"problem_number": i[1], "title": i[2]}
    return nd


def api_get(endpoint):
    return requests.get("http://uhunt.felix-halim.net/api/" + endpoint).text.strip()

def get_uid(username):
    return api_get("uname2uid/" + username)

def _clean_sub(sub):
    verdicts = {
        0  : "Compiling",
        10 : "Submission error",
        15 : "Can't be judged",
        20 : "In queue",
        30 : "Compile error",
        35 : "Restricted function",
        40 : "Runtime error",
        45 : "Output limit",
        50 : "Time limit",
        60 : "Memory limit",
        70 : "Wrong answer",
        80 : "Presentation Error",
        90 : "Accepted",
    }

    cleaned = {
        "problem": problems[str(sub[1])],
        "verdict": verdicts[sub[2]],
        "runtime": str(sub[3]) + "ms"
    }
    return cleaned

def submissions(uid, n):
    subs = reversed(json.loads(api_get("subs-user-last/"+uid+"/"+str(n)))["subs"])

    return map(_clean_sub, subs)

if not problems:
    jsoncache.put("problems", problems, 24)
    problems = jsoncache.get("problems")
