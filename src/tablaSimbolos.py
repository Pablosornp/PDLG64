class TablaSimbolos:
    #Constructor
    def __init__(self):
        self.fichTS = open("Salida\\tablaDeSimbolos.txt","w+")
        self.fichTS.close()
        self.TSG = {'Nombre':'TABLA PRINCIPAL #1:', 'Identificadores':[] }
        self.contTS = 2 #La numero 1 es la TSG
        self.despTSG = 0
        self.TSL = None
        self.despTSL = None

        self.TSactual = self.TSG
        self.despActual = self.despTSG
        self.declaracion = False

    #Metodos
    def crearTSL(self, posTS):
        nombre = self.buscaLexema(posTS)
        (tabla,pos)=self.leePosTS(posTS)
        self.TSL = {'Nombre':'TSL de la funcion '+'\''+nombre+'\' #'+ str(self.contTS)+':', 'Identificadores':[] }
        self.TSactual = self.TSL
        self.despTSL = 0
        tabla['Identificadores'][pos].insertaEtiq('ETI'+nombre+str(self.contTS))

    def destruirTSL(self):
        if self.TSL is not None:
            #self.imprimirTSL()
            self.volcarTSL()
            self.TSL = None
            self.despTSL = None
            self.contTS = self.contTS + 1
            self.TSactual = self.TSG

    def imprimirTSG(self):
        print(self.TSG['Nombre'] +': ')
        for id in self.TSG['Identificadores']:
            id.printID()
        print('\n')

    def imprimirTSL(self):
        print(self.TSL['Nombre'])
        for id in self.TSL['Identificadores']:
            id.printID()
        print('\n')

    def volcarTS(self):
        self.destruirTSL()
        self.fichTS = open("Salida\\tablaDeSimbolos.txt","r")
        volcadoTSL = self.fichTS.read()
        self.fichTS.close()
        self.fichTS = open("Salida\\tablaDeSimbolos.txt","w")
        self.fichTS.write(self.TSG['Nombre'] + '\n')
        for id in self.TSG['Identificadores']:
            self.fichTS.write('* LEXEMA: ' +'\''+id.lexema+'\'\n')
            if id.tipo[0] is 'function':
                self.fichTS.write('\t ATRIBUTOS: '+'\n\t +numParam: '+str(len(id.tipo[1][0]))+'\n\t +TipoRetorno: '+'\''+id.tipo[1][1]+'\'\n\t +EtiqFuncion: '+'\''+id.etiq+'\'\n')
                cont=1
                for arg in id.tipo[1][0]:
                    self.fichTS.write('\t +TipoParam'+str(cont)+ ': '+'\''+arg+'\'\n')
                    cont=cont+1
            elif id.tipo[0] is 'var':
                self.fichTS.write('\t ATRIBUTOS: '+'\n\t +despl: '+str(id.desp)+'\n\t +tipo: '+'\''+id.tipo[1]+'\'\n')
            self.fichTS.write('\t-------------------------------\n')
        self.fichTS.write('\n'+volcadoTSL)
        self.fichTS.close()


    def volcarTSL(self):
        self.fichTS = open("Salida\\tablaDeSimbolos.txt","a+")
        self.fichTS.write(self.TSL['Nombre'] + '\n')
        for id in self.TSL['Identificadores']:
            self.fichTS.write('* LEXEMA: ' +'\''+id.lexema+'\'')
            if(id.tipo[0] is 'arg'):
                    self.fichTS.write(' (parametro de entrada de la funcion)')
            self.fichTS.write('\n\t ATRIBUTOS: '+'\n\t +despl: '+str(id.desp)+'\n\t +tipo: '+'\''+id.tipo[1]+'\'\n')
            self.fichTS.write('\t-------------------------------\n')
        self.fichTS.write('\n')
        self.fichTS.close()




    #Metodo usado por el Lexico al encontrar un token. Devuelve la posicion si inserta o la posicion donde ya esta insertado
    def insertaNuevoID(self, newLexema):
        newID = Identificador(lexema=newLexema)
        posTS = self.buscaID(newLexema)
        pos = self.leePosTS(posTS)
        if(self.declaracion is True):
            if pos is None:
                self.TSactual['Identificadores'].append(newID)
                return self.generaPosTS(self.TSactual,len(self.TSactual['Identificadores'])-1)
            elif pos[0] is not self.TSactual:
                self.TSactual['Identificadores'].append(newID)
                return self.generaPosTS(self.TSactual,len(self.TSactual['Identificadores'])-1)
            else:
                raise Exception('No puede declararse dos variables con mismo nombre en mismo ambito')
        else:
            if pos is None:
                self.TSG['Identificadores'].append(newID)
                posTS = self.generaPosTS(self.TSG,len(self.TSG['Identificadores'])-1)
                self.insertaTipoTS(posTS,('var','int'))
                self.insertaDespTS(posTS,('int'))
                return posTS
            elif pos[0] is self.TSactual:
                return posTS
            elif pos[0] is self.TSG:
                return posTS
            else:
                raise Exception('ERROR: TS inconsistente')

    #pos = buscaID(lexema)
    def buscaID(self,lexema):
        pos=None
        tablaPos=None
        for idx, indentificador in enumerate(self.TSactual['Identificadores']):
            if indentificador.lexema == lexema:
                pos = idx
                tablaPos = self.TSactual
                break
        if (pos is None and self.TSactual is self.TSL):
            for idx, indentificador in enumerate(self.TSG['Identificadores']):
                if indentificador.lexema == lexema:
                    pos = idx
                    tablaPos = self.TSG
                    break
        if(pos is None):
            return None
        else:
            return self.generaPosTS(tablaPos,pos)

    def buscaLexema(self, posTS):
        (tabla,pos)=self.leePosTS(posTS)
        id = tabla['Identificadores'][pos]
        return id.lexema

    def buscaTipo(self,posTS):
        (tabla,pos)=self.leePosTS(posTS)
        id = tabla['Identificadores'][pos]
        return id.tipo


    #Actualiza el tipo de un ID en TS
    def insertaTipoTS(self,posTS,tipo):
        (tabla,pos)=self.leePosTS(posTS)
        tabla['Identificadores'][pos].insertaTipo(tipo)

    def insertaDespTS(self,posTS,tipo):
        (tabla,pos)=self.leePosTS(posTS)
        if tipo is 'int':
            tam=2
        elif tipo is 'bool':
            tam=4
        elif tipo is 'string':
            tam=128
        if tabla is self.TSG:
            tabla['Identificadores'][pos].insertaDesp(self.despTSG)
            self.despTSG=self.despTSG+tam
        elif tabla is self.TSL:
            tabla['Identificadores'][pos].insertaDesp(self.despTSL)
            self.despTSL=self.despTSL+tam


    def cerrarTS(self):
        self.fichTS.close()

    #Devuelve un codigo entero donde el primer digito es la tabla y el resto la posicion
    def generaPosTS(self, tabla, idx):
        if(tabla is self.TSG):
            codTabla = 1
        elif tabla is self.TSL:
            codTabla = 2
        return int(str(codTabla) + str(idx))

    #Dada un pos en TS devuelve la tupla (tabla, poscicion)
    def leePosTS(self,posTS):
        if posTS is not None:
            posTS = str(posTS)
            tablaPos = posTS[0]
            if tablaPos == '1':
                tabla = self.TSG
            elif tablaPos == '2':
                tabla = self.TSL
            pos = posTS[1:]
            return (tabla,int(pos))
        else:
            return None

