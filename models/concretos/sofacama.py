from models.concretos.sofa import Sofa
from models.concretos.cama import Cama

class SofaCama(Sofa, Cama):
    def __init__(self, nombre, material, color, precio_base, plazas, tamaño,
                 forma="rectangular", material_tapizado="tela"):
        Sofa.__init__(self, nombre, material, color, precio_base,
                      plazas=plazas, tiene_respaldo=True,
                      material_tapizado=material_tapizado,
                      es_reclinable=False, es_modular=False)
        Cama.__init__(self, nombre, material, color, precio_base,
                      forma=forma, tamaño=tamaño,
                      tipo_colchon="estándar", tiene_cabecera=False)

    def calcular_precio(self):
        return Sofa.calcular_precio(self) + Cama.calcular_precio(self)

    def obtener_descripcion(self):
        return (f"{self.nombre} de {self.material} color {self.color}, "
                f"{self.plazas} plazas, funciona como sofá y cama "
                f"de tamaño {self.tamaño} y forma {self.forma}")
