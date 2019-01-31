import platform
import os
import time
from pathlib import Path

class Statter():
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.location = str(Path.home())
        if platform.system() == "Linux":
            self.location += "/.bencher/"
        else:
            self.location += "\\.bencher\\"
        self.filename = self.location + suite_name + ".bench"
        self.file = open(self.filename, "r")

    def sum(self):
        data = self.file.read().split("\n")            
        return sum([i.split(",")[2] for i in data])
    def avg(self):
        data = self.file.read().split("\n")
        times = [i.split(",")[2] for i in data]
        return sum(times) / len(times)
