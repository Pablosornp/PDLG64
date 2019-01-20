import ply.lex as lex
import re
import tablaSimbolos

#Palabras reservadas
reservadas = ['INT','BOOL','STRING','IF','DEFAULT','BREAK','RETURN','FUNCTION','VAR','SWITCH','CASE','PRINT','PROMT','WHILE']

#Tokens
tokens = reservadas + ['ID','cteent','ctebool','CAD','MAS','MENOS','MUL','MOD','DIV','LLAVA','LLAVC','PARA','PARC',
						'DOSPUNTOS','FIN','SIG','OR','AND','NOT','ASIGR','ASIG','OPMAY','OPMEN',
						'OPIG','OPDISTINTO','COMMENT','PR']

#Tabla de palabras reservadas
valorReservadas = {'INT': 1, 'BOOL': 2, 'STRING': 3, 'IF': 4, 'DEFAULT': 5, 'BREAK': 6, 'RETURN': 7, 'FUNCTION': 8, 'VAR': 9, 'SWITCH': 10, 'CASE': 11, 'PRINT': 12, 'PROMPT': 13, 'WHILE': 14, 'TRUE': 'true', 'FALSE':'false' }

#Tabla de simbolos 2.0
tablaDeSimbolos = None


#Expresiones Regulares

# Comment
def t_COMMENT(t):
	r'(/\*(.|\n)*?\*/)|(//.*?(\n|$))'
	ncr = t.value.count("\n")
	t.lexer.lineno += ncr


def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)

def t_ASIGR(c):
	r'-='
	c.value=None
	return c

def t_OPIG(c):
	r'=='
	c.value=None
	return c

def t_MAS(c):
	r'\+'
	c.value=None
	return c


def t_MENOS(c):
	r'-'
	c.value=None
	return c


def t_MUL(c):
	r'\*'
	c.value=None
	return c


def t_DIV(c):
	r'/'
	c.value=None
	return c

def t_MOD(c):
	r'%'
	c.value=None
	return c

t_ignore = '\t '

def t_LLAVA(c):
	r'\{'
	c.value=None
	return c

def t_LLAVC(c):
	r'\}'
	c.value=None
	return c


def t_PARA(c):
	r'\('
	c.value=None
	return c


def t_PARC(c):
	r'\)'
	c.value=None
	return c

def t_FIN(c):
	r';'
	c.value=None
	return c


def t_SIG(c):
	r','
	c.value=None
	return c

def t_DOSPUNTOS(c):
	r':'
	c.value=None
	return c

def t_OR(c):
	r'\|\|'
	c.value=None
	return c

def t_AND(c):
	r'&&'
	c.value=None
	return c

def t_OPDISTINTO(c):
	r'!='
	c.value=None
	return c

def t_NOT(c):
	r'!'
	c.value=None
	return c

def t_ASIG(c):
	r'='
	c.value=None
	return c

def t_OPMAY(c):
	r'>'
	c.value=None
	return c

def t_OPMEN(c):
	r'<'
	c.value=None
	return c

#Funciones
def t_ID(c):
	r'[a-zA-Z_]+[a-zA-Z_0-9]*'
	lexema = c.value
	c.value=valorReservadas.get(c.value.upper(), 0)
	#Vemos si es cte booleana o PR
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
		c.value=tablaDeSimbolos.insertaNuevoID(lexema)
	return c

def t_ENT(c):
	r'\d+'
	c.type='cteent'
	if int(c.value) > 32767:
		raise Exception('ERROR Lexico en linea '+ str(c.lexer.lineno) +': Entero supera el tamaño máximo')
	c.value=int(c.value)
	return c

def t_CAD(t):
    r'(\"([^\\\n]|(\\(.|\n)))*?\")|(\'([^\\\n]|(\\(.|\n)))*?\')'
    t.value = '\"' +t.value[1:-1] +'\"'
    return t

def t_error(t):
	raise Exception('ERROR Lexico en linea '+ str(t.lexer.lineno)+': token no permitido.')

class AnalizadorLex:
	#Constructor
	def __init__(self, ts=None):
		self.lexer = lex.lex()
		self.ftokens = open("Salida\\tokens.txt","w+")
		global tablaDeSimbolos
		tablaDeSimbolos = ts

	def anyadirToken(self, tok):
		self.ftokens.write('<' + tok.type + ','+ xstr(tok.value) + '>\n')

#Funcion auxiliar que imprime vacio si es None o directamente el
#string argumento s en caso contrario
def xstr(s):
    if s is None:
        return ''
    return str(s)

#Funcion Main
def main():
	analizador = lex.lex()
	global tablaDeSimbolos
	tablaDeSimbolos = tablaSimbolos.TablaSimbolos()

	nombreFichero = input("Inserta nombre de fichero:")
	handle = open(nombreFichero)
	cadena = handle.read()
	analizador.input(cadena)
	ftokens = open("Salida\\tokens.txt","w+")

	tok = analizador.token()
	while tok is not None:
		if not tok :
			print("Token erroneo:",tok)
			break
		print('<' + tok.type + ','+ xstr(tok.value) + ',linea:'+str(analizador.lineno)+'>')
		ftokens.write('<' + tok.type + ','+ xstr(tok.value) + '>\n')
		try:
			tok = analizador.token()
		except Exception as error:
			print(repr(error))
			ftokens.close()
			return
	ftokens.close()

if __name__ == '__main__':
	main()
