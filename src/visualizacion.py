import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D


# FIGURA 1 — Campo vectorial + círculo (Ejercicio 1: Green)


def fig_green():
    # Grilla de puntos
    x = np.linspace(-3, 3, 18)
    y = np.linspace(-3, 3, 18)
    X, Y = np.meshgrid(x, y)

    # F = (x²-y³, x³+y²)
    U = X**2 - Y**3
    V = X**3 + Y**2
    magnitud = np.sqrt(U**2 + V**2)

    fig, ax = plt.subplots(figsize=(6, 6))

    # Campo vectorial coloreado por magnitud
    q = ax.quiver(X, Y, U, V, magnitud, cmap='plasma', scale=300, width=0.003)
    plt.colorbar(q, ax=ax, label='|F|')

    # Círculo C: x²+y²=4, radio 2
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(2 * np.cos(theta), 2 * np.sin(theta), 'r-', linewidth=2.5, label='C: $x^2+y^2=4$')

    # Flecha antihoraria
    ax.annotate('', xy=(-0.1, 2), xytext=(0.1, 2),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))

    # Región D sombreada
    circle_patch = plt.Circle((0, 0), 2, color='green', alpha=0.08)
    ax.add_patch(circle_patch)
    ax.text(0, 0, 'D', fontsize=16, ha='center', va='center', color='green')

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Ejercicio 1 — Teorema de Green\n'
                 r'$\oint_C (x^2-y^3)dx + (x^3+y^2)dy = 24\pi \approx 75.40$')
    ax.legend(loc='upper right')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('fig_green.png', dpi=150, bbox_inches='tight')
    print('[OK] fig_green.png guardada')
    plt.close()



# FIGURA 2 — Curvas de nivel + gradiente (Ejercicio 2: Conservativo)


def fig_potencial():
    x = np.linspace(-0.2, 2.3, 300)
    y = np.linspace(-0.2, 2.8, 300)
    X, Y = np.meshgrid(x, y)

    # φ(x,y) = x²y  (fijando z=0 para visualizar en 2D)
    PHI = X**2 * Y

    fig, ax = plt.subplots(figsize=(6, 6))

    # Curvas de nivel rellenas
    cf = ax.contourf(X, Y, PHI, levels=20, cmap='coolwarm', alpha=0.75)
    plt.colorbar(cf, ax=ax, label='φ(x, y) = x²y')

    # Contornos negros
    ax.contour(X, Y, PHI, levels=20, colors='k', linewidths=0.5, alpha=0.4)

    # Gradiente ∇φ = (2xy, x²)
    xg = np.linspace(0.1, 2.2, 10)
    yg = np.linspace(0.1, 2.7, 10)
    XG, YG = np.meshgrid(xg, yg)
    UG = 2 * XG * YG   # ∂φ/∂x
    VG = XG**2          # ∂φ/∂y
    ax.quiver(XG, YG, UG, VG, color='navy', scale=60, width=0.004, alpha=0.8)

    # Puntos A y B
    ax.plot(0, 0, '*', markersize=14, color='red',   label='A = (0, 0)')
    ax.plot(1, 2, '*', markersize=14, color='lime',  label='B = (1, 2)')
    ax.text(0.08, 0.1, 'A', fontsize=12, color='red')
    ax.text(1.08, 2.1, 'B', fontsize=12, color='lime')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Ejercicio 2 — Campo Conservativo\n'
                 r'$\varphi(x,y,z)=x^2y+xz^2,\quad W=\varphi(B)-\varphi(A)=3\,J$')
    ax.legend(loc='upper left')
    ax.set_xlim(-0.2, 2.3)
    ax.set_ylim(-0.2, 2.8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('fig_potencial.png', dpi=150, bbox_inches='tight')
    print('[OK] fig_potencial.png guardada')
    plt.close()



# FIGURA 3 — Superficie 3D + borde (Ejercicio 3: Stokes)


def fig_stokes():
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Disco S: z=0, x²+y²≤4
    r = np.linspace(0, 2, 40)
    theta = np.linspace(0, 2 * np.pi, 80)
    R, T = np.meshgrid(r, theta)
    XS = R * np.cos(T)
    YS = R * np.sin(T)
    ZS = np.zeros_like(XS)

    ax.plot_surface(XS, YS, ZS, alpha=0.25, color='royalblue', label='S: disco z=0')

    # Borde C: círculo x²+y²=4, z=0
    t = np.linspace(0, 2 * np.pi, 300)
    xc = 2 * np.cos(t)
    yc = 2 * np.sin(t)
    zc = np.zeros(300)
    ax.plot(xc, yc, zc, 'r-', linewidth=3, label='C: $x^2+y^2=4$')

    # Vector normal n=k desde el centro
    ax.quiver(0, 0, 0, 0, 0, 2, color='darkgreen', linewidth=3,
              arrow_length_ratio=0.2, label='n = k')
    ax.text(0.15, 0.15, 2.1, 'n = k', color='darkgreen', fontsize=11)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Ejercicio 3 — Teorema de Stokes\n'
                 r'$\oint_C \mathbf{F}\cdot d\mathbf{r}=4\pi\approx12.57$')
    ax.legend(loc='upper left', fontsize=9)
    ax.set_zlim(0, 2.5)

    plt.tight_layout()
    plt.savefig('fig_stokes.png', dpi=150, bbox_inches='tight')
    print('[OK] fig_stokes.png guardada')
    plt.close()



# MAIN


if __name__ == '__main__':
    fig_green()
    fig_potencial()
    fig_stokes()
    print('\n[OK] Las 3 figuras fueron generadas exitosamente.')