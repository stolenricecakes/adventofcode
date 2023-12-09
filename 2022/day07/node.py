class Node:
    isDirectory = False
    name = ""
    size = 0
    calculatedSize = 0
    parent = None

    def __init__(self, parent = None, isDirectory=None, name=None, size=0):
        self.parent = parent
        self.isDirectory = isDirectory
        self.name = name
        self.size = size
        self.children = {}

    def getSize(self):
        if not self.isDirectory:
           return self.size
        else:
           self.calculatedSize = 0
           for kid in self.children.values():
               self.calculatedSize = self.calculatedSize + kid.getSize()

           return self.calculatedSize

