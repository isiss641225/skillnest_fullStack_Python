#➡️ Pasar argumentos 
#Para poder personalizar nuestras instancia vamos a pasar algunos argumentos 
# al método __init__ y que de esta manera podamos asignarle a los atributos los valores correspondientes.

class Usuario:
   def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = limite_credito
       self.saldo_pagar = saldo_pagar

#Creación de instancias
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 30000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 30000, 0)
isidora = Usuario("isidora", "valenzuela", "isidora@gmail.com", 550000, 700)

#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


#Tarea 
'''
Crear una clase estudiante y asignarle los siguientes atributos:
rut, nombre, apellido, especialidad, fecha_nac
- Crear 3 instancias para la clase con distintos estudiantes
- Imprimir el nombre y apellido concatenando + especialidad
'''

class Estudiante:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac

martin = Estudiante("22840632-5", "Martin", "Rojas", "Programacion", "04-10-2008")
yulieth = Estudiante("27461998-8", "Yulieth", "Gonzalez", "Programacion", "12-03-2008")
arael = Estudiante("23036981-k", "Arael", "Anabalon", "programacion", "06-06-2009")


