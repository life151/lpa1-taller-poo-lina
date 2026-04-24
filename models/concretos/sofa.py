from models.categorias.asientos import Asiento

class Sofa(Asiento):
    def __init__(self, nombre, material, color, precio_base, plazas=2,
                 tiene_respaldo=True, material_tapizado="tela",
                 es_reclinable=False, es_modular=False):
        # Llamada directa a Asiento, no super()
        Asiento.__init__(self, nombre, material, color, precio_base)
        self.plazas = plazas
        self.tiene_respaldo = tiene_respaldo
        self.material_tapizado = material_tapizado
        self.es_reclinable = es_reclinable
        self.es_modular = es_modular

    def calcular_precio(self):
        extra = self.plazas * 100
        if self.es_reclinable: extra += 200
        if self.es_modular: extra += 300
        return self.precio_base + extra

    def obtener_descripcion(self):
        return (f"{self.nombre} de {self.material} color {self.color}, "
                f"{self.plazas} plazas, tapizado en {self.material_tapizado}, "
                f"{'reclinable' if self.es_reclinable else 'no reclinable'}, "
                f"{'modular' if self.es_modular else 'no modular'}")
