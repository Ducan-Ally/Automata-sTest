from FakeCompiler.fakeStructure import *
from FakeCompiler.semantic import *

dataList = list()
dataListI = list()
dataListO = list()
file = open("compiledFake.asm","w+")

def codeGeneration():
    semantic()

    for x in range(0, len(fakeStructure.statements)):
        if type(fakeStructure.statements[x]) is Metodo:
            generateMetodoCode(fakeStructure.statements[x])
        elif type(fakeStructure.statements[x]) is Print:
            generatePrintCode(fakeStructure.statements[x])

    file.write("li $v0, 10\n")
    file.write("syscall\n")

def generateMetodoCode(metodo):
    dataList.extend(metodo.variables)
    file.write(".data\n")
    for i in range(0,len(dataList)):
        file.write(dataList[i]+"I: .asciiz \"Insert digit for "+dataList[i]+": \\n\"\n")
        dataListI.append(dataList[i]+"I")
        file.write(dataList[i]+"O: .asciiz \"The value in " + dataList[i] + " is: \\n\"\n")
        dataListO.append(dataList[i]+"O")

    file.write(".text\n")
    file.write("main:\n")

    for i in range(0,len(dataList)):
        file.write("li $v0, 4\n")
        file.write("la $a0, "+dataListI[i]+"\n")
        file.write("syscall\n")

        file.write("li $v0, 5\n")
        file.write("syscall\n")
        file.write("move $s"+str(i)+", $v0\n")

def generatePrintCode(p):
    i = 0
    while (i < len(dataList) and dataList[i] != p.name):
        i = i + 1
    if i < len(dataList) :
        file.write("li $v0, 4\n")
        file.write("la $a0, " + dataListO[i] + "\n")
        file.write("syscall\n")

        file.write("li $v0, 1\n")
        file.write("move $a0, $s"+ str(i)+"\n")
        file.write("syscall\n")

codeGeneration()


#To run: ../Trials/trial1.fake
#To run: ../Trials/trial2.fake
#To run: ../Trials/trial3.fake
#To run: ../Trials/trial4.fake