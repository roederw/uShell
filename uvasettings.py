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
            utils.write_file(SETTINGS_PATH, json.dumps(self.d))

    def prompt_info(self):
        print "No config file found, creating at: " + SETTINGS_PATH
        print "uva username:"
        username = raw_input()

        print "default submission language:"
        print constants.language
        language = raw_input()

        ret = {
            'username': username,
            'language': language
        }
        return ret;

    def __getitem__(self, i):
        return self.d[i]
