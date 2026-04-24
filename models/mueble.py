from abc import ABC, abstractmethod

class Mueble(ABC):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float):
        self._nombre = nombre
        self._material = material
        self._color = color
        self._precio_base = precio_base

    @property
    def nombre(self): return self._nombre
    @property
    def material(self): return self._material
    @property
    def color(self): return self._color
    @property
    def precio_base(self): return self._precio_base

    @abstractmethod
    def calcular_precio(self) -> float: ...
    @abstractmethod
    def obtener_descripcion(self) -> str: ...
