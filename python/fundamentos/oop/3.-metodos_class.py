class Usuario:
   def __init__(self, nombre, apellido, email):
       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0

   def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido


#Instancias de la clase
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la")
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la")

miyagi.hacer_compra(2000)
print(f"Primera compra de {miyagi.nombre}: {miyagi.saldo_pagar}")
segundacompra = 300
miyagi.hacer_compra(segundacompra)
print(f"Segunda compra: {miyagi.saldo_pagar}")
#Imprimir cuanto credito le queda a miyagi
print(f"Credito disponible ${miyagi.limite_credito - miyagi.saldo_pagar}")


#Compras de Daniel 2 compras y muestra solo a pagar 
daniel.hacer_compra(45)
print(miyagi.saldo_pagar) #Imprime: 350
print(daniel.saldo_pagar) #Imprime: 45


#Tarea 

'''
1.- Crear un nuevo método que permita aumentar el límite de crédito.
Imprimir el nuevo límite de crédito

2.- Creaer un método que permita cambiar el correo de la instancia.
Mostrar el nuevo correo
'''

miyagi.hacer_compra(2000)
print(f"El nuevo límite de crédito es: {miyagi.limite_credito}")

