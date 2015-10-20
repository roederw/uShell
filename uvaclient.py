import requests
from bs4 import BeautifulSoup
import getpass
import settings
import uvaapi as api
import udebug
import headers
import utils

'''

Main level of abstraction for interfacing with UVa.

'''

BASE_URL   = "https://uva.onlinejudge.org/"
LOGIN_URL  = BASE_URL + "index.php?option=com_comprofiler&task=login"
SUBMIT_URL = BASE_URL + "index.php?option=com_onlinejudge&Itemid=25&page=save_submission"

class uvaclient:
    def __init__(self):
        # Create a session for making requests
        # Nessesary to persist login information
        self.session = requests.Session()
        self.username = settings.username
        self.uid = api.get_uid(self.username)

    def prompt_password(self):
        return getpass.getpass("Password: ")

    # Helpers for making post requests through our session with
    # an option for adding custom headers or overwriting defaults
    def _post(self, url, data, custom_headers=None, redirects=True):
        custom_headers = custom_headers or {}
        h = utils.merge_dicts(headers.uva_headers, custom_headers)

        return self.session.post(url, data=data, headers=h,
                allow_redirects=redirects)

    def _get(self, url, custom_headers=None, redirects=True):
        custom_headers = custom_headers or {}
        h = utils.merge_dicts(headers.uva_headers, custom_headers)

        return self.session.get(url, headers=h, allow_redirects=redirects)

    # Query the homepage for login tokens and fill in username and password
    # UVa generates some random token for security so we need to load the page
    # and grab it before making our login request
    def _login_data(self):
        soup = BeautifulSoup(self._get(BASE_URL).text, "html.parser")
        login_form = soup.find_all("form")[0]

        d = {e['name']: e.get('value', '') for e in login_form.find_all("input", {'name': True})}
        d['username'] = self.username
        d['passwd'] = self.prompt_password()
        return d

    # Grab nesseary security info and then authenticate
    def login(self):
        data = self._login_data()
        self._post(LOGIN_URL, data, {'Referer': BASE_URL}, False)
        if (len(self.session.cookies) == 1):
            print "Authentication failed"
            self.login()

    def get_baseurl(self):
            return BASE_URL

    def get_problem_name(self, problem_num):
        return api.get_problem_name(problem_num)

    # Submits a problem with the given parameters
    # Must be logged in for this to work
    # see settings.py for a list of language codes
    def submit(self, problemid, f, language = settings.language):
        data = {
            "localid":   problemid,
            "code":      open(f, "r").read(),
            "language":  language,
            "codeupl":   "",
            "problemid": "",
            "category":  ""
        }
        self._post(SUBMIT_URL, data, {"Referer": SUBMIT_URL})

    # Proxy calls to the API
    def submissions(self, n = 3):
        return api.submissions(self.uid, n)

    def leaderboard(self, problem_number, n = 10):
        return api.leaderboard(problem_number, n)

    def user_submissions(self, user):
        return api.user_submissions(user)

    def user_submissions_problem(self, user, problem_number):
        return api.user_submissions_problem(user, problem_number)

    def testcases(self, problem_num):
        return udebug.testcases(problem_num)
