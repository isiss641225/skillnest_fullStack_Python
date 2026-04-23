#Funciones en python
def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado


resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25


#Parametros y argumentos
def buenos_dias(nombre):
   print("Buenos días " + nombre)
#Llamada a la función y asignación de valor a párametro
buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")



def buenos_dias(nombre):
   return "Buenos días "+nombre

#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python

#Ejercicio de retorno de valor
#Crear una función que reciba una frase + un parametro
#Devolver el valor de la frase completa e imprimir

def construirFrase(frase, palabra):
   return f"{frase} {palabra}"

frase = input("Ingrese una frase")
palabra = input("Ingrese una palabra")
resultadoFrase = construirFrase(frase, palabra)
print(resultadoFrase)