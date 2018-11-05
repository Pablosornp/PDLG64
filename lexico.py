import ply.lex as lex
import re



#Palabras reservadas
reservadas = ['INT','BOOL','STRING','IF','DEFAULT','BREAK','RETURN','FUNCTION','VAR','SWITCH','CASE','PRINT','PROMT']

#Tokens
tokens = reservadas + ['ID','ENT','CAD','MAS','MENOS','MUL','DIV','LLAVA','LLAVC','PARA','PARC',
						'CORA','CORC','FIN','SIG','OR','AND','NOT','ASIG_R','ASIG','OP_MAY','OP_MEN',
						'OP_IG','OP_MAY_IG','OP_MEN_IG']



#Expresiones Regulares

t_MAS = r'\+'
t_MENOS = r'-'
t_MUL = r'\*'
#t_Div = r'/'

t_ignore = '\t '
t_LLAVA = r'{'
t_LLAVC = r'}'
t_PARA = r'\('
t_PARC = r'\)'
t_CORA = r'\['
t_CORC = r'\]'

t_FIN = r';'
t_SIG = r','

#t_OR = r'\'
t_AND = r'\&\&'
t_NOT = r'\!'
#t_ASIG_R = r'\-\='
t_ASIG = r'='
t_OP_MAY = r'>'
t_OP_MEN = r'<'
#t_OP_MAY_IG = r'\>\='
#t_OP_MEN_IG = r'\<\='
#t_IG = r'\=\='



#Funciones

def t_ID(c):
	r'[a-zA-Z_]+[a-zA-Z_0-9]*'
	return c

def t_ENT(c):
	r'\d+'
	c.value=int(c.value)
	return c

def t_INT(c):
	r'int'
	return c

def t_BOOL(c):
	r'bool'
	return c

def t_STRING(c):
	r'string'
	return c

def t_IF(c):
	r'if'
	return c

def t_DEFAULT(c):
	r'dfault'
	return c

def t_BREAK(c):
	r'break'
	return c

def t_RETURN(c):
	r'return'
	return c

def t_FUNCTION(c):
	r'function'
	return c

def t_VAR(c):
	r'var'
	return c

def t_SWITCH(c):
	r'switch'
	return c

def t_CASE(c):
	r'case'
	return c

def t_PRINT(c):
	r'print'
	return c

def t_PROMPT(c):
	r'promt'
	return c

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

analizador = lex.lex()

nombreFichero = input("Inserta nombre de fichero:")
handle = open(nombreFichero)
cadena =handle.read()
analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok :
		print("Token erroneo:",tok)
		break
	print(tok)
