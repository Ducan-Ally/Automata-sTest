# coding=utf-8

import ply.lex as lex

#Reserved words
reserved = {
    'metodo' : 'METODO',
    'print' : 'PRINT'
}

#Token's list
tokens = [
    'COMMA',
    'EQUAL',
    'INT',
    'NAME',
    'NEWLINE',
    'LEFTPARENTHESIS',
    'RIGHTPARENTHESIS'
] + list(reserved.values())

#Regular expresions

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_]([a-zA-Z_0-9]|_)*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    t.value = "NEWLINE"
    t.type = "NEWLINE"
    return t

t_COMMA = r'\,'
t_EQUAL = r'\='
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_ignore = r' '

def t_error(t):
    print("Lexical error in line",t.lexer.lineno,"-- Invalid character:",t.value[:1])
    t.lexer.skip(1)

lexer = lex.lex()


'''
name = input("Escriba el nombre del archivo con el código fuente ")
file = open(name, 'r')
line = file.read()
lexer.input(line)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
'''