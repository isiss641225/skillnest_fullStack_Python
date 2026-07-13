class SuscripcionStreaming:
    costos_suscripcion = {
        "Gratis": 0,
        "Estándar": 5.99,
        "Premium": 10.99
    }

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion[tipo_suscripcion]
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto):
        self.saldo_pendiente -= monto

        if self.saldo_pendiente < 0:
            self.saldo_pendiente = 0

        print(f"Pago realizado. Saldo pendiente: ${self.saldo_pendiente}")

    def cambiar_suscripcion(self, nuevo_tipo):
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.costo_mensual = self.costos_suscripcion[nuevo_tipo]
            self.saldo_pendiente = self.costo_mensual

            print(f"Suscripción cambiada a {nuevo_tipo}")
        else:
            print("Tipo de suscripción no válido.")

    def ver_contenido_exclusivo(self):
        if self.tipo_suscripcion == "Premium":
            print("Puedes ver todo el contenido exclusivo Premium.")
        elif self.tipo_suscripcion == "Estándar":
            print("Puedes ver contenido exclusivo Estándar.")
        else:
            print("La suscripción Gratis no tiene contenido exclusivo.")

    def mostrar_info_suscripcion(self):
        print("Usuario:", self.usuario)
        print("Tipo de suscripción:", self.tipo_suscripcion)
        print("Costo mensual:", self.costo_mensual)
        print("Saldo pendiente:", self.saldo_pendiente)

# ==============================
# INSTANCIAS 3 USUARIOS
# ==============================

# Crea 3 usuarios con diferentes tipos de suscripción
u1 = SuscripcionStreaming("Ana", "Gratis")
u2 = SuscripcionStreaming("Carlos", "Estándar")
u3 = SuscripcionStreaming("Beatriz", "Premium")

print("\n--- Pruebas Usuario 1 (Intenta ver, mejora, paga) ---")
u1.ver_contenido_exclusivo()
u1.cambiar_suscripcion("Estándar")
u1.realizar_pago(5.99)

print("\n--- Pruebas Usuario 2 (Ve, mejora, paga 2 veces) ---")
u2.ver_contenido_exclusivo()
u2.cambiar_suscripcion("Premium")
u2.realizar_pago(10.00)
u2.realizar_pago(0.99)

print("\n--- Pruebas Usuario 3 (Paga menos, ve contenido) ---")
u3.realizar_pago(5.00)
u3.ver_contenido_exclusivo()

print("\n--- Resumen Final ---")
u1.mostrar_info_suscripcion()
u2.mostrar_info_suscripcion()
u3.mostrar_info_suscripcion()