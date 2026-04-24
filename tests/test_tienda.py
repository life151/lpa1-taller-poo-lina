import pytest
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla
import pytest
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla

def test_tienda_agregar_y_calcular_total():
    tienda = TiendaMuebles()
    silla = Silla("Silla comedor", "Madera", "Blanco", 100, respaldo=True)
    tienda.agregar_mueble(silla)

    assert len(tienda.inventario) == 1
    assert tienda.calcular_total() == silla.calcular_precio()
