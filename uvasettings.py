from os.path import expanduser
import json
import utils

SETTINGS_PATH = expanduser("~") + "/.uvashell"

class uvasettings():
    def __init__(self):
        try:
            home = expanduser("~")
            f = open(home + "/.uvashell", "r")
            self.d = json.loads(f.read())
        except Exception as e:
            self.d = self.prompt_info()
            utils.write_file(expanduser("~") + "/.uvashell", json.dumps(self.d))

    def prompt_info(self):
        print "uva username:"
        username = raw_input()

        print "default submission language:"
        language = raw_input()

        ret = {
            'username': username,
            'language': language
        }
        return ret;

    def __getitem__(self, i):
        return self.d[i]
