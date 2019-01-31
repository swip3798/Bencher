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
        file = open(self.filename, "r")
        self.data = file.read().split("\n")

    def sum(self):
        return sum([float(i.split(",")[2]) for i in self.data[:-1]])

    def avg(self):
        times = [float(i.split(",")[2]) for i in self.data[:-1]]
        return sum(times) / len(times)

    def count(self):
        return len(self.data) - 1
