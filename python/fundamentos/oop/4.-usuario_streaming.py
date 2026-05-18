""" 🗂️ Define la clase UsuarioStreaming, que debe incluir:

Atributos:
nombre
email
suscripcion (Gratis, Estándar o Premium)
lista_reproduccion (lista de títulos agregados por el usuario).
Métodos:
agregar_a_lista(self, titulo) agrega un contenido a la lista de reproducción.
ver_contenido(self, titulo) simula que el usuario reproduce un contenido.
cambiar_suscripcion(self, nueva_suscripcion) modifica el tipo de suscripción del usuario.
mostrar_info_usuario(self) muestra los datos del usuario y su lista de reproducción.
🧪 Realizar las siguientes pruebas con instancias:

Crea 3 usuarios de la plataforma de streaming.
Haz que el primer usuario agregue dos títulos a su lista y los vea.
Haz que el segundo usuario agregue un título, lo vea y cambie su suscripción.
Haz que el tercer usuario agregue tres títulos, los vea y cambie su suscripción dos veces. """

class UsuarioStreaming:
   def __init__(self, nombre, email, suscripcion="Gratis"):
       self.nombre = nombre
       self.email = email
       self.suscripcion = suscripcion
       self.lista_reproduccion = []


   def agregar_a_lista(self, titulo):
       self.lista_reproduccion.append(titulo)
       """Agrega un contenido a la lista de reproducción del usuario."""
       pass


   def ver_contenido(self, titulo):
        if titulo in self.lista_reproduccion:
            print(f"El usuario {self.nombre} estaba viendo '{titulo}")
        else:
            print(f"Titulo no encontrado {titulo}")
        """Simula que el usuario reproduce un contenido."""


   def cambiar_suscripcion(self, nueva_suscripcion):
       susAntigua = self.suscripocion
       self.suscripcion = nueva_suscripcion
       print(f"Suscripcion = nueva_suscripcion")
       """Cambia el tipo de suscripción del usuario."""
       


   def mostrar_info_usuario(self):
       """Muestra la información del usuario y su lista de reproducción."""
       print(f"Nombre: {self.nombre}")
       print(f"Email: {self.email}")
       print(f"Suscripcion: {self.suscripcion}")
       if len(self.lista_reproduccion) == 0:
           print("La lista de reproducción está vacía")
       else:
           print(f"Lista de reproduccion: \n  {"\n ".join(self.lista_reproduccion)}")
   




#Todos los valores que se deban registrar deben ser con input
#Añadir menú while para llamar a los métodos
#(Menú de selección)