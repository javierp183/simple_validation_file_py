""" Output Templater """
from string import Template

class File:
    def __init__(self,file):
        self.file = file

    def exist(self):
        try:
            f = open(self.file)
            if f.read():
                return True

        except IOError:
            return False
    
    def content(self):
        return True if open(self.file).readline() != "" else False