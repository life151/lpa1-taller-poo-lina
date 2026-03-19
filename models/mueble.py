"""
Clase base abstracta Mueble
Este es el punto de partida de nuestra jerarquía de clases.
"""

# TODO: Importar ABC y abstractmethod del módulo abc
# Estos son necesarios para crear clases y métodos abstractos
from abc import ABC, abstractmethod


class Mueble(ABC):
    """
    Clase abstracta base para todos los muebles.
    
    Esta clase define la estructura común que deben tener todos los muebles
    de nuestra tienda, pero no puede ser instanciada directamente.
    
    Conceptos OOP aplicados:
    - Abstracción: Define una interfaz común sin implementación específica
    - Encapsulación: Usa atributos privados con getters/setters
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float):
        """
        Constructor de la clase Mueble.
        """
        # TODO: Inicializar los atributos privados usando underscore
        self._nombre = nombre
        self._material = material
        self._color = color
        if precio_base < 0:
            raise ValueError("El precio base no puede ser negativo")
        self._precio_base = precio_base
    
    # TODO: Implementar las propiedades (getters) para cada atributo
    @property
    def nombre(self) -> str:
        """Getter para el nombre del mueble."""
        return self._nombre
    
    @property
    def material(self) -> str:
        return self._material
    
    @property
    def color(self) -> str:
        return self._color
    
    @property
    def precio_base(self) -> float:
        return self._precio_base
    
    # TODO: Implementar los setters para cada atributo donde sea necesario
    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value.strip()
    
    @material.setter
    def material(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El material no puede estar vacío")
        self._material = value.strip()
    
    @color.setter
    def color(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El color no puede estar vacío")
        self._color = value.strip()
    
    @precio_base.setter
    def precio_base(self, value: float) -> None:
        if value < 0:
            raise ValueError("El precio base no puede ser negativo")
        self._precio_base = value
    
    # TODO: Implementar método abstracto calcular_precio()
    @abstractmethod
    def calcular_precio(self) -> float:
        """Calcula el precio final del mueble."""
        pass
    
    # TODO: Implementar método abstracto obtener_descripcion()
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Obtiene una descripción detallada del mueble."""
        pass
    
    def __str__(self) -> str:
        """
        Representación en cadena del mueble.
        Este método concreto puede ser usado por todas las clases hijas.
        """
        # TODO: Implementar usando las propiedades
        return f"{self.nombre} de {self.material} en color {self.color}"
    
    def __repr__(self) -> str:
        """
        Representación técnica del mueble para debugging.
        """
        # TODO: Implementar una representación técnica
        return (
            f"Mueble(nombre='{self.nombre}', material='{self.material}', "
            f"color='{self.color}', precio_base={self.precio_base})"
        )
        