"""
Clase concreta Escritorio.
"""

from ..categorias.superficies import Superficie

class Escritorio(Superficie):
    """
    Representa un escritorio para trabajar o estudiar.
    Hereda de la clase abstracta Superficie.
    """

    def __init__(self, nombre: str, material: str, color: str,
                 precio_base: float, forma: str, tamaño: str,
                 tiene_cajones: bool = True, numero_cajones: int = 2,
                 tiene_estante: bool = False):
        super().__init__(nombre, material, color, precio_base, forma, tamaño)
        self._tiene_cajones = tiene_cajones
        self._numero_cajones = numero_cajones
        self._tiene_estante = tiene_estante

    # --- Getters y Setters ---
    @property
    def tiene_cajones(self) -> bool:
        return self._tiene_cajones

    @tiene_cajones.setter
    def tiene_cajones(self, value: bool) -> None:
        self._tiene_cajones = bool(value)

    @property
    def numero_cajones(self) -> int:
        return self._numero_cajones

    @numero_cajones.setter
    def numero_cajones(self, value: int) -> None:
        if value < 0:
            raise ValueError("El número de cajones no puede ser negativo")
        self._numero_cajones = value

    @property
    def tiene_estante(self) -> bool:
        return self._tiene_estante

    @tiene_estante.setter
    def tiene_estante(self, value: bool) -> None:
        self._tiene_estante = bool(value)

    # --- Métodos concretos ---
    def calcular_precio(self) -> float:
        """
        Calcula el precio del escritorio considerando:
        - Precio base
        - Costo adicional por cajones
        - Costo adicional por estante
        """
        precio = self._precio_base
        if self.tiene_cajones:
            precio += self.numero_cajones * 40
        if self.tiene_estante:
            precio += 100
        return precio

    def obtener_descripcion(self) -> str:
        """
        Devuelve una descripción completa del escritorio.
        """
        return (f"Escritorio {self.nombre} ({self.material}, {self.color}) - "
                f"Forma: {self.forma}, Tamaño: {self.tamaño}, "
                f"Cajones: {self.numero_cajones if self.tiene_cajones else 'No'}, "
                f"Estante: {'Sí' if self.tiene_estante else 'No'}, "
                f"Precio: ${self.calcular_precio():.2f}")
        