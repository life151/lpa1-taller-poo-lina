from models.categorias.superficies import Superficie

class Cama(Superficie):
    def __init__(self, nombre, material, color, precio_base, forma, tamaño,
                 tipo_colchon="estándar", tiene_cabecera=True):
        super().__init__(nombre, material, color, precio_base, forma, tamaño)
        self.tipo_colchon = tipo_colchon
        self.tiene_cabecera = tiene_cabecera

    def calcular_precio(self):
        extra = 300 if self.tiene_cabecera else 0
        return self.precio_base + extra

    def obtener_descripcion(self):
        return (f"{self.nombre} de {self.material} color {self.color}, "
                f"forma {self.forma}, tamaño {self.tamaño}, "
                f"colchón {self.tipo_colchon}, "
                f"{'con cabecera' if self.tiene_cabecera else 'sin cabecera'}")
