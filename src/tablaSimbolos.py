class TablaSimbolos:
    #Constructor
    def __init__(self):
        self.fichTS = open("Salida\\tablaDeSimbolos.txt","w+")
        self.contTS = 2 #La numero 1 será la TSG
        self.TSG = {'Nombre':'TABLA PRINCIPAL','Numero':1, 'Identificadores':[] }
        self.despTSG = 0
        self.TSL = None
        self.despTSL = None
        self.etiquetas = []

        self.TSactual = self.TSG
        self.despActual = self.despTSG
        self.declaracion = False

    #Metodos
    def crearTSL(self, nombre):
        self.TSL = {'Nombre':'TSL: '+nombre,'Numero':self.contTS, 'Identificadores':[] }
        self.despTSL = 0

    def destruirTSL(self):
        imprimirTSL()
        self.TSL = {}
        self.despTSL = 0
        self.contTS = self.contTS + 1

    def imprimirTSG(self):
        print(self.TSG['Nombre'])
        for id in self.TSG['Identificadores']:
            id.printID()
        print('\n')

    def imprimirTSL(self):
        print(self.TSL['Nombre'])
        for id in self.TSL['Identificadores']:
            id.printID()
        print('\n')

    #Metodo usado por el Lexico al encontrar un token
    def insertaNuevoID(self, newLexema):
        (pos,tablaPos) = self.buscaID(newLexema) #PTE
        if(self.declaracion is True):
            if pos is None:
                self.TSactual['Identificadores'].append(newID)
                return self.buscaID(newLexema)
        elif pos is None:
            self.TSG['Identificadores'].append(newID)
            return self.buscaID(newLexema)

    #Metodo laxo usado por el Lexico al encontrar un token (no chequea id repe)
    def insertaNuevoIDLAXO(self, newLexema):
        pos = self.buscaID(newLexema) #PTE
        newID = Identificador(lexema=newLexema)
        self.TSactual['Identificadores'].append(newID)
        return self.buscaID(newLexema)


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
        return (pos,tablaPos)



    #Actualiza el tipo de un ID en TS
    def insertaTipoTS(self,pos,tipo):
        self.TSactual['Identificadores'][pos].insertaTipo(tipo)

    #Modifica el flag de declaración
    def modoDeclaracion(self,flag):
        self.declaracion = flag


    def cerrarTS(self):
        self.fichTS.close()

class Identificador:
    #Constructor
    def __init__(self, *args, **kwargs):
        self.lexema = kwargs.get('lexema','-') #string
        self.tipo = kwargs.get('tipo','-') #tipo
        self.desp = kwargs.get('desp','-') #int
        self.params = kwargs.get('params','-') #Lista de tipos
        self.tipoRet = kwargs.get('tipoRet','-') #tipo
        self.etiq = kwargs.get('etiq','-') #string

    def insertaInfo(self, *args, **kwargs):
        self.tipo = kwargs.get('tipo','-') #tipo
        self.desp = kwargs.get('desp','-') #int
        self.params = kwargs.get('params','-') #Lista de tipos
        self.tipoRet = kwargs.get('tipoRet','-') #tipo
        self.etiq = kwargs.get('etiq','-') #string

    def printID(self):
        print('( lexema:' + self.lexema + ', tipo:' + self.tipo + ' )')

    def insertaTipo(self,tipo):
        self.tipo=tipo


    def insertaDesp(self,desp):
        self.desp = desp
        self.despActual = self.despActual + desp



def main():
    ts = TablaSimbolos()
    ts.insertaNuevoID('contador')
    ts.insertaNuevoID('esCierto')
    pos = ts.buscaID('contador')
    ts.insertaTipoTS(pos,'int')
    pos = ts.buscaID('esCierto')
    ts.insertaTipoTS(pos,'bool')
    ts.crearTSL('Funcion a')
    ts.imprimirTSG()
    ts.imprimirTSL()
    ts.destruirTSL()

if __name__ == '__main__':
    main()
