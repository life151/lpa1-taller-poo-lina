"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

# TODO: Importar la clase padre Mueble
from ..mueble import Mueble

# TODO: Importar ABC y abstractmethod si es necesario
from abc import abstractmethod


class Asiento(Mueble):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        """
        Constructor para muebles de asiento.
        """
        # TODO: Llamar al constructor de la clase padre usando super()
        super().__init__(nombre, material, color, precio_base)

        # TODO: Inicializar los atributos específicos de asiento
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado

    # TODO: Implementar propiedades (getters) para los nuevos atributos
    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas

    @property
    def tiene_respaldo(self) -> bool:
        return self._tiene_respaldo

    @property
    def material_tapizado(self) -> str:
        return self._material_tapizado

    # TODO: Implementar setters con validaciones apropiadas
    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        if value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_personas = value

    @tiene_respaldo.setter
    def tiene_respaldo(self, value: bool) -> None:
        self._tiene_respaldo = value

    @material_tapizado.setter
    def material_tapizado(self, value: str) -> None:
        self._material_tapizado = value

    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        """
        factor = 1.0

        # TODO: Agregar lógica aquí
        if self.tiene_respaldo:
            factor += 0.1

        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.2
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1

        if self.capacidad_personas > 1:
            factor += 0.05 * (self.capacidad_personas - 1)

        return factor

    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        """
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info

    # TODO: Mantener el método calcular_precio como abstracto
    @abstractmethod
    def calcular_precio(self) -> float:
        pass

    # TODO: Mantener el método obtener_descripcion como abstracto
    @abstractmethod
    def obtener_descripcion(self) -> str:
        pass
    
