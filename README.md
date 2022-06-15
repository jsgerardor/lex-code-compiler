# Analizador léxico de javascript escrito en Python usando la librería PLY.lex

### PALABRAS RESERVADAS
Las palabras reservadas y símbolos, se encuentran en el archivo **js_lexer.py**

### Reglas de Expresiones Regulares para tokens
se encuentran en el archivo **js_lexer.py** , se declaran para reconocer los identificadores y tipos de datos al momento de hacer el análisis con ayuda de la librería ply

### Funcionamiento

Para ejecutar la aplicación ejecutar:

```py
python main.py
```
Output:

```bash
MENU COMPILADOR
                1: Línea de código
                2: Analizador Lexico
                3: Salir
opcion: 
```

Seleccionando la primera opción se debe ingresar una línea de código javascript, ejemplo:

```py
console.log("prueba");
```

Output:

```bash
LexToken(CONSOLE,'console',1,0)
LexToken(POINT,'.',1,7)
LexToken(LOG,'log',1,8)
LexToken(LPAREN,'(',1,11)
LexToken(STRING,'"prueba"',1,12)
LexToken(RPAREN,')',1,20)
LexToken(SEMICOLON,';',1,21)
```

Si se selecciona la segunda opción, se debe ingresar la dirección de un archivo <js> . En caso de que el archivo se encuentre en el root de la aplicación **<name>.js** solo se escribe el nombre del archivo, ejemplo:

```bash
direccion del archivo a ser analizado: test.js
```

Output ejemplo (dependiendo del contenido del archivo):

```bash
LexToken(VAR,'var',1,0)
LexToken(ID,'x',1,4)
LexToken(COMMA,',',1,5)
LexToken(ID,'y',1,7)
LexToken(COMMA,',',1,8)
LexToken(ID,'z',1,10)
LexToken(SEMICOLON,';',1,11)
LexToken(ID,'x',2,15)
LexToken(EQUAL,'=',2,17)
LexToken(NUMBER,5,2,19)
LexToken(SEMICOLON,';',2,20)
LexToken(ID,'y',3,26)
LexToken(EQUAL,'=',3,28)
LexToken(NUMBER,6,3,30)
LexToken(SEMICOLON,';',3,31)
LexToken(ID,'z',4,36)
LexToken(EQUAL,'=',4,38)
LexToken(ID,'x',4,40)
LexToken(PLUS,'+',4,42)
LexToken(ID,'y',4,44)
LexToken(SEMICOLON,';',4,45)
LexToken(CONSOLE,'console',6,50)
LexToken(POINT,'.',6,57)
LexToken(LOG,'log',6,58)
LexToken(LPAREN,'(',6,61)
LexToken(STRING,'"hola"',6,62)
LexToken(RPAREN,')',6,68)
LexToken(SEMICOLON,';',6,69)
LexToken(CONSOLE,'console',7,71)
LexToken(POINT,'.',7,78)
LexToken(LOG,'log',7,79)
LexToken(LPAREN,'(',7,82)
LexToken(ID,'z',7,83)
LexToken(RPAREN,')',7,84)
LexToken(SEMICOLON,';',7,85)

presione enter para continuar...

```