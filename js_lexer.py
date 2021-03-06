import ply.lex as lex
import os

# lista de tokens
tokens = (

    # Palabras Reservadas
    'FUNCTION',
    'DOCUMENT',
    'CONSOLE',
    'LOG',
    'BREAK',
    'TRUE',
    'FALSE',
    'NEW',
    'OBJECT',
    'ARRAY',
    'NULL',
    'THIS',
    'VAR',
    'LET',
    'CONST',
    'ELSE',
    'IF',
    'STRING',
    'RETURN',
    'VOID',
    'WHILE',
    'FOR',

    # Symbolos
    'HASH',
    'ID',
    'POINT',
    'PLUS',
    'PLUSPLUS',
    'MINUS',
    'MINUSMINUS',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'SEMICOLON',
    'COMMA',
    'LGREATER',
    'RGREATER',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'QUOTES',


    #Otros
    'TRHOW',
    'CATCH',
    'FINALLY',
    'TYPEOF',
    'DEFAULT',
    'JSON',
    'MATH',
    'INSTANCEOF',
    'NUMBER',
)


# Reglas de Expresiones Regulares para tokens

t_PLUS = r'\+'
t_MINUS = r'-'
t_MINUSMINUS = r'\-\-'
t_POINT = r'\.'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_QUOTES = r'\"'

def t_INCLUDE(t):
    r'include'
    return t


def t_FUNCTION(t):
    r'function'
    return t

def t_DOCUMENT(t):
    r'document'
    return t

def t_CONST(t):
    r'const'
    return t

def t_LET(t):
    r'let'
    return t

def t_VAR(t):
    r'var'
    return t

def t_VOID(t):
    r'void'
    return t

def t_CONSOLE(t):
    r'console'
    return t

def t_LOG(t):
    r'log'
    return t

def t_NULL(t):
    r'null'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_DEFAULT(t):
    r'default'
    return t


def t_NEW(t):
    r'new'
    return t

def t_OBJECT(t):
    r'object'
    return t

def t_TYPEOF(t):
    r'typeof'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_THIS(t):
    r'this'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_MATH(t):
    r'MATH'
    return t

def t_JSON(t):
    r'JSON'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_IF(t):
    r'if'
    return t

def t_RETURN(t):
    r'return'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_STRING(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_GREATEREQUAL(t):
    r'>='
    return t

def t_DEQUAL(t):
    r'=='
    return t

def t_LGREATER(t):
    r'<<'
    return t

def t_RGREATER(t):
    r'>>'
    return t

def t_DISTINT(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'(\/\*(\s*|.*?)*\*\/)|(\/\/.*)'
    t.lexer.lineno += t.value.count('\n')

t_ignore = ' \t'

def t_error(t):
    print (("Error Lexico: " + str(t.value[0])))
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

lexer = lex.lex()

def Analizador_lexico():
    a = input("direccion del archivo a ser analizado: ")
    if ( os.path.exists (a)):
        f = open(a)
        data = f.read()
        f.close()
        lexer.input(data)
        test(data, lexer)
    else:
        print ("El archivo no existe")

def Analizador_lexico_consola():
    linea = input("Ingrese l??nea de c??digo: ")
    if ( linea ):
        lexer.input(linea)
        test(linea, lexer)
    else:
        print ("Ingrese una l??nea de c??digo javascript")




