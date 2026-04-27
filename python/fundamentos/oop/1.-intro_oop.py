#creacion de la clase usuario - Entidad
class Usuario:
   def __init__(self): #constructor de la clase
    self.nombre = "Nariyoshi"
    self.apellido = "Miyagi"
    self.email = "miyagi@codingdojo.la"
    self.limite_credito = 30000
    self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
isidora = Usuario()

#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Miyagi
print(miyagi.email)
print(miyagi.limite_credito)
print(miyagi.saldo_pagar)

#Nuevos valores asignados a atributos de la instancia
daniel.nombre = "Daniel"
daniel.apellido = "Larusso"
daniel.email = "daniel@gmail.com"
daniel.limite_credito = 100000
daniel.saldo_pagar = 300000

print(daniel.nombre)


#Valores a nueva instancia
isidora.nombre = "Isidora"
isidora.apellido = "Valenzuela"
isidora.email = "isidora@gmail.com"
isidora.limite_credito = 100000
isidora.saldo_pagar = 300000

#Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(isidora.nombre)