class Identificador:
    #Constructor
    def __init__(self, *args, **kwargs):
        self.lexema = kwargs.get('lexema','-') #string
        self.tipo = kwargs.get('tipo','-') #tipo
        self.desp = kwargs.get('desp','-') #int
        self.etiq = kwargs.get('etiq','-') #string

    def insertaInfo(self, *args, **kwargs):
        self.tipo = kwargs.get('tipo','-') #tipo
        self.desp = kwargs.get('desp','-') #int
        self.etiq = kwargs.get('etiq','-') #string

    def printID(self):
        tipoRes='('
        if(self.tipo[0] in ['var','arg']):
            tipoRes = self.tipo[0]+ ' '+self.tipo[1]
        elif (self.tipo[0] is 'function'):
            for tipo in self.tipo[1][0]:
                tipoRes=tipoRes + tipo + ','
            tipoRes = tipoRes + ' RET: ' + self.tipo[1][1]
            tipoRes = tipoRes + ')'
        print('( lexema:' + self.lexema + ', tipo:' + tipoRes + ', desp:' + str(self.desp) + ', etiq:' + self.etiq +' )')

    def insertaTipo(self,tipo):
        self.tipo=tipo

    def insertaDesp(self,desp):
        self.desp=desp

    def insertaEtiq(self,etiq):
        self.etiq=etiq


def main():
    ts = TablaSimbolos()
    ts.insertaNuevoID('esCierto')
    ts.insertaNuevoID('contador')
    pos = ts.buscaID('contador')
    ts.insertaTipoTS(pos,'int')
    pos = ts.buscaID('esCierto')
    ts.insertaTipoTS(pos,'bool')
    pos=ts.insertaNuevoID('funA')
    #Creo Tabla para funcion a
    ts.crearTSL(pos)
    ts.declaracion=True
    ts.insertaNuevoID('contador')
    ts.insertaNuevoID('arg1')
    pos = ts.buscaID('contador')
    ts.insertaTipoTS(pos,'string')
    ts.declaracion=False
    pos = ts.insertaNuevoID('pepe')
    ts.destruirTSL()

    pos=ts.insertaNuevoID('funB')
    ts.declaracion=True
    ts.crearTSL(pos)
    pos=ts.insertaNuevoID('contador')
    print(pos)
    pos=ts.insertaNuevoID('arg1')
    ts.insertaTipoTS(pos,'string')
    ts.declaracion=False
    ts.destruirTSL()

    ts.imprimirTSG()



if __name__ == '__main__':
    main()
