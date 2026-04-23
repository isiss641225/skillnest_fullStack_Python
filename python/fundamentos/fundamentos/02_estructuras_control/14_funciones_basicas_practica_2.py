import os

#Ejercicio 1

# Calcula experiencia
def multiplica_por_2(num):
    result = []
    for i in range(num + 1):
        result.append(i + 2)
    return result

def ejercicio1():
    result1 = multiplica_por_2(5)
    print(result1)

# Debe retornar: [0, 2, 4, 6, 8, 10]


#Ejercicio 2
# Analiza publicaciones
def suma_y_resta():
    suma = list[0] + list[1]
    resta = list[0] - list[1]
    print(f"suma :  {suma}")
    return resta

def ejercicio2():
    resta = suma_y_resta({120, 115})
    print(f"retorno / resta: {resta}")

# Imprime: 235 y retorna: 5


#Ejercicio 3
# Puntaje ajustado
def sumatoria_menos_longitud(sumatoria):
    total = sum(sumatoria)
    longitud = len(sumatoria)
    resultado = total - longitud
    print(f"total = {total}, longitud = {longitud}")
    return resultado

def ejercicio3():
    retornar = sumatoria_menos_longitud([10, 5, 3, 7])
    print(f"El resultado del retorno es: {retornar}")

# Suma total = 25, longitud = 4, debe retornar: 21



# Ejercicio 4
# Ajusta visualizaciones
def valores_multiplicados_segundo(c):
    valores = []
    print(len(c))
    for i in range(len(c)):
        valores.append(c[i] * (len(c) - 1))
    return valores
# Imprime: 4 y retorna: [300, 9, 150, 60]
# Imprime: 1 y retorna: []


# Ejercicio 5
# Genera precio fijo
def valor_multiplicado_longitud(d, e):
    valor = []
    for i in range(e) :
        valor.append(d*e)
    return valor
# Debe retornar: [10, 10]
# Debe retornar: [35, 35, 35, 35, 35]



def limpiarconsola():
    os.system('cls')


continuar = True
while continuar:
    print("\n---Ejercicios Python---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    opcion = input("\n---Elije una opción: (1-15) (0 para salir)")
    if opcion == "1":
        limpiarconsola()
        print("\nEjecutar ejercicio 1: ")
        multiplica_por_2()
    elif opcion == "2":
        limpiarconsola()
        print("\nEjecutar ejercicio 2: ")
        suma_y_resta()
    elif opcion == "3":
        limpiarconsola()
        print("\nEjecutar ejercicio 3: ")
        sumatoria_menos_longitud()
    elif opcion == "4":
        limpiarconsola()
        print("\nEjecutar ejercicio 4: ")
        valores_multiplicados_segundo()
    elif opcion == "5":
        limpiarconsola()
        print("\nEjecutar ejercicio 5: ")
        valor_multiplicado_longitud()
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válido. Intenta otra vez.")