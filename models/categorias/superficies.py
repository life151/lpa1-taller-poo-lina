from abc import ABC
from models.mueble import Mueble

class Superficie(Mueble, ABC):   # Nombre con mayúscula
    def __init__(self, nombre: str, material: str, color: str,
                 precio_base: float, forma: str = "rectangular",
                 tamaño: str = "mediano"):
        super().__init__(nombre, material, color, precio_base)
        self.forma = forma
        self.tamaño = tamaño

    def obtener_info_superficie(self) -> str:
        return f"Forma: {self.forma}, Tamaño: {self.tamaño}"
