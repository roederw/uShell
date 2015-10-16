#!/usr/bin/env python
from uvaclient import uvaclient
import sys

class command():
    def __init__(self, func, h):
        self.func = func
        self.h = h

    def __call__(self, *args):
        self.func(*args)

def sub_command(client, args):
    if (len(args) > 0):
        client.submissions(args[0])
    else:
        client.submissions()

def submit_command(client, args):
    print "Logging in..."
    client.login()
    print "Submitting..."
    client.submit(args[0], args[1])
    print "Done!"

if __name__ == "__main__":
    commands = {
        "subs": command(sub_command, "Usage: uva subs [n]"),
        "submit": command(submit_command, "Usage: submit <problem_number> <source_file>")
    }

    command = sys.argv[1]
    sys.argv = sys.argv[2:]

    if command in commands:
        u = uvaclient()
        commands[command](u, sys.argv)

    else:
        print "Commands:"
        for name in commands.keys():
            print "\t" + name + " - " + commands[name].h
