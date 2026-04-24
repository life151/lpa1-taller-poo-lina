"""
Clase concreta Cajonera.
"""

from ..categorias.almacenamiento import Almacenamiento

class Cajonera(Almacenamiento):
    """
    Representa una cajonera para guardar objetos.
    Hereda de la clase abstracta Almacenamiento.
    """

    def __init__(self, nombre: str, material: str, color: str,
                 precio_base: float, capacidad_volumen: float,
                 numero_cajones: int):
        # Una cajonera siempre tiene cajones y no necesariamente puertas
        super().__init__(nombre, material, color, precio_base,
                         capacidad_volumen, tiene_puertas=False,
                         numero_cajones=numero_cajones)

    def calcular_precio(self) -> float:
        """
        Calcula el precio de la cajonera considerando:
        - Precio base
        - Costo adicional por cada cajón
        - Factor por capacidad de volumen
        """
        precio = self._precio_base
        precio += self.numero_cajones * 30
        precio += (self.capacidad_volumen / 50) * 10
        return precio

    def obtener_descripcion(self) -> str:
        """
        Devuelve una descripción completa de la cajonera.
        """
        return (f"Cajonera {self.nombre} ({self.material}, {self.color}) - "
                f"{self.obtener_info_almacenamiento()}, "
                f"Precio: ${self.calcular_precio():.2f}")
        