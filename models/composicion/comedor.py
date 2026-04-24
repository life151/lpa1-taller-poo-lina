from models.concretos.mesa import Mesa
from models.concretos.silla import Silla

class Comedor:
    def __init__(self, mesa: Mesa):
        self.mesa = mesa
        self.sillas = []

    def agregar_silla(self, silla: Silla):
        self.sillas.append(silla)

    def quitar_silla(self, silla: Silla):
        self.sillas.remove(silla)

    def calcular_precio(self):
        return self.mesa.calcular_precio() + sum(s.calcular_precio() for s in self.sillas)

    def obtener_descripcion(self):
        return f"Comedor con {len(self.sillas)} sillas y {self.mesa.obtener_descripcion()}"
