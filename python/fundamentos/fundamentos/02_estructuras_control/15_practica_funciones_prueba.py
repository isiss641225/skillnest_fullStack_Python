import os
"""Requisitos obligatorios
Su trabajo debe cumplir con lo siguiente:
Uso de funciones con parámetros
Uso de menú con ciclo while
Uso de input() para solicitar datos
Uso de listas (arreglos)
Uso de diccionarios
Uso de ciclos for
Uso de estructuras condicionales (if, elif, else)
Código ordenado, comentado y correctamente indentado
Opción de salida del programa (0. Salir)"""


# Ejercicios a desarrollar

# Su programa deberá considerar las siguientes funciones:

"""1.- Crear una función que reciba una lista de números enteros y muestre 
 cuál es el número mayor y cuál es el menor."""
def listaNum(listado):
    menor = min(listado)
    mayor = max(listado)
    print(f"El número mayor es {mayor} \nEl número menor es {menor}")

def ejercicio1():
    limit = int(input("Ingresa un limite de valores: "))
    listadoNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit} : "))
        listadoNum.append(num)
        i += 1
    listaNum(listadoNum)

""" 2.- Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene."""
def esVocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales

def contarVocales(texto):
    contador = 0
    for letra in texto:
        if esVocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales")

def ejercicio2():
    texto = input("Ingresa el texto: ")
    contarVocales(texto)



""" 3.- Crear una función que reciba una lista de nombres y 
 muestre únicamente aquellos que tengan más de 5 letras."""
def filtrar(lista):
    resultado = []
    for nombre in lista:
        if len(nombre) > 5:
            resultado.append(nombre)
    return

def ejercicio3():
    nombres = []
    cantidad = int(input("¿Cuántos nombres quieres ingresar?: "))

    for i in range(cantidad):
        nombre = input("Ingrese un nombre: ")
        print(f"{nombre} agregado con éxito a la lista")
        nombres.append(nombre)

    listaNombres = filtrar(nombres)
    print(f"Los nombres con más de 5 letras son \n  )")

""" 4.- Crear una función que reciba una lista de notas (números decimales), 
 calcule el promedio e indique si el estudiante aprueba (promedio mayor o igual a 4.0)."""
def listaNotas(notas):
    lista = 0
    for i in range(len(notas)):
        lista += notas[i]
        if notas[i] >= 4.0 and notas[i] <= 7.0:
            print(f"El estudiante {i+1} pasa con un {notas[i]}")
        elif notas[i] >= 1 and notas[i] <= 3.9:
            print(f"El estudiante {i+1} no pasa con un {notas[i]}")
        else:
            print("Error")
    return lista / (len(lista) + 1)

def ejercicio4():
    largo = int(input("Cuántas notas va a ingresar: "))
    nota = [] #lista
    for i in range(largo): #almacena notas
        inp = float(input(f"Ingrese nota {i + 1}")) #
    if inp !="":
        nota.append(inp)
    print(listaNotas(nota))
""" 5.- Crear una función que reciba una lista de precios de productos y 
 aplique un descuento del 10%, mostrando el valor original y el nuevo valor."""


""" 6.- Crear una función que reciba un número entero y determine si es par o impar."""
def numeroEntero(numero):
    if numero % 2 == 0:
        print(f"El número ingresado {numero} es par")
    else:
        print(f"El número ingresado {numero} es impar")

def ejercicio6():
    num = int(input("Ingrese un número entero: "))
    numeroEntero(num)
    


""" 7.- Crear una función que reciba una lista de edades y muestre cuántas 
 personas son mayores de edad (18 años o más)."""

def edades(lista):
    num = 0
    for i in range(len(lista)):
        if lista[i] >= 18:
            num >= 1
    return num 

def personas():
    edad = []
    inp = int(input("¿Cuántas personas vas a ingresar hoy?: "))



""" 8.- Crear una función que reciba una lista de palabras y permita buscar 
 cuántas veces aparece una palabra específica ingresada por el usuario."""
def vecesqueaparece(palabras):
    buscar = input("Ingrese la palabra que desea buscar: ")
    vecesqueaparece = 0
    for i in range(len(palabras)):
        if buscar == palabras[i]:
            vecesqueaparece += 1
    print(f"La palabra {buscar} aparece {vecesqueaparece} en la lista. ")

def registropalabras():
    cantidad = int(input("Ingrese la cantidad de palabras: "))
    listapalabras = []
    for i in range(cantidad):
        palabra = input(f"")




""" 9.- Crear una función que reciba una lista de números y genere una nueva 
 lista que contenga únicamente los números positivos."""

""" 10.- Crear una función que reciba una lista de productos 
 (utilizando diccionarios con nombre y stock) y muestre cuáles tienen un stock menor a 5 unidades."""

def limpiar_consola():
    os.system('cls')

continuar = True
while continuar: 
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    print("---Ejercicio 7---")
    print("---Ejercicio 8---")
    print("---Ejercicio 9---")
    print("---Ejercicio 10---")
    opcion = input("\n---Elije una opción: (1-5) (0 para salir)")
    if opcion == "1":
        limpiar_consola()
        print("\nEjecutar ejercicio 1: ")
        ejercicio1()
    elif opcion == "2":
        limpiar_consola()
        print("\nEjecutar ejercicio 2: ")
        
    elif opcion == "3":
        limpiar_consola()
        print("\nEjecutar ejercicio 3: ")
        
    elif opcion == "4":
        limpiar_consola()
        print("\nEjecutar ejercicio 4: ")
        
    elif opcion == "5":
        limpiar_consola()
        print("\nEjecutar ejercicio 5: ")
        
    elif opcion == "6":
        limpiar_consola()
        print("\nEjecutar ejercicio 6: ")
        numeroEntero()
    elif opcion == "7":
        limpiar_consola()
        print("\nEjecutar ejercicio 7: ")
        
    elif opcion == "8":
        limpiar_consola()
        print("\nEjecutar ejercicio 8: ")
        
    elif opcion == "9":
        limpiar_consola()
        print("\nEjecutar ejercicio 9: ")
        
    elif opcion == "10":
        limpiar_consola()
        print("\nEjecutar ejercicio 10: ")
        
    elif opcion == "0":
        limpiar_consola()
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.") 