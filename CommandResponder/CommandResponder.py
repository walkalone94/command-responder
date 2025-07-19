#!/usr/bin/env python3

from cortexutils.responder import Responder
import subprocess

class CommandResponder(Responder):
    def __init__(self):
        Responder.__init__(self)

    def run(self):
        command = self.get_param("data", None)
        result = subprocess.getoutput(command)
        self.report({"command": command, "output": result})

if __name__ == '__main__':
    CommandResponder().run()

