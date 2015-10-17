import requests
from bs4 import BeautifulSoup
import getpass
import secret
import uvaapi as api

BASE_URL   = "https://uva.onlinejudge.org/"
LOGIN_URL  = "https://uva.onlinejudge.org/index.php?option=com_comprofiler&task=login"
SUBMIT_URL = BASE_URL + "index.php?option=com_onlinejudge&Itemid=25&page=save_submission"
API_URL    = "http://uhunt.felix-halim.net/api/"

def get_headers():
    headers = {
        'Accept-Charset': 'utf-8,ISO-8859-1',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent' :  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) "+
                        "AppleWebKit/537.17 (KHTML, like Gecko) "+
                        "Chrome/24.0.1312.57 Safari/537.17",
        "Accept" : "text/html, application/xml, text/xml, */*",
    }
    return headers


def merge_dicts(d1, d2):
    for k in d2.keys():
        d1[k] = d2[k]
    return d1

class uvaclient:
    def __init__(self):
        self.session = requests.Session()
        self.username = secret.username
        self.uid = api.get_uid(self.username)

    def prompt_password(self):
        return getpass.getpass("Password: ")

    def _post(self, url, data, custom_headers=None, redirects=True):
        custom_headers = custom_headers or {}
        headers = merge_dicts(get_headers(), custom_headers)

        return self.session.post(url, data=data, headers=headers, allow_redirects=redirects)

    def _get(self, url, custom_headers=None, redirects=True):
        custom_headers = custom_headers or {}
        headers = merge_dicts(get_headers(), custom_headers)

        return self.session.get(url, headers=headers, allow_redirects=redirects)


    def _login_data(self):
        soup = BeautifulSoup(self._get(BASE_URL).text, "html.parser")
        login_form = soup.find_all("form")[0]

        d = {e['name']: e.get('value', '') for e in login_form.find_all("input", {'name': True})}
        d['username'] = self.username
        d['passwd'] = self.prompt_password()
        return d

    def login(self):
        data = self._login_data()
        self._post(LOGIN_URL, data, {'Referer': BASE_URL}, False)

    def submit(self, problemid, language, f):
        data = {
            "localid":   problemid,
            "code":      open(f, "r").read(),
            "language":  language,
            "codeupl":   "",
            "problemid": "",
            "category":  ""
        }
        self._post(SUBMIT_URL, data, {"Referer": SUBMIT_URL})

    def submissions(self, n = 3):
        resp = api.submissions(self.uid, n)

        for i in resp:
            print i["problem"]["title"] + " - " + i["verdict"] + " - " + i["runtime"]

    def leaderboard(self, problem_number):
        print "Problem " + str(problem_number) + ": " + api.get_problem_name(problem_number) 
        resp = api.leaderboard(problem_number, 10)
        for i in resp:
            print "Rank: " + str(i['rank'])  + " User: " + i['uname'] 

    def user_submissions_problem(self, user, problem_number):
        resp = api.user_submissions_problem(user, problem_number)
        for i in resp:
            print "Submission ID: %-12s Verdict: %-20s Runtime: %-11s Language Used: %-10s" % (i["submission_id"], i["verdict"], i["runtime"], i["language"])
