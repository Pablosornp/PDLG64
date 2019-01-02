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

#Tabla de simbolos 1.0
tablaDeSimbolos = {}

#Puntero a TS siguiente
count = 1

#Expresiones Regulares

def t_MAS(c):
	r'\+'
	c.value=""
	return c


def t_MENOS(c):
	r'-'
	c.value=""
	return c


def t_MUL(c):
	r'\*'
	c.value=""
	return c


def t_DIV(c):
	r'/'
	c.value=""
	return c

def t_MOD(c):
	r'%'
	c.value=""
	return c

t_ignore = '\n\t '


def t_LLAVA(c):
	r'\{'
	c.value=""
	return c

def t_LLAVC(c):
	r'\}'
	c.value=""
	return c


def t_PARA(c):
	r'\('
	c.value=""
	return c


def t_PARC(c):
	r'\)'
	c.value=""
	return c


def t_CORA(c):
	r'\['
	c.value=""
	return c


def t_CORC(c):
	r'\]'
	c.value=""
	return c

def t_FIN(c):
	r';'
	c.value=""
	return c


def t_SIG(c):
	r','
	c.value=""
	return c

def t_DOSPUNTOS(c):
	r':'
	c.value=""
	return c

def t_OR(c):
	r'\|\|'
	c.value=""
	return c

def t_AND(c):
	r'&&'
	c.value=""
	return c

def t_NOT(c):
	r'!'
	c.value=""
	return c

def t_ASIGR(c):
	r'-='
	c.value=""
	return c


def t_OPIG(c):
	r'=='
	c.value=""
	return c


def t_ASIG(c):
	r'='
	c.value=""
	return c

def t_OPDISTINTO(c):
	r'!='
	c.value=""
	return c


def t_OPMAY(c):
	r'>'
	c.value=""
	return c

def t_OPMEN(c):
	r'<'
	c.value=""
	return c

#Funciones
# Comment
def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*?(\n|$))'
    pass

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
		if tablaDeSimbolos.get(lexema, 0) == 0:
			global count
			tablaDeSimbolos[lexema]=count
			count = count+1
			c.value=tablaDeSimbolos[lexema]
		else:
			c.value=tablaDeSimbolos.get(lexema, 0)



	return c

def t_ENT(c):
	r'\d+'
	c.type='cteent'
	c.value=int(c.value)
	return c

def t_CAD(t):
    r'(\"([^\\\n]|(\\(.|\n)))*?\")|(\'([^\\\n]|(\\(.|\n)))*?\')'
    return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

def getJSlexer():
	return lex.lex()


#Funcion Main
def main():
	analizador = lex.lex()

	nombreFichero = input("Inserta nombre de fichero:")
	handle = open(nombreFichero)
	cadena = handle.read()
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

if __name__ == '__main__':
	main()
