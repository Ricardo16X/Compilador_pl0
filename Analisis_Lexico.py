import ply.lex as lex
import re
import codecs
import os
import sys
# Lista de Reservadas
reservadas = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
        'VAR','PROCEDURE','OUT','IN','ELSE']
# Lista de Tokens.
tokens =    reservadas + ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
        'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
        'LPARENT','RPARENT','COMMA','SEMMICOLOM',
        'DOT','UPDATE']

t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='
# Función de Identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t
# Función de Comentarios
def t_COMMENT(t):
    r'\#.*'
# Función de Números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Función de Espacios en blanco
def t_blank_(t):
    r'\s+'
# Función de Saltos de Línea
def t_newLine(t):
    r'\n+'
# Función de Errores
def t_error(t):
    print("Caracter ilegal " + t.value[0])
    t.lexer.skip(1)
# Función de Buscar Fichero
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    # Ciclo For
    for base,dirs,files in os.walk(directorio):
        ficheros.append(files)
    
    for file in files:
        print(str(cont) + '. ' + str(file))
        cont = cont + 1
    
    while respuesta == False:
        numArchivo = input('\nNúmero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print('Has escogido \n' + files[int(numArchivo) - 1])
    return files[int(numArchivo) - 1]

# Buscar dentro del fichero o directorio
# Escritorio
directorio = 'C:\\Users\\Ordenador\\Documents\\Python\\Compilador pl0\\test\\'
# Portatil
#directorio = 'C:\\Users\\Ordenador\\Escritorio\\carpeta xd\\test\\'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fileOpen = codecs.open(test,"r","utf-8")
cadena = fileOpen.read()
fileOpen.close()
# Trabajando sobre la variable cadena
analizador = lex.lex()
analizador.input(cadena)
# Leyendo cadena o trabajando cadena
while True:
    tok = analizador.token()
    if not tok: break
    print(tok)