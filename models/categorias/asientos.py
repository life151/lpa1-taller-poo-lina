from models.mueble import Mueble

class Asiento(Mueble):
    def __init__(self, nombre, material, color, precio_base):
        # Llamada directa a Mueble, no super()
        Mueble.__init__(self, nombre, material, color, precio_base)
