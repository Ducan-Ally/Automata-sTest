import ply.yacc as yacc
from FakeCompiler.lexer import tokens
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

def parseMethod():
    parser = yacc.yacc()
    name = input("Escriba el nombre del archivo con el código fuente ")
    file = open(name, 'r')
    line = file.read()
    while True:
        parser.parse(line)
        break

def p_Start1(p):
    'FakeProgram : names EQUAL METODO LEFTPARENTHESIS INT RIGHTPARENTHESIS continuation'
    fakeStructure.addStatemet(Metodo(p[1],p[5]))

def p_Start2(p):
    'FakeProgram : PRINT NAME continuation'
    fakeStructure.addStatemet(Print(p[2]))

def p_names1(p):
    'names : NAME COMMA names'
    p[0] = list()
    p[0].extend(p[3])
    p[0].append(p[1])

def p_names2(p):
    'names : NAME'
    p[0] = list()
    p[0].append(p[1])

def p_continuation1(p):
    'continuation : NEWLINE FakeProgram'

def p_continuation2(p):
    'continuation : empty'

def p_error(p):
    if p:
        print(bcolors.FAIL+"Error:" +bcolors.ENDC ,bcolors.HEADER + p.type+ bcolors.ENDC, bcolors.BOLD + "", p.value,"" + bcolors.ENDC, bcolors.WARNING + "Sucedió en la línea:" + bcolors.ENDC, bcolors.UNDERLINE + "" ,p.lineno,"" + bcolors.ENDC)
         # Just discard the token and tell the parser it's okay.
        parser.errok()

def p_empty(p):
    'empty : '

fakeStructure = FakeStructures()