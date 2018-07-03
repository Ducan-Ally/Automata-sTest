class FakeStructures:
    def __init__(self):
        self.statements = []

    def addStatemet(self,statement):
        self.statements.insert(0,statement)

    def printStatements(self):
        for x in range (0, len(self.statements)):
            self.statements[x].printObject()

class Metodo:
    id = "METODO"
    def __init__(self,variables,variableCounter):
        self.variables = variables
        self.variableCounter = variableCounter

    def printObject(self):
        print(self.variableCounter)
        for x in range (0, len(self.variables)):
            print(self.variables[x])

class Print:
    id = "PRINT"
    def __init__(self,name):
        self.name = name

    def printObject(self):
        print(self.name)