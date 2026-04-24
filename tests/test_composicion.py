"""
Pruebas unitarias para las clases de composición.
"""
import pytest
from models.concretos.mesa import Mesa
from models.concretos.silla import Silla
from models.composicion.comedor import Comedor

def test_comedor_precio_y_descripcion():
    mesa = Mesa("Mesa comedor", "Madera", "Blanco", 300, forma="rectangular", tamaño="grande", plazas=6)
    comedor = Comedor(mesa)
    comedor.agregar_silla(Silla("Silla comedor", "Madera", "Blanco", 100, respaldo=True))
    comedor.agregar_silla(Silla("Silla comedor", "Madera", "Blanco", 100, respaldo=False))

    precio_total = comedor.calcular_precio()
    assert precio_total > 300
    desc = comedor.obtener_descripcion()
    assert "Comedor" in desc
    assert "sillas" in desc
