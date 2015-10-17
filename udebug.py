import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "http://www.udebug.com/"

def get_answers(problem_num, form_data, tests):
    url = BASE_URL + "UVa/" + str(problem_num)

    headers = {
        'Accept-Charset': 'utf-8,ISO-8859-1',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent' :  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) "+
                        "AppleWebKit/537.17 (KHTML, like Gecko) "+
                        "Chrome/24.0.1312.57 Safari/537.17",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": url
    }

    form_data['input_data'] = tests
    form_data['op'] = "Go!"

    resp = requests.post(url, data=form_data, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup.find("div", {"id": "output-data-inner"}).pre.text

def udebug_get(endpoint):
    return requests.get(BASE_URL + str(endpoint)).text

def get_testcases(endpoint):
    return udebug_get("get-random-critical-input/random/" + endpoint).strip()

def get_form_data(problem_num):
    html = udebug_get("UVa/" + problem_num)
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find_all("form")[1]
    return {e['name']: e.get('value', '') for e in form.find_all("input", {'name': True})}

def testcases(problem_num):
    d = get_form_data(problem_num)

    tests = json.loads(get_testcases(d['problem_nid']))
    if tests == "":
        return tests, None
    answers = get_answers(problem_num, d, tests)
    return tests, answers
