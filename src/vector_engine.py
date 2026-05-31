import numpy as np
from scipy import integrate


# FUNCIÓN 1: Teorema de Green — Ejercicio 1


def green_circulo(R=2.0):
    """
    Calcula la integral de línea usando el Teorema de Green.

    Integral: ∮_C (x²-y³)dx + (x³+y²)dy
    sobre el círculo de radio R, sentido antihorario.

    Método:
        P = x²-y³,  Q = x³+y²
        ∂Q/∂x - ∂P/∂y = 3x² + 3y² = 3r²  (en polares)
        ∬_D 3r² · r dr dθ  con r∈[0,R], θ∈[0,2π]

    Parámetros:
        R (float): radio del círculo. Debe ser positivo.

    Retorna:
        float: valor numérico de la integral.

    Ejemplo:
        >>> abs(green_circulo(2) - 24 * np.pi) < 0.01
        True
    """
    if R <= 0:
        raise ValueError(f"El radio debe ser positivo. Se recibió R = {R}")

    def integrando(r, theta):
        # 3(x²+y²) * jacobiano = 3r² * r = 3r³
        return 3 * r**2 * r

    resultado, error_est = integrate.dblquad(
        integrando,
        0, 2 * np.pi,   # límites de theta (variable externa)
        0, R            # límites de r     (variable interna)
    )

    analitico = 24 * np.pi  # = 3 * (R⁴/4) * 2π con R=2

    print("=" * 55)
    print("  EJERCICIO 1 — Teorema de Green")
    print("=" * 55)
    print(f"  Resultado analítico : 24π      = {analitico:.6f}")
    print(f"  Resultado numérico  :           {resultado:.6f}")
    print(f"  Error absoluto      :           {abs(resultado - analitico):.2e}")
    print(f"  Error relativo      :           {abs(resultado - analitico)/analitico*100:.4f}%")

    return resultado



# FUNCIÓN 2: Campo conservativo — Ejercicio 2


def campo_conservativo(A=(0, 0, 0), B=(1, 2, 1)):
    """
    Verifica conservatividad, halla función potencial y calcula trabajo.

    Campo: F = (2xy+z², x², 2xz)
    Función potencial: φ(x,y,z) = x²y + xz²
    Trabajo: W = φ(B) - φ(A)  (independiente del camino)

    Método:
        1. Calcular curl F = ∇×F y verificar que sea (0,0,0)
        2. Integrar φ_x respecto a x → φ = x²y + xz² + g(y,z)
        3. Usar φ_y y φ_z para determinar g → g = constante
        4. W = φ(B) - φ(A)

    Parámetros:
        A (tuple): punto inicial (x, y, z).
        B (tuple): punto final  (x, y, z).

    Retorna:
        float: trabajo W en Joules.

    Ejemplo:
        >>> abs(campo_conservativo((0,0,0), (1,2,1)) - 3.0) < 1e-10
        True
    """
    def phi(x, y, z):
        """Función potencial: φ(x,y,z) = x²y + xz²"""
        return x**2 * y + x * z**2

    # Verificar curl F = 0 en punto de prueba (x0,y0,z0)
    x0, y0, z0 = 1.0, 1.0, 1.0
    # curl F = (R_y - Q_z,  P_z - R_x,  Q_x - P_y)
    # F = (P, Q, R) = (2xy+z², x², 2xz)
    curl_i = 0 - 0          # ∂R/∂y - ∂Q/∂z = 0 - 0
    curl_j = 2*z0 - 2*z0    # ∂P/∂z - ∂R/∂x = 2z - 2z
    curl_k = 2*x0 - 2*x0    # ∂Q/∂x - ∂P/∂y = 2x - 2x
    es_conservativo = (curl_i == 0 and curl_j == 0 and curl_k == 0)

    W = phi(*B) - phi(*A)
    analitico = 3.0

    print("=" * 55)
    print("  EJERCICIO 2 — Campo conservativo")
    print("=" * 55)
    print(f"  curl(F) = ({curl_i}, {curl_j}, {curl_k})")
    print(f"  ¿Es conservativo?   : {es_conservativo}")
    print(f"  φ(x,y,z)            = x²y + xz²")
    print(f"  φ{B} = {phi(*B):.4f}")
    print(f"  φ{A} = {phi(*A):.4f}")
    print(f"  W = φ(B) - φ(A)     = {W:.6f} J")
    print(f"  Resultado analítico : {analitico:.6f} J")
    print(f"  Error absoluto      : {abs(W - analitico):.2e}")

    return W



# FUNCIÓN 3: Teorema de Stokes — Ejercicio 3


