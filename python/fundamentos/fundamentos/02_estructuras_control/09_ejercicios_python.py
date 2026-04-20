# Guía de Ejercicios: Lógica Fundamental
# I. Interacción y Condicionales (Básico)
"""1. Números Pares Dinámicos
Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$). 
El programa debe imprimir los primeros $n$ números pares positivos.
"""
"""
num = int(input("¿Cuantos números pares desea ver?: "))
for i in range(1, num + 1):
    print(i * 2)
"""


def numerosDinamicos():
    n = int(input("¿Cuantos números desea ver?: "))
    pares = []
    for i in range (1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")
numerosDinamicos()


""" 2. Verificador de Edad y Acceso
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
"""


def verificarEdad():
    anio = int(input("Ingrese su año de nacimiento: "))
    edad = 2026 - anio

    if edad >= 18:
      print("Eres mayor de edad.")
    else:
        faltan = 18 - edad
        print(f"Eres menor de edad. \nTe faltan {faltan} años para ser mayor de edad.")
verificarEdad()


""" 3. Calculadora de Descuentos
Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, aplica un 15% de descuento. 
Muestra el subtotal, el descuento aplicado y el total final.
"""


def descuento():
    precioProduc = int(input("Ingrese el precio del producto: "))
    cantidadProduc  = int(input("Ingrese la cantidad de productos que desea comprar: "))
    total = precioProduc * cantidadProduc

    if total > 100:
        descuento = total * 15 / 100
        print(f"A tu producto se le aplicara un descuento del 15%. Precio inicial ${total}, precio final ${descuento}")
    else:
        print(F"El total es de ${total}")
descuento()


"""4. Clasificador de Números
Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, 
Negativo-Par, Negativo-Impar o Cero."""


def clasificadorNum():
    n = int(input("Ingrese un número: "))
    if n > 0 and n % 2 == 0:
        print(f"El n° ingresado {n} es Positivo-Par")
    elif n > 0 and n % 2 != 0:
        print(f"El n° ingresado {n} es Positivo-Impar")
    elif n < 0 and n % 2 == 0:
        print(f"El n° ingresado {n} es Negativo-Par")
    elif n < 0 and n % 2 != 0:
        print(f"El n° ingresado {n} es Negativo-Impar")
clasificadorNum()


""" 5. Tabla de Multiplicar Personalizada
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, 
pero solo muestra los resultados que sean múltiplos de 3. """

def tablaMultiplicar():
    num = int(input("Ingresar números a trabajar: "))
    for i in range (1, 13):
        resultado = num * 1
        if resultado & 3 == 0:
            print(f"Del (num) números son divisible por 3: {resultado} ")



""" 6. Sumatoria con Centinela
Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario ingrese un número negativo. 
Al final, muestra la suma total (sin incluir el negativo). """

def sumaCentinela():
    suma_total = 0
    


""" 7. Contador de Vocales
Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la 
cadena y contar cuántas vocales tiene en total. """

def contadorVocales():
    texto = input("Ingresa una palabra o frase: ").lower()
    vocales = 0
    for i in range(len(texto)):
        #Repetir la condición con cada vocal
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            vocales += 1
            #Mismo de arriba pero con las vocales con tilde
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
            vocales += 1
    print(f"La cadena '{texto}' tiene {vocales} en total")

""" 8. Validación de Contraseña
Define una contraseña en una variable. Pide al usuario que la intente adivinar. 
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso. """



""" III. Manejo de Arreglos / Listas (Avanzado)
9. Registro de Nombres
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. 
Guárdalos en el arreglo y, al final, imprímelos en orden inverso al que fueron ingresados. """



""" 10. Promedio de Notas
Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. 
Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja. """

def promedioNotas():
    cantidad = int(input("¿Cuántas notas deseas ingresar?"))
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")

""" 11. Filtro de Arreglos
Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga 
solo los números que sean mayores a 50. Muestra ambos arreglos. """

#def filtroArreglos():
    

""" 12. Buscador de Elementos
Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el 
programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está. """

def buscadorElemento():
    ciudades = ["Nairobi", "Tokio", "Santiago", "Lima", "Caracas", "Río", "Berlín", "Seúl", "Buenos Aires",]
    ciudad = input("Ingresar ciudad (con mayúscula al principio): ").capitalize()
    esta = ciudades.index(ciudad)
    if esta < int(ciudades) 

""" IV. Retos de Lógica Combinada
13. Simulación de Inventario
Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar 3 productos 
con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor]. """
def 
""" 14. Generador de Lista de Compras
Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso termina cuando 
el usuario escribe "terminar". Al final, muestra la lista ordenada alfabéticamente. """

""" 15. Análisis de Temperaturas
Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes). """

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
    print("---Ejercicio 11---")
    print("---Ejercicio 12---")
    print("---Ejercicio 13---")
    print("---Ejercicio 14---")
    print("---Ejercicio 15---")
    opcion = input("\n---Elije una opción: (1-15) (0 para salir)")
    if opcion == "1":
        print("\nEjecutar ejercicio 1: ")
        numerosDinamicos()
    elif opcion == "2":
        print("\nEjecutar ejercicio 2: ")
        verificarEdad()
    elif opcion == "3":
        print("\nEjecutar ejercicio 3: ")
        descuento()
    elif opcion == "4":
        print("\nEjecutar ejercicio 4: ")
        clasificadorNum()
    elif opcion == "5":
        print("\nEjecutar ejercicio 5: ")
        tablaMultiplicar()
    elif opcion == "6":
        print("\nEjecutar ejercicio 6: ")
        sumaCentinela()
    elif opcion == "7":
        print("\nEjecutar ejercicio 7: ")
        contadorVocales()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")