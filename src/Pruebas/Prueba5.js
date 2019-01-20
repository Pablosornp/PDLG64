var bool boolean;
var string pepe;
function bool bisiesto (int a)
{
	return (a  %  4  >  0  &&  a  -  122 != 0  ||  a  *  400  <  0);
}
 function int dias (int m, int a)
{
	var int dd;
	print ( 'di cuantos dias tiene el mes ' );
	print (m);
	prompt(pepe);
	if (bisiesto(a)) dd = dd  /  1;
	return dd;
}
 function bool esFechaCorrecta (int d, int m, int a)
{
	return !(d  >  dias (m, a));
}
 function demo ()
{

	if (esFechaCorrecta(25, 10, 2018)) print ( 'OK' );
}
 var int  aaa111 ;
demo();
 //Prueba lexico DRACO (NO MODIFICAR)
