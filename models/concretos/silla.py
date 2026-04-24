from models.categorias.asientos import Asiento

class Silla(Asiento):
    def __init__(self, nombre, material, color, precio_base, respaldo=True):
        super().__init__(nombre, material, color, precio_base)
        self.respaldo = respaldo

    def calcular_precio(self):
        return self.precio_base + (50 if self.respaldo else 0)

    def obtener_descripcion(self):
        return f"{self.nombre} de {self.material} color {self.color}, {'con respaldo' if self.respaldo else 'sin respaldo'}"