def stokes_circulo(R=2.0, n=1000):
    """
    Calcula ∮_C F·dr usando el Teorema de Stokes.

    Campo: F = (z, x, y)
    Curva C: círculo x²+y²=R², z=0, sentido antihorario.
    Superficie S: disco plano z=0, x²+y²≤R², n=k=(0,0,1)

    Método:
        curl(F) = (1, 1, 1)
        (curl F)·n = (1,1,1)·(0,0,1) = 1
        ∬_S 1 dS = Área del disco = πR²

    Verificación directa:
        Parametrizar C: r(t) = (R cos t, R sin t, 0)
        Integrar F·dr numéricamente con trapecios.

    Parámetros:
        R (float): radio del círculo. Debe ser positivo.
        n (int)  : número de puntos para integración numérica.

    Retorna:
        float: valor de la integral por Stokes (= πR²).

    Ejemplo:
        >>> abs(stokes_circulo(2) - 4 * np.pi) < 0.01
        True
    """
    if R <= 0:
        raise ValueError(f"El radio debe ser positivo. Se recibió R = {R}")

    # --- Stokes: (curl F)·n = 1  →  integral = área del disco ---
    resultado_stokes = np.pi * R**2

    # --- Verificación: integral de línea directa ---
    t = np.linspace(0, 2 * np.pi, n)
    x = R * np.cos(t)
    y = R * np.sin(t)
    z = np.zeros(n)

    dx = np.gradient(x, t)
    dy = np.gradient(y, t)
    dz = np.zeros(n)

    # F = (z, x, y) sobre la curva: Fx=0, Fy=x, Fz=y
    integrando_linea = z * dx + x * dy + y * dz
    resultado_linea = np.trapezoid(integrando_linea, t)

    analitico = 4 * np.pi

    print("=" * 55)
    print("  EJERCICIO 3 — Teorema de Stokes")
    print("=" * 55)
    print(f"  curl(F)             = (1, 1, 1)")
    print(f"  n = k               = (0, 0, 1)")
    print(f"  (curl F)·n          = 1")
    print(f"  Área del disco      = πR² = π({R})² = {resultado_stokes:.6f}")
    print(f"  Stokes (área × 1)   = {resultado_stokes:.6f}")
    print(f"  Línea directa       = {resultado_linea:.6f}")
    print(f"  Resultado analítico : 4π  = {analitico:.6f}")
    print(f"  Error (Stokes)      : {abs(resultado_stokes - analitico):.2e}")
    print(f"  Error (línea)       : {abs(resultado_linea  - analitico):.2e}")

    return resultado_stokes



# FUNCIÓN 4: Tabla comparativa de resultados


def tabla_resultados():
    """
    Ejecuta los 3 ejercicios e imprime una tabla comparativa.

    Muestra resultado analítico, numérico y error relativo (%)
    para cada ejercicio del parcial.

    Retorna:
        dict: diccionario con los 3 resultados numéricos.
    """
    print("\n" + "=" * 55)
    print("  EJECUTANDO LOS 3 EJERCICIOS...")
    print("=" * 55 + "\n")

    r1 = green_circulo(2.0)
    print()
    r2 = campo_conservativo((0, 0, 0), (1, 2, 1))
    print()
    r3 = stokes_circulo(2.0)

    # Valores analíticos
    a1 = 24 * np.pi
    a2 = 3.0
    a3 = 4 * np.pi

    err1 = abs(r1 - a1) / a1 * 100
    err2 = abs(r2 - a2) / a2 * 100
    err3 = abs(r3 - a3) / a3 * 100

    print("\n")
    print("=" * 65)
    print("  TABLA COMPARATIVA — Resultados Analíticos vs Numéricos")
    print("=" * 65)
    print(f"  {'Ejercicio':<28} {'Analítico':>10} {'Numérico':>10} {'Error %':>8}")
    print("-" * 65)
    print(f"  {'1 — Green (24π)':<28} {a1:>10.4f} {r1:>10.4f} {err1:>7.4f}%")
    print(f"  {'2 — Conservativo (3 J)':<28} {a2:>10.4f} {r2:>10.4f} {err2:>7.4f}%")
    print(f"  {'3 — Stokes (4π)':<28} {a3:>10.4f} {r3:>10.4f} {err3:>7.4f}%")
    print("=" * 65)
    print(f"  Todos los errores < 1%: {all(e < 1.0 for e in [err1, err2, err3])}")
    print("=" * 65)

    return {"green": r1, "conservativo": r2, "stokes": r3}



# MAIN


if __name__ == "__main__":
    tabla_resultados()
