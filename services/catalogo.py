import unicodedata
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.concretos.sofa import Sofa
from models.concretos.cama import Cama
from models.concretos.sofacama import SofaCama

class Catalogo:
    def __init__(self):
        self.muebles = [
            Silla("Silla básica", "Madera", "Blanco", 100),
            Mesa("Mesa comedor", "Metal", "Negro", 200, forma="rectangular", tamaño="grande", plazas=6),
            Sofa("Sofá", "Tela", "Gris", 400, plazas=3, es_reclinable=True),
            Cama("Cama", "Madera", "Café", 500, forma="rectangular", tamaño="grande", tiene_cabecera=True),
            SofaCama("Sofá cama", "Tela", "Gris", 500, plazas=3, tamaño="grande")
        ]

    def _normalizar(self, texto: str) -> str:
        return ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        ).lower()

    def listar_muebles(self):
        return [m.obtener_descripcion() for m in self.muebles]

    def buscar_por_nombre(self, nombre: str):
        nombre_norm = self._normalizar(nombre)
        return [m for m in self.muebles if nombre_norm in self._normalizar(m.nombre)]
