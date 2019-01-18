var int contador;
var bool esCierto;
a=2
var string cadena;
function int divide (int num1, int num2)
{
 a = b //variable no existente que se declarará como global y entera
 var int b //declaracion de variable local
 b=a //b coge el valor de la variable global
 var bool a //declaracion de variable local de mismo nombre de la global que hace que esta ultima no sea ya accesible
 a = b  //asignacion a variable local
 return a;
}

def insertaNuevoID(self, newLexema):
      posTS = self.buscaID(newLexema)
      pos = self.leePosTS(posTS)
      newID = Identificador(lexema=newLexema)
      if(self.declaracion is True):
          if pos is None or pos[1] is not self.TSactual:
              self.TSactual['Identificadores'].append(newID)
              return self.generaPosTS(self.TSactual,len(self.TSactual['Identificadores'])-1)
          else:
              raise Exception('Error Semantico: No pueden declararse dos ids de mismo nombre en el mismo ambito')
      elif pos is None:
          self.TSG['Identificadores'].append(newID)
          return self.generaPosTS(self.TSG,len(self.TSG['Identificadores'])-1)
