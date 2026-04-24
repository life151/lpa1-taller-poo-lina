from models.categorias.superficies import Superficie

class Mesa(Superficie):
    def __init__(self, nombre, material, color, precio_base, forma="rectangular", tamaño="mediano", plazas=4):
        super().__init__(nombre, material, color, precio_base, forma, tamaño)
        self.plazas = plazas

    def calcular_precio(self):
        return self.precio_base + (self.plazas * 20)

    def obtener_descripcion(self):
        return f"{self.nombre} de {self.material} color {self.color}, {self.forma}, tamaño {self.tamaño}, para {self.plazas} personas"
