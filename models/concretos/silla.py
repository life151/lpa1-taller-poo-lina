"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

# TODO: Importar la clase padre Asiento
from ..categorias.asientos import Asiento


class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        """
        Constructor de la silla.
        """
        # TODO: Llamar al constructor padre con capacidad fija de 1 persona
        super().__init__(nombre, material, color, precio_base, 1, tiene_respaldo, material_tapizado)

        # TODO: Inicializar atributos específicos de la silla
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas

    # TODO: Implementar propiedades para los nuevos atributos
    @property
    def altura_regulable(self) -> bool:
        """Getter para altura regulable."""
        return self._altura_regulable

    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        """Setter para altura regulable."""
        self._altura_regulable = value

    @property
    def tiene_ruedas(self) -> bool:
        return self._tiene_ruedas

    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        self._tiene_ruedas = value

    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillas.
        """
        # 1. Comenzar con el precio base
        precio = self.precio_base

        # 2. Aplicar factor de comodidad heredado
        precio *= self.calcular_factor_comodidad()

        # 3. Agregar costos por características especiales
        if self.altura_regulable:
            precio += 50
        if self.tiene_ruedas:
            precio += 30

        # 4. Retornar precio redondeado a 2 decimales
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la silla.
        """
        descripcion = f"Silla: {self.nombre}, Material: {self.material}, Color: {self.color}, "
        descripcion += f"Precio base: {self.precio_base}, {self.obtener_info_asiento()}"
        if self.altura_regulable:
            descripcion += ", Altura regulable"
        if self.tiene_ruedas:
            descripcion += ", Con ruedas"
        return descripcion

    def regular_altura(self, nueva_altura: int) -> str:
        """
        Simula la regulación de altura de la silla.
        """
        if not self.altura_regulable:
            return "Esta silla no permite regular la altura."
        return f"La altura de la silla ha sido ajustada a {nueva_altura} cm."

    def es_silla_oficina(self) -> bool:
        """
        Determina si la silla es adecuada para oficina.
        """
        # TODO: Una silla es de oficina si tiene ruedas Y altura regulable
        return self.tiene_ruedas and self.altura_regulable
    