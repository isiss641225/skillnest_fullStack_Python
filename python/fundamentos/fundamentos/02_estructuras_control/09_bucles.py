#1
""" La secuencia de números comienza en 0 por default; el bucle se detiene cuando llega al fin, es decir al argumento enviado a range (pero excluye ese número); 
cada iteración aumenta en secuencia 1 por default. Veamos el resultado del código: """

for i in range(4):
   print(i)


#2
""" La secuencia de números comienza en 2 (el primer argumento); el bucle se detiene cuando llega al fin (segundo argumento, excluyéndolo); 
cada iteración aumenta en secuencia 1 por default. Veamos el resultado del código: """

for i in range(2, 8):
   print(i)


#3
""" La secuencia de números comienza en 2 (el primer argumento); el bucle se detiene cuando llega al fin (segundo argumento, excluyéndolo); cada iteración aumenta en secuencia 3 (tercer argumento).
Veamos el resultado del código: """

for i in range(2, 10, 3):
   print(i)


""" En caso de necesitar un paso para nuestra secuencia, es necesario enviar los tres argumentos al rango.
¡Los rangos también pueden ser decrementales! Para lograr esto, indicaremos que el paso sea un número negativo. """

for i in range(0, 15, 3):
   print(i)
#Imprime: 0, 3, 6, 9, 12

for i in range(10, 1, -3):
   print(i)
#Imprime: 10, 7, 4    