import ply.lex as lex
import re
import lexico

class AnalizadorSinSem:
    #Constructor
    def __init__(self):
        self.lexico = lexico.AnalizadorLex()
        self.sigToken = None
        self.fichParse = open("parse.txt","w+")
        self.fichParse.write('Des')

    #Funciones parse
    def P(self):
        first1 = [("PR",6), ("ID",None), ("PR",4), ("PR",12), ("PR",13), ("PR",7), ("PR",10), ("PR",9), ("PR",14)]
        first2 = [("PR",8)]
        first3 = [("$",None)]

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 1')
            self.B()
            self.P()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 2')
            self.F()
            self.P()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 3')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def B(self):
        first1 = [("PR",9)] #First(var T id ;)={ var }
        first2 = [("PR",4)]  #First(if ( E ) S)={ if }
        first3 = [("PR",14)] #First(while ( E ) { C })={ while }
        first4 = [("PR",10)] #First(switch ( E ) { D })={ switch }
        first5 = [("PR",6), ("ID",None), ("PR",12), ("PR",13), ("PR",7)] #First(S)={ break id print prompt return }

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 4')
            self.equiparaToken(("PR",9))
            self.T()
            self.equiparaToken(("ID",None))
            self.equiparaToken(("FIN",None))
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 5')
            self.equiparaToken(("PR",4))
            self.equiparaToken(("PARA",None))
            self.E()
            self.equiparaToken(("PARC",None))
            self.S()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 6')
            self.equiparaToken(("PR",14))
            self.equiparaToken(("PARA",None))
            self.E()
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("LLAVA",None))
            self.C()
            self.equiparaToken(("LLAVC",None))
        elif (self.tokenInFirst(first4)):
            self.fichParse.write(' 7')
            self.equiparaToken(("PR",10))
            self.equiparaToken(("PARA",None))
            self.E()
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("LLAVA",None))
            self.D()
            self.equiparaToken(("LLAVC",None))
        elif (self.tokenInFirst(first5)):
            self.fichParse.write(' 8')
            self.S()
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def T(self):
        first1 = [("PR",1)] #First(int)={ int }
        first2 = [("PR",2)] #First(bool)={ bool }
        first3 = [("PR",3)] #First(string)={ string }

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 9')
            self.equiparaToken(("PR",1))
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 10')
            self.equiparaToken(("PR",2))
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 11')
            self.equiparaToken(("PR",3))
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    def S(self):
        first1 = [("ID",None)] #First(id S')={ id }
        first2 = [("PR",7)] # First(return X ;)={ return }
        first3 = [("PR",12)] #First(print ( E ) ;)={ print }
        first4 = [("PR",13)] #First(prompt ( id ) ;)={ prompt }
        first5 = [("PR",6)] #First( break ;)={ break }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 12')
            self.equiparaToken(("ID",None))
            self.S_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 13')
            self.equiparaToken(("PR",7))
            self.X()
            self.equiparaToken(("FIN",None))
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 14')
            self.equiparaToken(("PR",12))
            self.equiparaToken(("PARA",None))
            self.E()
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("FIN",None))
        elif (self.tokenInFirst(first4)):
            self.fichParse.write(' 15')
            self.equiparaToken(("PR",13))
            self.equiparaToken(("PARA",None))
            self.equiparaToken(("ID",None))
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("FIN",None))
        elif (self.tokenInFirst(first5)):
            self.fichParse.write(' 16')
            self.equiparaToken(("PR",6))
            self.equiparaToken(("FIN",None))
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def S_(self):
        first1 = [("ASIG",None)] #First(= E ;)={ = }
        first2 = [("ASIGR",None)] #First(-= E ;)={ -= }
        first3 = [("PARA",None)] #First(( L ) ;)={ ( }

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 17')
            self.equiparaToken(("ASIG",None))
            self.E();
            self.equiparaToken(("FIN",None))
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 18')
            self.equiparaToken(("ASIGR",None))
            self.E();
            self.equiparaToken(("FIN",None))
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 19')
            self.equiparaToken(("PARA",None))
            self.L()
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("FIN",None))
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def F(self):
        first1 = [("PR",8)] #First(function H id ( A ) { C })={ function }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 20')
            self.equiparaToken(("PR",8))
            self.H()
            self.equiparaToken(("ID",None))
            self.equiparaToken(("PARA",None))
            self.A()
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("LLAVA",None))
            self.C()
            self.equiparaToken(("LLAVC",None))
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def H(self):
        first1 = [("PR",1), ("PR",2), ("PR",3)] #First(T)={ int bool string }
        first2 = [("ID",None)] #Follow(H)={ id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 21')
            self.T()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 22')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def L(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(E Q)={ ! ( cte_bool CAD cte_ent id }
        first2 = [("PARC",None)] #Follow(L)={ ) }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 23')
            self.E()
            self.Q()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 24')
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    def Q(self):
        first1 = [("SIG",None)] #First(, E Q)={ , }
        first2 = [("PARC",None)] #Follow(Q)={ ) }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 25')
            self.equiparaToken(("SIG",None))
            self.E()
            self.Q()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 26')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def A(self):
        first1 = [("PR",1), ("PR",2), ("PR",3)] #First(T id K)={ int bool string }
        first2 = [("PARC",None),("FIN",None)] #Follow(A)={ ) ; }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 27')
            self.T()
            self.equiparaToken(("ID",None))
            self.K()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 28')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def K(self):
        first1 = [("SIG",None)] #First(, T id K)={ , }
        first2 = [("PARC",None)] #Follow(K)={ ) }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 29')
            self.equiparaToken(("SIG",None))
            self.T()
            self.equiparaToken(("ID",None))
            self.K()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 30')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def X(self):
        first1 = [("NOT",None), ("PARA",None), ("ctebool",None), ("CAD",None), ("cteent",None), ("ID",None)] #First(E)={ ! ( cte_bool CAD cte_ent id }
        first2 = [("FIN",None)] #Follow(X)={ ; }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 31')
            self.E()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 32')
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    def C(self):
        first1 = [("PR",6),("ID",None),("PR",4),("PR",12),("PR",13),("PR",7),("PR",10),("PR",9),("PR",14)] #First(B C)={ break id if print prompt return switch var while }
        first2 = [("PR",11),("LLAVC",None),("PR",5)] #Follow(C)={ case } default }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 33')
            self.B()
            self.C()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 34')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def E(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None), ("cteent",None), ("ID",None)]#First(R E')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 35')
            self.R()
            self.E_()
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def E_(self):
        first1 = [("OR",None)] #First(|| R E')={ || }
        first2 = [("PARC",None),("SIG",None),("FIN",None)] #Follow(E')={ ) , ; }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 36')
            self.equiparaToken(("OR",None))
            self.R()
            self.E_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 37')
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    def R(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(U R')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 38')
            self.U()
            self.R_()
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def R_(self):
        first1 = [("AND",None)] #First(&& U R')
        first2 = [("PARC",None), ("SIG",None), ("FIN",None), ("OR",None)] #Follow(R')={ ) , ; || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 39')
            self.equiparaToken(("AND",None))
            self.U()
            self.R_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 40')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def U(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None), ("cteent",None), ("ID",None)] #First(V U')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 41')
            self.V()
            self.U_()
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def U_(self):
        first1 = [("OPIG",None)] #First(== V U')={ == }
        first2 = [("OPDISTINTO",None)] #First(!= V U')={ != }
        first3 = [("AND",None),("PARC",None),("SIG",None),("FIN",None),("OR",None)] #Follow(U')={ && ) , ; || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 42')
            self.equiparaToken(("OPIG",None))
            self.V()
            self.U_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 43')
            self.equiparaToken(("OPDISTINTO",None))
            self.V()
            self.U_()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 44')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def V(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(W V')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 45')
            self.W()
            self.V_()
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def V_(self):
        first1 = [("OPMAY",None)] #First(> W V')={ > }
        first2 = [("OPMEN",None)] #First(< W V')={ < }
        first3 = [("OPDISTINTO",None), ("AND",None), ("PARC",None), ("SIG",None), ("FIN",None), ("OPIG",None), ("OR",None)] #Follow(V')={ != && ) , ; == || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 46')
            self.equiparaToken(("OPMAY",None))
            self.W()
            self.V_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 47')
            self.equiparaToken(("OPMEN",None))
            self.W()
            self.V_()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 48')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def W(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(Z W')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 49')
            self.Z()
            self.W_()
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    def W_(self):
        first1 = [("MAS",None)] #First(+ Z W')={ + }
        first2 = [("MENOS",None)] #First(- Z W')={ - }
        first3 = [("OPDISTINTO",None), ("AND",None), ("PARC",None), ("SIG",None), ("FIN",None),("OPMEN",None),("OPMAY",None),("OPIG",None),("OR",None)] #Follow(W')={ != && ) , ; < == > || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 50')
            self.equiparaToken(("MAS",None))
            self.Z()
            self.W_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 51')
            self.equiparaToken(("MENOS",None))
            self.Z()
            self.W_()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 52')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def Z(self):
        first1 = [("NOT",None), ("PARA",None), ("ctebool",None), ("CAD",None), ("cteent",None), ("ID",None)] #First(G Z')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 53')
            self.G()
            self.Z_()
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def Z_(self):
        first1 = [("MUL",None)] #First(* G Z')={ * }
        first2 = [("DIV",None)] #First(/ G Z')={ / }
        first3 = [("MOD",None)] #First(% G Z')={ % }
        first4 = [("OPDISTINTO",None), ("AND",None), ("PARC",None), ("MAS",None), ("SIG",None), ("MENOS",None), ("FIN",None),("OPMEN",None), ("OPIG",None), ("OPMAY",None), ("OR",None)] #Follow(Z')={ != && ) + , - ; < == > || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 54')
            self.equiparaToken(("MUL",None))
            self.G()
            self.Z_()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 55')
            self.equiparaToken(("DIV",None))
            self.G()
            self.Z_()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 56')
            self.equiparaToken(("MOD",None))
            self.G()
            self.Z_()
        elif (self.tokenInFirst(first4)):
            self.fichParse.write(' 57')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def G(self):
        first1 = [("NOT",None)] #First(! G)={ ! }
        first2 = [("ID",None)] #First(id G')={ id }
        first3 = [("PARA",None)] #First(( E ))={ ( }
        first4 = [("cteent",None)] #First(cte_ent)={ cte_ent }
        first5 = [("CAD",None)] #First(CAD)={ CAD }
        first6 = [("ctebool",None)] #First(cte_bool)={ cte_bool }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 58')
            self.equiparaToken(("NOT",None))
            self.G()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 59')
            self.equiparaToken(("ID",None))
            self.G_()
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 60')
            self.equiparaToken(("PARA",None))
            self.E()
            self.equiparaToken(("PARC",None))
        elif (self.tokenInFirst(first4)):
            self.fichParse.write(' 61')
            self.equiparaToken(("cteent",None))
        elif (self.tokenInFirst(first5)):
            self.fichParse.write(' 62')
            self.equiparaToken(("CAD",None))
        elif (self.tokenInFirst(first6)):
            self.fichParse.write(' 63')
            self.equiparaToken(("ctebool",None))
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def G_(self):
        first1 = [("PARA",None)] # First(( L ))={ ( }
        first2 = [("OPDISTINTO",None), ("MOD",None), ("AND",None), ("PARC",None), ("MUL",None), ("MAS",None), ("SIG",None), ("MENOS",None), ("DIV",None), ("FIN",None), ("OPMEN",None), ("OPIG",None), ("OPMAY",None), ("OR",None)] #Follow(G')={ != % && ) * + , - / ; < == > || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 64')
            self.equiparaToken(("PARA",None))
            self.L()
            self.equiparaToken(("PARC",None))
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 65')
        else:
            raise Exception("ERROR: sintaxis incorrecta")

    def D(self):
        first1 = [("PR",11)] #First(case cte_ent : C D)={ case }
        first2 = [("PR",5)] #First(default : C)={ default }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 66')
            self.equiparaToken(("PR",11))
            self.equiparaToken(("cteent",None))
            self.equiparaToken(("DOSPUNTOS",None))
            self.C()
            self.D()
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 67')
            self.equiparaToken(("PR",5))
            self.equiparaToken(("DOSPUNTOS",None))
            self.C()
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    #Funcion auxiliar equiparaToken:
    #Tiene como parametro de entrada una tupla (type,value) del token
    def equiparaToken(self,tok):
        #if (tok[0] == self.sigToken[0] and tok[1] == self.sigToken[1]) or tok[0] == self.sigToken[0] == "ID" or tok[0] == self.sigToken[0] == "CAD" :
        if (tok[0] == self.sigToken[0] and tok[1] == self.sigToken[1]) or (tok[0] == self.sigToken[0] and self.sigToken[0] in ["CAD", "ID", "ctebool", "cteent"]) :
            st1 = self.lexico.lexer.token()
            if (st1 is not None): #Cargamos el primer token
                self.sigToken = (st1.type, st1.value)
                self.lexico.anyadirToken(st1)
                print(self.sigToken[0], self.sigToken[1])
            else:
                self.sigToken = ("$", None)
                print("$")
        else:
            raise Exception("ERROR: sintaxis incorrecta")


    #Funcion auxiliar tokenInFirst:
    def tokenInFirst(self,first):
        if self.sigToken in first:
            return True
        elif self.sigToken[0] in ["CAD", "ID", "ctebool", "cteent"]:
            return (self.sigToken[0], None) in first
        else:
            return False

    def closeFiles(self):
        self.fichParse.close()




def main():
    an = AnalizadorSinSem()
    nombreFichero = input("Inserta nombre de fichero:")
    handle = open(nombreFichero)
    cadena = handle.read()
    an.lexico.lexer.input(cadena)
    st1 = an.lexico.lexer.token()
    if (st1 is not None): #Cargamos el primer token
        an.sigToken = (st1.type, st1.value)
        print(an.sigToken[0], an.sigToken[1])
        an.lexico.anyadirToken(st1)
        #{TSG = newTS(); despG=0}
        an.P()
        #destruirTS()
    else:
        print("Fichero fuente vacío \n")
    an.closeFiles()


if __name__ == '__main__':
	main()
