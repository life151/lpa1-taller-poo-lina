"""
Clase concreta Sillón.
"""

from ..categorias.asientos import Asiento

class Sillon(Asiento):
    """
    Representa un sillón individual para sentarse cómodamente.
    Hereda de la clase abstracta Asiento.
    """

    def __init__(self, nombre: str, material: str, color: str,
                 precio_base: float, capacidad_personas: int = 1,
                 tiene_respaldo: bool = True, material_tapizado: str = "tela",
                 tiene_reposabrazos: bool = True, es_reclinable: bool = False):
        super().__init__(nombre, material, color, precio_base,
                         capacidad_personas, tiene_respaldo, material_tapizado)
        self._tiene_reposabrazos = tiene_reposabrazos
        self._es_reclinable = es_reclinable

    # --- Getters y Setters ---
    @property
    def tiene_reposabrazos(self) -> bool:
        return self._tiene_reposabrazos

    @tiene_reposabrazos.setter
    def tiene_reposabrazos(self, value: bool) -> None:
        self._tiene_reposabrazos = bool(value)

    @property
    def es_reclinable(self) -> bool:
        return self._es_reclinable

    @es_reclinable.setter
    def es_reclinable(self, value: bool) -> None:
        self._es_reclinable = bool(value)

    # --- Métodos concretos ---
    def calcular_precio(self) -> float:
        """
        Calcula el precio del sillón considerando:
        - Precio base
        - Factor de comodidad
        - Reposabrazos opcionales
        - Función reclinable
        """
        precio = self._precio_base * self.calcular_factor_comodidad()
        if self.tiene_reposabrazos:
            precio += 80
        if self.es_reclinable:
            precio += 200
        return precio

    def obtener_descripcion(self) -> str:
        """
        Devuelve una descripción completa del sillón.
        """
        return (f"Sillón {self.nombre} ({self.material}, {self.color}) - "
                f"{self.obtener_info_asiento()}, "
                f"Reposabrazos: {'Sí' if self.tiene_reposabrazos else 'No'}, "
                f"Reclinable: {'Sí' if self.es_reclinable else 'No'}, "
                f"Precio: ${self.calcular_precio():.2f}")
        
