from FakeCompiler.parser import *
from FakeCompiler.fakeStructure import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def semantic():
    parseMethod()
    fakeStructure.printStatements()

    for x in range(0, len(fakeStructure.statements)):
        if type(fakeStructure.statements[x]) is Metodo:
            metodoChecker(fakeStructure.statements[x])
        elif type(fakeStructure.statements[x]) is Print:
            printChecker(fakeStructure.statements[x])


def metodoChecker(metodo):
    if 0 < metodo.variableCounter and metodo.variableCounter <= 5:
        if 0 < len(metodo.variables) and len(metodo.variables) <= 5:
            if metodo.variableCounter == len(metodo.variables):
                variablesList.extend(metodo.variables)
            else:
                print(bcolors.FAIL + "Recieved parameters:" + bcolors.ENDC, len(metodo.variables),
                      bcolors.FAIL + "expected:" + bcolors.ENDC, metodo.variableCounter)
        else:
            print(bcolors.FAIL + "The number of variables have to be between 1 and 5, but instead recieved:" + bcolors.ENDC,
                len(metodo.variables))
    else:
        print(bcolors.FAIL + "The metodo parameter have to be between 1 and 5, but instead recieved:" + bcolors.ENDC,
              metodo.variableCounter)

def printChecker(p):
    found = False
    for i in range(0,len(variablesList)):
        if p.name == variablesList[i]:
            found = True

    if not found:
        print(bcolors.FAIL + "The variable:"+bcolors.ENDC,p.name,bcolors.FAIL + "doesnt exist."+bcolors.ENDC)

variablesList = list()
semantic()

#To run: ../Trials/trial1.fake
#To run: ../Trials/trial2.fake
#To run: ../Trials/trial3.fake
#To run: ../Trials/trial4.fake