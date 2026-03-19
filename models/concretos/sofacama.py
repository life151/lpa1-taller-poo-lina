"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

# TODO: Importar las clases padre
from .sofa import Sofa
from .cama import Cama


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        """
        Constructor del sofá-cama.
        """
        # TODO: Inicializar usando las clases padre
        super().__init__(nombre, material, color, precio_base,
                         capacidad_personas, True, material_tapizado)

        # TODO: Inicializar atributos específicos de cama
        self._tamaño_cama = tamaño_cama
        self._incluye_colchon = incluye_colchon

        # TODO: Inicializar atributos únicos del sofá-cama
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"  # Puede ser "sofa" o "cama"

    # TODO: Implementar propiedades para los nuevos atributos
    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion

    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual (sofa o cama)."""
        return self._modo_actual

    def convertir_a_cama(self) -> str:
        """Convierte el sofá en cama."""
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"

        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"

    def convertir_a_sofa(self) -> str:
        """Convierte la cama en sofá."""
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"

        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"

    def calcular_precio(self) -> float:
        """Calcula el precio combinando las funcionalidades de sofá y cama."""
        precio = self.precio_base

        # Factor de comodidad del asiento
        precio *= self.calcular_factor_comodidad()

        # Funcionalidad dual
        precio *= 1.5

        # Costo por mecanismo
        if self.mecanismo_conversion == "electrico":
            precio += 200
        elif self.mecanismo_conversion == "hidraulico":
            precio += 150
        else:  # manual/plegable
            precio += 100

        # Costo por colchón
        if self._incluye_colchon:
            precio += 300

        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """Descripción que combina características de sofá y cama."""
        descripcion = f"Sofá-cama {self.nombre} fabricado en {self.material} color {self.color}."
        descripcion += f"\n{self.obtener_info_asiento()}"
        descripcion += f"\nTamaño de cama: {self._tamaño_cama}"
        descripcion += f"\nMecanismo de conversión: {self.mecanismo_conversion}"
        descripcion += f"\nColchón incluido: {'Sí' if self._incluye_colchon else 'No'}"
        descripcion += f"\nModo actual: {self.modo_actual}"
        descripcion += f"\nPrecio: ${self.calcular_precio():.2f}"
        return descripcion

    def obtener_capacidad_total(self) -> dict:
        """Obtiene la capacidad tanto como sofá como cama."""
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2 if self._tamaño_cama in ["matrimonial", "queen", "king"] else 1
        }
        return capacidades

    # TODO: Implementar método para verificar compatibilidad de modo
    def puede_usar_como_cama(self) -> bool:
        """Verifica si actualmente puede usarse como cama."""
        return self._modo_actual == "cama"

    def puede_usar_como_sofa(self) -> bool:
        """Verifica si actualmente puede usarse como sofá."""
        return self._modo_actual == "sofa"

    def __str__(self) -> str:
        """Representación en cadena del sofá-cama."""
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
