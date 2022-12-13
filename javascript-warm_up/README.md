¿Ques una variable?
Una variable es un contenedor de un valor.

¿Declarar una variable?
antes de usar una variable primero debemos crearla, los cual se llama declarar una variable. "let" es la palabra clave
seguida con el nombre de nuestra variable.
ejemplo:
* let myName;
para probrar si esta variable existe solo se escribe "myName";

¿Como inicializar una variable utilizano let?
se declara el nombre de la variable seguido de un signo igual(=), seguido del valor deseable
ejemplo:
* myName = 'Chris';
* myAge = 37;

¿Podemos declarar e inicializar una variable al mismo tiempo?
si, es la mejor manera de utilizar 
ejemplo:
* let myDog = 'Rover';

¿Como inicializar una variable utilizano var?
cuando se creo javascript var era la unica forma de declara una variable.
puede declarar una variable vardespués de inicializarla
ejemplo:
myName = 'Chris';
var myName;
puedes declarar la misma variable tantas veces como quieras
ejemplo:
var myName = 'Chris';
var myName = 'Bob';

¿Podemos Actualizar una variable?
Si puede inicializado con un valor, puede cambiar (o actualizar) ese valor dándole un valor diferente.
ejemplo:
myName = 'Bob';
myAge = 40;

¿ reglas de nomenclatura de variables?
ejemplo:
age
myAge
init
initialColor
finalOutputValue
audio1
audio2

¿Tipos de variables?
* Números: puede tomar valores enteros y decimales, si comillas
ejemplo:
let myAge = 17;

* Strings: son fragmentos de texto envueltos con comillas simples y dobles, de lo contrario js lo interpreta como variable.
ejemplo:
let dolphinGoodbye = 'So long and thanks for all the fish';

* Booleanos: son valores verdadero/falso (true/false), utilizada para provar una condicion.
ejemplo:
let iAmAlive = true;
let test = 6 < 3;

* arreglos: Una matriz es un único objeto que contiene varios valores encerrados entre corchetes y separados por comas.
ejemplo:
let myNameArray = ['Chris', 'Bob', 'Jim'];
let myNumberArray = [10, 15, 40];

se accede a su valor por la ubicacion dentro de la matriz:
ejemplo:
myNameArray[0]; // should return 'Chris'
myNumberArray[2]; // should return 40

el primer elemento está en el índice 0.

* Objetos: un objeto es una estructura de código que modela un objeto de la vida real. Puede tener un objeto simple que represente una caja y contenga información sobre su ancho, largo y alto, o podría tener un objeto que represente a una persona y contenga datos sobre su nombre, altura, peso, qué idioma habla.
ejemplo:
let dog = { name : 'Spot', breed : 'Dalmatian' };

Para recuperar la información almacenada en el objeto
ejemplo.
dog.name

* Escritura dinámica: JavaScript es un "lenguaje tipado dinámicamente", lo que significa que, a diferencia de otros lenguajes, no necesita especificar qué tipo de datos contendrá una variable (números, cadenas, matrices, etc.).
ejemplo:
let myNumber = '500'; // oops, this is still a string
typeof myNumber;
myNumber = 500; // much better — now this is a number
typeof myNumber;
let myString = 'Hello';

¿ Ques Constantes en JavaScript?
Además de variables, puede declarar constantes. Son como variables, excepto que:

- debes inicializarlos cuando los declaras
- no puede asignarles un nuevo valor después de haberlos inicializado.

ejemplo: 
const count = 1;

¿Cuándo usar const y cuándo usar let?
Úsalo constcuando puedas y úsalo letcuando tengas que hacerlo.
Esto significa que si puede inicializar una variable cuando la declara y no necesita reasignarla más tarde, conviértala en una constante. 



