import ply.lex as lex
import re



#Palabras reservadas
reservadas = ['INT','BOOL','STRING','IF','DEFAULT','BREAK','RETURN','FUNCTION','VAR','SWITCH','CASE','PRINT','PROMT']

#Tokens
tokens = reservadas + ['ID','cteent','ctebool','CAD','MAS','MENOS','MUL','MOD','DIV','LLAVA','LLAVC','PARA','PARC',
						'CORA','CORC','DOSPUNTOS','FIN','SIG','OR','AND','NOT','ASIGR','ASIG','OPMAY','OPMEN',
						'OPIG','COMMENT','PR']

#Tabla de palabras reservadas
valorReservadas = {'INT': 1, 'BOOL': 2, 'STRING': 3, 'IF': 4, 'DEFAULT': 5, 'BREAK': 6, 'RETURN': 7, 'FUNCTION': 8, 'VAR': 9, 'SWITCH': 10, 'CASE': 11, 'PRINT': 12, 'PROMPT': 13, 'TRUE': 'true', 'FALSE':'false' }

#Expresiones Regulares

t_MAS = r'\+'
t_MENOS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'

t_ignore = '\n\t '
t_LLAVA = r'\{'
t_LLAVC = r'\}'
t_PARA = r'\('
t_PARC = r'\)'
t_CORA = r'\['
t_CORC = r'\]'

t_FIN = r';'
t_SIG = r','
t_DOSPUNTOS = r':'

t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_ASIGR = r'-='
t_ASIG = r'='
t_OPMAY = r'>'
t_OPMEN = r'<'
t_OPIG = r'=='



#Funciones
# Comment
def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*?(\n|$))'
    pass

def t_ID(c):
	r'[a-zA-Z_]+[a-zA-Z_0-9]*'
	c.value=valorReservadas.get(c.value.upper(), 0)
	if(c.value!=0):
		if c.value=='true':
			c.type='ctebool'
			c.value=1
		elif c.value=='false':
			c.type='ctebool'
			c.value=0
		else:
			c.type='PR'
	else:
		c.value='ptrTS'


	return c

def t_ENT(c):
	r'\d+'
	c.type='cteent'
	c.value=int(c.value)
	return c

def t_CAD(t):
    r'\"([^\\\n]|(\\(.|\n)))*?\"'
    return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

analizador = lex.lex()

nombreFichero = input("Inserta nombre de fichero:")
handle = open(nombreFichero)
cadena =handle.read()
analizador.input(cadena)
ftokens = open("tokens.txt","w+")

while True:
	tok = analizador.token()
	if not tok :
		print("Token erroneo:",tok)
		break
	print('<' + tok.type + ','+ str(tok.value) + '>')
	ftokens.write('<' + tok.type + ','+ str(tok.value) + '>\n')

ftokens.close()
