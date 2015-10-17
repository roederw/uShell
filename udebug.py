import requests
import json
from bs4 import BeautifulSoup
import headers

'''

A wrapper for functions which interface with www.udebug.com

'''

BASE_URL = "http://www.udebug.com/"

# Given a problem number and test data, return the expected output
# according to udebug
def get_answers(problem_num, form_data, tests):
    url = BASE_URL + "UVa/" + str(problem_num)

    form_data['input_data'] = tests
    form_data['op'] = "Go!"
    h = headers.udebug_headers
    h["Referer"] =  url

    resp = requests.post(url, data=form_data, headers=h)
    soup = BeautifulSoup(resp.text, "html.parser")
    return soup.find("div", {"id": "output-data-inner"}).pre.text

# Make a get request to a specified udebug endpoint
def udebug_get(endpoint):
    return requests.get(BASE_URL + str(endpoint)).text

# Get random test input for a given problem
def get_testcases(endpoint):
    return udebug_get("get-random-critical-input/random/" + endpoint).strip()

# parses form info to be used to make POST requests
def get_form_data(problem_num):
    html = udebug_get("UVa/" + problem_num)
    soup = BeautifulSoup(html, "html.parser")
    form = soup.find_all("form")[1]
    return {e['name']: e.get('value', '') for e in form.find_all("input", {'name': True})}

# Given a UVa problem number return
# the set of test cases provided by
# udebug as well as the expected output
def testcases(problem_num):
    d = get_form_data(problem_num)

    tests = json.loads(get_testcases(d['problem_nid']))
    if tests == "":
        return tests, None
    answers = get_answers(problem_num, d, tests)
    return tests, answers
