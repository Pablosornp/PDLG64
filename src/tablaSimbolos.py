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
        self.declaracion = False

    #Metodos
    def crearTSL(self, nombre):
        self.TSL = {'Nombre':'TSL'+nombre,'Numero':self.contTS, 'Identificadores':[] }
        self.despTSL = 0

    def destruirTSL(self):
        imprimirTSL()
        self.TSL = {}
        self.despTSL = 0
        self.contTS = self.contTS + 1

    def imprimirTSL(self):
        None

    #Metodo usado por el Lexico al encontrar un token
    def insertaNuevoID(self, newLexema):
        pos = self.buscaID(newLexema) #PTE
        if (pos is None):
            newID = Identificador(lexema=newLexema)
            self.TSactual['Identificadores'].append(newID)
            return self.buscaID(newLexema)
        else:
            raise Exception('ERROR: No puede declararse una variable dos veces en el mismo ambito')

    #Metodo laxo usado por el Lexico al encontrar un token (no chequea id repe)
    def insertaNuevoIDLAXO(self, newLexema):
        pos = self.buscaID(newLexema) #PTE
        newID = Identificador(lexema=newLexema)
        self.TSactual['Identificadores'].append(newID)
        return self.buscaID(newLexema)


    #pos = buscaID(lexema)
    def buscaID(self,lexema):
        pos=None
        for idx, indentificador in enumerate(self.TSactual['Identificadores']):
            if indentificador.lexema == lexema:
                pos = idx
                break
        return pos


    #Actualiza el tipo de un ID en TS
    def insertaTipoTS(self,pos,tipo):
        self.TSactual['Identificadores'][pos].insertaTipo(tipo)


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

    def printID(self):
        print('( lexema:' + self.lexema + ', tipo:' + self.tipo + ' )')

    def insertaTipo(self,tipo):
        self.tipo=tipo

    def insertaDesp(self,desp):
        self.desp=desp


def main():
    ts = TablaSimbolos()
    ts.insertaNuevoID('contador')
    ts.insertaNuevoID('esCierto')
    pos = ts.buscaID('contador')
    ts.insertaTipoTS(pos,'int')
    pos = ts.buscaID('esCierto')
    ts.insertaTipoTS(pos,'bool')
    for id in ts.TSG['Identificadores']:
        id.printID()

if __name__ == '__main__':
    main()
