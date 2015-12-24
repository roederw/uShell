from os.path import expanduser
import json
import utils
import constants

SETTINGS_PATH = expanduser("~") + "/.uvashell"

class uvasettings():
    def __init__(self):
        try:
            f = open(SETTINGS_PATH, "r")
            self.d = json.loads(f.read())
        except Exception as e:
            self.d = self.prompt_info()
            self.write_out()

    def prompt_info(self):
        print "No config file found, creating at: " + SETTINGS_PATH
        print "Enter your desired UVA Username:"
        username = raw_input()

        print "Now, enter your default submission language (you have the ability to change this later):"
        print constants.language
        language = raw_input()

        ret = {
            'username': username,
            'language': language
        }
        return ret;

    def write_out(self):
        utils.write_file(SETTINGS_PATH, json.dumps(self.d))

    def __getitem__(self, i):
        return self.d[i]

    def __setitem__(self, key, value):
        self.d[key] = value
        self.write_out()
