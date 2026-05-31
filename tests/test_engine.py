import numpy as np
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Si se ejecuta directo desde raíz:
try:
    from vector_engine import green_circulo, campo_conservativo, stokes_circulo
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from vector_engine import green_circulo, campo_conservativo, stokes_circulo



# PRUEBAS — Ejercicio 1: Green


def test_green_radio_2():
    """El resultado debe ser 24π con radio 2."""
    resultado = green_circulo(2.0)
    assert abs(resultado - 24 * np.pi) < 0.01, \
        f"Green radio 2: esperado {24*np.pi:.4f}, obtenido {resultado:.4f}"

def test_green_radio_1():
    """Con radio 1 el resultado analítico es 3π/2."""
    # ∫∫ 3r³ dr dθ = 3*(1/4)*2π = 3π/2
    resultado = green_circulo(1.0)
    esperado = 3 * np.pi / 2
    assert abs(resultado - esperado) < 0.01, \
        f"Green radio 1: esperado {esperado:.4f}, obtenido {resultado:.4f}"

def test_green_radio_negativo():
    """Debe lanzar ValueError si el radio es negativo."""
    with pytest.raises(ValueError):
        green_circulo(-1.0)

def test_green_radio_cero():
    """Debe lanzar ValueError si el radio es cero."""
    with pytest.raises(ValueError):
        green_circulo(0.0)

def test_green_error_relativo_menor_1_porciento():
    """El error relativo debe ser menor al 1%."""
    resultado = green_circulo(2.0)
    error = abs(resultado - 24 * np.pi) / (24 * np.pi) * 100
    assert error < 1.0, f"Error relativo demasiado alto: {error:.4f}%"



# PRUEBAS — Ejercicio 2: Campo conservativo


def test_conservativo_resultado():
    """El trabajo de A a B debe ser 3 J."""
    W = campo_conservativo((0, 0, 0), (1, 2, 1))
    assert abs(W - 3.0) < 1e-10, \
        f"Trabajo: esperado 3.0000 J, obtenido {W:.6f} J"

def test_conservativo_mismo_punto():
    """El trabajo de un punto a sí mismo debe ser cero."""
    W = campo_conservativo((1, 1, 1), (1, 1, 1))
    assert abs(W) < 1e-10, \
        f"Trabajo A→A: esperado 0, obtenido {W:.6f}"

def test_conservativo_independencia_camino():
    """
    El campo conservativo garantiza W = φ(B) - φ(A),
    independiente del camino. Verificamos con distintos B.
    """
    W1 = campo_conservativo((0, 0, 0), (2, 1, 0))
    W2 = campo_conservativo((0, 0, 0), (1, 4, 0))
    # φ(2,1,0) = 4*1 + 2*0 = 4
    # φ(1,4,0) = 1*4 + 1*0 = 4
    assert abs(W1 - 4.0) < 1e-10, f"W1 esperado 4.0, obtenido {W1}"
    assert abs(W2 - 4.0) < 1e-10, f"W2 esperado 4.0, obtenido {W2}"

def test_conservativo_antisimetria():
    """El trabajo de B a A debe ser el negativo del de A a B."""
    W_ab = campo_conservativo((0, 0, 0), (1, 2, 1))
    W_ba = campo_conservativo((1, 2, 1), (0, 0, 0))
    assert abs(W_ab + W_ba) < 1e-10, \
        f"Antisimetría fallida: W_AB + W_BA = {W_ab + W_ba:.6f}"



# PRUEBAS — Ejercicio 3: Stokes


def test_stokes_radio_2():
    """El resultado debe ser 4π con radio 2."""
    resultado = stokes_circulo(2.0)
    assert abs(resultado - 4 * np.pi) < 0.01, \
        f"Stokes radio 2: esperado {4*np.pi:.4f}, obtenido {resultado:.4f}"

def test_stokes_radio_1():
    """Con radio 1 el resultado debe ser π."""
    resultado = stokes_circulo(1.0)
    assert abs(resultado - np.pi) < 0.01, \
        f"Stokes radio 1: esperado {np.pi:.4f}, obtenido {resultado:.4f}"

def test_stokes_radio_negativo():
    """Debe lanzar ValueError si el radio es negativo."""
    with pytest.raises(ValueError):
        stokes_circulo(-2.0)

def test_stokes_error_relativo_menor_1_porciento():
    """El error relativo debe ser menor al 1%."""
    resultado = stokes_circulo(2.0)
    error = abs(resultado - 4 * np.pi) / (4 * np.pi) * 100
    assert error < 1.0, f"Error relativo demasiado alto: {error:.4f}%"
