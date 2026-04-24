import pytest
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.concretos.sofa import Sofa
from models.concretos.cama import Cama
from models.concretos.sofacama import SofaCama

def test_silla_precio_y_descripcion():
    silla = Silla("Silla comedor", "Madera", "Blanco", 100, respaldo=True)
    assert silla.calcular_precio() == 150
    assert "con respaldo" in silla.obtener_descripcion()

def test_mesa_precio_y_descripcion():
    mesa = Mesa("Mesa comedor", "Metal", "Negro", 200, forma="rectangular", tamaño="grande", plazas=6)
    assert mesa.calcular_precio() == 200 + (6 * 20)
    assert "rectangular" in mesa.obtener_descripcion()

def test_sofa_precio_y_descripcion():
    sofa = Sofa("Sofá", "Tela", "Gris", 400, plazas=3, es_reclinable=True)
    assert sofa.calcular_precio() == 400 + (3*100) + 200
    assert "reclinable" in sofa.obtener_descripcion()

def test_cama_precio_y_descripcion():
    cama = Cama("Cama", "Madera", "Café", 500, forma="rectangular", tamaño="grande", tiene_cabecera=True)
    assert cama.calcular_precio() == 800
    assert "con cabecera" in cama.obtener_descripcion()

def test_sofacama_precio_y_descripcion():
    sofacama = SofaCama("Sofá cama", "Tela", "Gris", 500, plazas=3, tamaño="grande")
    assert isinstance(sofacama.calcular_precio(), (int, float))
    assert "sofá" in sofacama.obtener_descripcion().lower()
    assert "cama" in sofacama.obtener_descripcion().lower()
