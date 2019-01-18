import lexico
import tablaSimbolos

class AnalizadorSinSem:
    #Constructor
    def __init__(self):
        self.ts = tablaSimbolos.TablaSimbolos()
        self.lx = lexico.AnalizadorLex(self.ts)
        self.sigToken = None
        self.fichParse = open("Salida\\parse.txt","w+")
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
            raise Exception("ERROR sintactico: sintaxis incorrecta")

    def B(self):
        first1 = [("PR",9)] #First(var T id ;)={ var }
        first2 = [("PR",4)]  #First(if ( E ) S)={ if }
        first3 = [("PR",14)] #First(while ( E ) { C })={ while }
        first4 = [("PR",10)] #First(switch ( E ) { D })={ switch }
        first5 = [("PR",6), ("ID",None), ("PR",12), ("PR",13), ("PR",7)] #First(S)={ break id print prompt return }

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 4')
            self.equiparaToken(("PR",9))
            self.ts.declaracion = True
            tTipo = self.T()
            pos = self.sigToken[1]
            self.equiparaToken(("ID",None))
            self.ts.insertaTipoTS(pos,('var',tTipo))
            self.ts.insertaDespTS(pos,tTipo)
            self.ts.declaracion = False
            self.equiparaToken(("FIN",None))
            BtipoRet='tipo_vacio'


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
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        #return BtipoRet

    def T(self):
        first1 = [("PR",1)] #First(int)={ int }
        first2 = [("PR",2)] #First(bool)={ bool }
        first3 = [("PR",3)] #First(string)={ string }

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 9')
            self.equiparaToken(("PR",1))
            Ttipo='int'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 10')
            self.equiparaToken(("PR",2))
            Ttipo='bool'
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 11')
            self.equiparaToken(("PR",3))
            Ttipo='string'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return Ttipo

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
            raise Exception("ERROR sintactico: sintaxis incorrecta")

    def S_(self):
        first1 = [("ASIG",None)] #First(= E ;)={ = }
        first2 = [("ASIGR",None)] #First(-= E ;)={ -= }
        first3 = [("PARA",None)] #First(( L ) ;)={ ( }

        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 17')
            self.equiparaToken(("ASIG",None))
            eTipo=self.E();
            self.equiparaToken(("FIN",None))
            s_Tipo=eTipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 18')
            self.equiparaToken(("ASIGR",None))
            eTipo=self.E();
            self.equiparaToken(("FIN",None))
            if eTipo is'int':
                s_Tipo=eTipo
            else:
                s_Tipo='tipo_error'
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 19')
            self.equiparaToken(("PARA",None))
            lTipo=self.L()
            self.equiparaToken(("PARC",None))
            self.equiparaToken(("FIN",None))
            s_Tipo=lTipo
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return s_Tipo

    def F(self):
        first1 = [("PR",8)] #First(function H id ( A ) { C })={ function }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 20')
            self.equiparaToken(("PR",8))
            self.ts.declaracion = True
            hTipo=self.H()
            pos = self.sigToken[1]
            self.equiparaToken(("ID",None))
            self.ts.crearTSL(pos)
            self.equiparaToken(("PARA",None))
            aTipo=self.A()
            self.equiparaToken(("PARC",None))
            self.ts.insertaTipoTS(pos,('function',(aTipo,hTipo)))
            self.ts.declaracion = False
            self.equiparaToken(("LLAVA",None))
            self.C()
            self.equiparaToken(("LLAVC",None))
            self.ts.destruirTSL()
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")

    def H(self):
        first1 = [("PR",1), ("PR",2), ("PR",3)] #First(T)={ int bool string }
        first2 = [("ID",None)] #Follow(H)={ id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 21')
            tTipo=self.T()
            hTipo = tTipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 22')
            hTipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return hTipo

    def L(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(E Q)={ ! ( cte_bool CAD cte_ent id }
        first2 = [("PARC",None)] #Follow(L)={ ) }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 23')
            eTipo=self.E()
            qTipo=self.Q()
            if qTipo is 'tipo_vacio':
                lTipo=[eTipo]
            else:
                qTipo.insert(0,eTipo)
                lTipo=qTipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 24')
            lTipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return lTipo


    def Q(self):
        first1 = [("SIG",None)] #First(, E Q)={ , }
        first2 = [("PARC",None)] #Follow(Q)={ ) }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 25')
            self.equiparaToken(("SIG",None))
            eTipo=self.E()
            q1Tipo=self.Q()
            if qTipo is 'tipo_vacio':
                qTipo = [eTipo]
            else:
                q1Tipo.insert(0,eTipo)
                qTipo = q1Tipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 26')
            qTipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return qTipo

    def A(self):
        first1 = [("PR",1), ("PR",2), ("PR",3)] #First(T id K)={ int bool string }
        first2 = [("PARC",None),("FIN",None)] #Follow(A)={ ) ; }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 27')
            tTipo=self.T()
            pos = self.sigToken[1]
            self.equiparaToken(("ID",None))
            self.ts.insertaTipoTS(pos, ('var',tTipo))
            self.ts.insertaDespTS(pos, tTipo)
            kTipo=self.K()
            if(kTipo is 'tipo_vacio'):
                aTipo = [tTipo]
            else:
                kTipo.insert(0,tTipo)
                aTipo = kTipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 28')
            aTipo=['tipo_vacio']
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return aTipo

    def K(self):
        first1 = [("SIG",None)] #First(, T id K)={ , }
        first2 = [("PARC",None)] #Follow(K)={ ) }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 29')
            self.equiparaToken(("SIG",None))
            tTipo=self.T()
            pos = self.sigToken[1]
            self.equiparaToken(("ID",None))
            self.ts.insertaTipoTS(pos,tTipo)
            self.ts.insertaDespTS(pos, tTipo)
            k1Tipo = self.K()
            if(k1Tipo is 'tipo_vacio'):
                kTipo = [tTipo]
            else:
                k1Tipo.insert(0,tTipo)
                kTipo = k1Tipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 30')
            kTipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return kTipo

    def X(self):
        first1 = [("NOT",None), ("PARA",None), ("ctebool",None), ("CAD",None), ("cteent",None), ("ID",None)] #First(E)={ ! ( cte_bool CAD cte_ent id }
        first2 = [("FIN",None)] #Follow(X)={ ; }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 31')
            eTipo=self.E()
            xTipo=eTipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 32')
            xTipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return xTipo


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
            raise Exception("ERROR sintactico: sintaxis incorrecta")

    def E(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None), ("cteent",None), ("ID",None)]#First(R E')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 35')
            rTipo=self.R()
            e_Tipo=self.E_()
            if e_Tipo == 'tipo_vacio':
                eTipo=rTipo
            elif e_Tipo == 'bool' and rTipo=='bool':
                eTipo='bool'
            else:
                raise Exception("ERROR semantico: expresion incorrecta")
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return eTipo

    def E_(self):
        first1 = [("OR",None)] #First(|| R E')={ || }
        first2 = [("PARC",None),("SIG",None),("FIN",None)] #Follow(E')={ ) , ; }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 36')
            self.equiparaToken(("OR",None))
            rTipo=self.R()
            e1_Tipo=self.E_()
            if rTipo == 'bool' and e1_Tipo in ['bool', 'tipo_vacio']:
                e_Tipo='bool'
            else:
                e_Tipo = 'tipo_error'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 37')
            e_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return e_Tipo


    def R(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(U R')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 38')
            uTipo=self.U()
            r_Tipo=self.R_()
            if r_Tipo=='tipo_vacio':
                rTipo=uTipo
            elif r_Tipo =='bool' and uTipo == 'bool':
                rTipo = 'bool'
            else:
                 rTipo = 'tipo_error'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return rTipo

    def R_(self):
        first1 = [("AND",None)] #First(&& U R')
        first2 = [("PARC",None), ("SIG",None), ("FIN",None), ("OR",None)] #Follow(R')={ ) , ; || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 39')
            self.equiparaToken(("AND",None))
            uTipo=self.U()
            r1_Tipo=self.R_()
            if uTipo=='bool' and r1_Tipo in ['bool', 'tipo_vacio']:
                r_Tipo='bool'
            else:
                r_Tipo = 'tipo_error'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 40')
            r_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return r_Tipo

    def U(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None), ("cteent",None), ("ID",None)] #First(V U')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 41')
            vTipo=self.V()
            u_Tipo=self.U_()
            if u_Tipo == 'tipo_vacio':
                uTipo = vTipo
            elif u_Tipo == 'bool' and vTipo=='int':
                uTipo = 'bool'
            else:
                uTipo = 'tipo_error'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return uTipo

    def U_(self):
        first1 = [("OPIG",None)] #First(== V U')={ == }
        first2 = [("OPDISTINTO",None)] #First(!= V U')={ != }
        first3 = [("AND",None),("PARC",None),("SIG",None),("FIN",None),("OR",None)] #Follow(U')={ && ) , ; || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 42')
            self.equiparaToken(("OPIG",None))
            vTipo=self.V()
            u1_Tipo=self.U_()
            if(vTipo == 'int' and u1_Tipo == 'tipo_vacio'):
                u_Tipo='bool'
            else:
                u_Tipo='tipo_error'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 43')
            self.equiparaToken(("OPDISTINTO",None))
            vTipo=self.V()
            u1_Tipo=self.U_()
            if(vTipo == 'int' and u1_Tipo == 'tipo_vacio'):
                u_Tipo='bool'
            else:
                u_Tipo='tipo_error'
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 44')
            u_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return u_Tipo

    def V(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(W V')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 45')
            wTipo=self.W()
            v_Tipo=self.V_()
            if v_Tipo == 'tipo_vacio':
                vTipo=wTipo
            elif v_Tipo =='bool' and wTipo=='int':
                vTipo='bool'
            else:
                vTipo='tipo_error'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return vTipo

    def V_(self):
        first1 = [("OPMAY",None)] #First(> W V')={ > }
        first2 = [("OPMEN",None)] #First(< W V')={ < }
        first3 = [("OPDISTINTO",None), ("AND",None), ("PARC",None), ("SIG",None), ("FIN",None), ("OPIG",None), ("OR",None)] #Follow(V')={ != && ) , ; == || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 46')
            self.equiparaToken(("OPMAY",None))
            wTipo=self.W()
            v1_Tipoself.V_()
            if(wTipo == 'int' and v1_Tipo == 'tipo_vacio'):
                v_Tipo='bool'
            else:
                v_Tipo='tipo_error'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 47')
            self.equiparaToken(("OPMEN",None))
            wTipo=self.W()
            v1_Tipoself.V_()
            if(wTipo == 'int' and v1_Tipo == 'tipo_vacio'):
                v_Tipo='bool'
            else:
                v_Tipo='tipo_error'
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 48')
            v_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return v_Tipo

    def W(self):
        first1 = [("NOT",None),("PARA",None),("ctebool",None),("CAD",None),("cteent",None),("ID",None)] #First(Z W')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 49')
            zTipo=self.Z()
            w_Tipo=self.W_()
            if w_Tipo == 'tipo_vacio':
                wTipo = zTipo
            elif zTipo == 'int' and w_Tipo == 'int':
                wTipo='int'
            else:
                wTipo = 'tipo_error'

        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return wTipo


    def W_(self):
        first1 = [("MAS",None)] #First(+ Z W')={ + }
        first2 = [("MENOS",None)] #First(- Z W')={ - }
        first3 = [("OPDISTINTO",None), ("AND",None), ("PARC",None), ("SIG",None), ("FIN",None),("OPMEN",None),("OPMAY",None),("OPIG",None),("OR",None)] #Follow(W')={ != && ) , ; < == > || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 50')
            self.equiparaToken(("MAS",None))
            zTipo = self.Z()
            w1_Tipo = self.W_()
            if(zTipo=='int' and w1_Tipo in ['int','tipo_vacio']):
                w_Tipo = 'int'
            else:
                w_Tipo = 'tipo_error'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 51')
            self.equiparaToken(("MENOS",None))
            zTipo = self.Z()
            w1_Tipo = self.W_()
            if(zTipo=='int' and w1_Tipo in ['int','tipo_vacio']):
                w_Tipo = 'int'
            else:
                w_Tipo = 'tipo_error'
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 52')
            w_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return w_Tipo

    def Z(self):
        first1 = [("NOT",None), ("PARA",None), ("ctebool",None), ("CAD",None), ("cteent",None), ("ID",None)] #First(G Z')={ ! ( cte_bool CAD cte_ent id }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 53')
            gTipo = self.G()
            z_Tipo = self.Z_()
            if z_Tipo == 'tipo_vacio':
                zTipo=gTipo
            elif z_Tipo == 'int' and gTipo=='int':
                zTipo='int'
            else:
                zTipo='tipo_error'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return zTipo

    def Z_(self):
        first1 = [("MUL",None)] #First(* G Z')={ * }
        first2 = [("DIV",None)] #First(/ G Z')={ / }
        first3 = [("MOD",None)] #First(% G Z')={ % }
        first4 = [("OPDISTINTO",None), ("AND",None), ("PARC",None), ("MAS",None), ("SIG",None), ("MENOS",None), ("FIN",None),("OPMEN",None), ("OPIG",None), ("OPMAY",None), ("OR",None)] #Follow(Z')={ != && ) + , - ; < == > || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 54')
            self.equiparaToken(("MUL",None))
            gTipo=self.G()
            z1_Tipo=self.Z_()
            if(gTipo is'int' and z1_Tipo in ['int','tipo_vacio' ] ):
                z_Tipo='int'
            else:
                z_Tipo='tipo_error'
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 55')
            self.equiparaToken(("DIV",None))
            gTipo=self.G()
            z1_Tipo=self.Z_()
            if(gTipo is 'int' and z1_Tipo in ['int','tipo_vacio' ] ):
                z_Tipo='int'
            else:
                z_Tipo='tipo_error'
        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 56')
            self.equiparaToken(("MOD",None))
            gTipo=self.G()
            z1_Tipo=self.Z_()
            if(gTipo is 'int' and z1_Tipo in ['int','tipo_vacio' ] ):
                z_Tipo='int'
            else:
                z_Tipo='tipo_error'
        elif (self.tokenInFirst(first4)):
            self.fichParse.write(' 57')
            z_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return z_Tipo

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
            g1_Tipo=self.G()
            if g1_Tipo is 'bool':
                gTipo = 'bool'
            else:
                gTipo = 'tipo_error'

        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 59')
            pos = self.sigToken[1]
            tipoID = self.ts.buscaTipo(pos)
            self.equiparaToken(("ID",None))
            g_Tipo=self.G_()
            if g_Tipo is 'tipo_vacio':
                gTipo=tipoID
            elif tipoID[0] is 'function' and tipoID[1][0] is g_Tipo:
                gTipo=tipoID[1][1]
            else:
                gTipo='tipo_error'

        elif (self.tokenInFirst(first3)):
            self.fichParse.write(' 60')
            self.equiparaToken(("PARA",None))
            eTipo=self.E()
            self.equiparaToken(("PARC",None))
            gTipo=eTipo
        elif (self.tokenInFirst(first4)):
            self.fichParse.write(' 61')
            self.equiparaToken(("cteent",None))
            gTipo='int'
        elif (self.tokenInFirst(first5)):
            self.fichParse.write(' 62')
            self.equiparaToken(("CAD",None))
            gTipo='string'
        elif (self.tokenInFirst(first6)):
            self.fichParse.write(' 63')
            self.equiparaToken(("ctebool",None))
            gTipo='bool'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return gTipo

    def G_(self):
        first1 = [("PARA",None)] # First(( L ))={ ( }
        first2 = [("OPDISTINTO",None), ("MOD",None), ("AND",None), ("PARC",None), ("MUL",None), ("MAS",None), ("SIG",None), ("MENOS",None), ("DIV",None), ("FIN",None), ("OPMEN",None), ("OPIG",None), ("OPMAY",None), ("OR",None)] #Follow(G')={ != % && ) * + , - / ; < == > || }
        if (self.tokenInFirst(first1)):
            self.fichParse.write(' 64')
            self.equiparaToken(("PARA",None))
            lTipo=self.L()
            self.equiparaToken(("PARC",None))
            g_Tipo=lTipo
        elif (self.tokenInFirst(first2)):
            self.fichParse.write(' 65')
            g_Tipo='tipo_vacio'
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")
        return g_Tipo

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
            raise Exception("ERROR sintactico: sintaxis incorrecta")


    #Funcion auxiliar equiparaToken:
    #Tiene como parametro de entrada una tupla (type,value) del token
    def equiparaToken(self,tok):
        if (tok[0] == self.sigToken[0] and tok[1] == self.sigToken[1]) or (tok[0] == self.sigToken[0] and self.sigToken[0] in ["CAD", "ID", "ctebool", "cteent"]) :
            st1 = self.lx.lexer.token()
            if (st1 is not None): #Cargamos el primer token
                self.sigToken = (st1.type, st1.value)
                self.lx.anyadirToken(st1)
                #print(self.sigToken[0], self.sigToken[1]) #Para ver los tokens
            else:
                self.sigToken = ("$", None)
                print("$")
        else:
            raise Exception("ERROR sintactico: sintaxis incorrecta")


    #Funcion auxiliar tokenInFirst:
    def tokenInFirst(self,first):
        if self.sigToken in first:
            return True
        elif self.sigToken[0] in ["CAD", "ID", "ctebool", "cteent"]:
            return (self.sigToken[0], None) in first
        else:
            return False

    #Cierra todos los ficheros de salida
    def closeFiles(self):
        self.fichParse.close()
        self.lx.ftokens.close()
        self.ts.fichTS.close()

def main():
    an = AnalizadorSinSem()
    nombreFichero = input("Inserta nombre de fichero:")
    handle = open(nombreFichero)
    cadena = handle.read()
    an.lx.lexer.input(cadena)
    st1 = an.lx.lexer.token() #Cargamos el primer token
    if (st1 is not None):
        an.sigToken = (st1.type, st1.value)
        #print(an.sigToken[0], an.sigToken[1]) #Para ver el primer token
        an.lx.anyadirToken(st1)
        an.P()
        an.ts.imprimirTSG() #Temporal: se sustituira por el fichero de TS
        #Posteriormente hay que hacer append del fichero con la TSG y el fichero
        #con las TSL

    else:
        print("Fichero fuente vacío \n")
    an.closeFiles()


if __name__ == '__main__':
	main()
