import ply.lex as lex
import re
import lexico

class AnalizadorSinSem:
    #Constructor
    def __init__(self):
        self.lexer = lexico.getJSlexer()
        self.sigToken = None
        self.fichTokens = open("tokens.txt","w+")
        self.fichParse = open("parse.txt","w+")
        self.fichParse.write('Des')

    #Funciones parse
    def P():
        st = tokToString(self.sigToken)
        firstBP = ["break", "id", "if", "print", "prompt", "return", "switch", "var", "while"]
        firstFP = ["function"]
        firstLambda = ["$"]

        if (st in firstBP):
            self.fichParse.write(' 1')
            B()
            P()
        elif (st in firstFP):
            self.fichParse.write(' 2')
            F()
            P()
        elif (st in firstLambda):
            self.fichParse.write(' 3')
        else:
            print("ERROR: sintaxis incorrecta")

    def B():
        st = tokToString(self.sigToken)
        first1 = ["var"]
        first2 = ["if"]
        first3 = ["where"]
        first4 = ["switch"]
        first5 = ["break", "id", "print", "prompt", "return"]

        if(st in first1): #First(var A ;)={ var }
            self.fichParse.write(' 4')
            equiparaToken("var")
            A()
            equiparaToken(";")
        elif (st in first2): #First(if ( E ) S)={ if }
            self.fichParse.write(' 5')
            equiparaToken("if")
            equiparaToken("(")
            E()
            equiparaToken(")")
            S()

        elif (st in first3):#First(while ( E ) { C })={ while }
        elif (st in first4):
        elif (st in first5):
        else:
            print("ERROR: sintaxis incorrecta")






def main():
    an = AnalizadorSinSem()
    nombreFichero = input("Inserta nombre de fichero:")
    handle = open(nombreFichero)
    cadena = handle.read()
    an.lexer.input(cadena)
    an.sigToken = an.lexer.token() #Cargamos el primer token



if __name__ == '__main__':
	main()
