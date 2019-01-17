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
