"""
Clase concreta Armario.
"""

from ..categorias.almacenamiento import Almacenamiento

class Armario(Almacenamiento):
    """
    Representa un armario para guardar objetos.
    Hereda de la clase abstracta Almacenamiento.
    """

    def __init__(self, nombre: str, material: str, color: str,
                 precio_base: float, capacidad_volumen: float,
                 tiene_puertas: bool, numero_cajones: int = 0,
                 tipo_puertas: str = "abatibles"):
        super().__init__(nombre, material, color, precio_base,
                         capacidad_volumen, tiene_puertas, numero_cajones)
        self._tipo_puertas = tipo_puertas

    @property
    def tipo_puertas(self) -> str:
        return self._tipo_puertas

    @tipo_puertas.setter
    def tipo_puertas(self, value: str) -> None:
        if not value:
            raise ValueError("El tipo de puertas no puede estar vacío")
        self._tipo_puertas = value

    def calcular_precio(self) -> float:
        """
        Calcula el precio del armario considerando:
        - Precio base
        - Costo adicional por puertas
        - Costo adicional por cajones
        - Factor por capacidad de volumen
        """
        precio = self._precio_base
        if self.tiene_puertas:
            precio += 150
        precio += self.numero_cajones * 40
        precio += (self.capacidad_volumen / 100) * 20
        return precio

    def obtener_descripcion(self) -> str:
        """
        Devuelve una descripción completa del armario.
        """
        return (f"Armario {self.nombre} ({self.material}, {self.color}) - "
                f"{self.obtener_info_almacenamiento()}, "
                f"Tipo de puertas: {self.tipo_puertas}, "
                f"Precio: ${self.calcular_precio():.2f}")
        