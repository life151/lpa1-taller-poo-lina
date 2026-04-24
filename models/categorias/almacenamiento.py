from abc import ABC
from models.mueble import Mueble

class Almacenamiento(Mueble, ABC):
    def __init__(self, nombre: str, material: str, color: str,
                 precio_base: float, capacidad_volumen: float,
                 tiene_puertas: bool = False, numero_cajones: int = 0):
        super().__init__(nombre, material, color, precio_base)
        self.capacidad_volumen = capacidad_volumen
        self.tiene_puertas = tiene_puertas
        self.numero_cajones = numero_cajones

    @property
    def capacidad(self):
        return self.capacidad_volumen

    def obtener_info_almacenamiento(self) -> str:
        return (f"Capacidad: {self.capacidad_volumen} litros, "
                f"Puertas: {'Sí' if self.tiene_puertas else 'No'}, "
                f"Cajones: {self.numero_cajones}")
