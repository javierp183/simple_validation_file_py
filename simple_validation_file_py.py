""" Output Templater """
from string import Template

#Dict with common common key and values.
words = {
    'var': 'mundo',
    'name': 'javier'
}

class File:
    def __init__(self,file):
        #self.content = self.__open_content__()
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

        
        
        
        
a = File("noexiste.txt")
a.exist()
a.content()