import numpy as np
import os
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()
os.makedirs("Informe/img", exist_ok=True)

def graficar(mediciones_file, file_suffix, is_vary_n):
    x = []
    results = {}
    
    try:
        with open(mediciones_file, "r") as f:
            for line in f:
                if line.strip():
                    size, time = line.strip().split(',')
                    size = int(size)
                    time = float(time)
                    x.append(size)
                    results[size] = time
    except FileNotFoundError:
        print(f"El archivo '{mediciones_file}' no se encontró.")
        return

    x = np.array(x)
    y_reales = np.array([results[n] for n in x])
    
    if is_vary_n:
        f = lambda x, c1, c2: c1 * (2.0 ** x) + c2  # Exponencial O(2^N)
        f_label = "O(2^N)"
        f2 = lambda x, c1, c2: c1 * x * x + c2 # Cuadrático O(N^2)
        f2_label = "O(N²)"
        title = 'Complejidad vs Cantidad de Jugadores (M fijo = 15)'
        xlabel = 'Cantidad de Jugadores (N)'
    else:
        f = lambda x, c1, c2: c1 * x + c2  # Lineal O(M)
        f_label = "O(M)"
        f2 = lambda x, c1, c2: c1 * x * x + c2 # Cuadrático O(M^2)
        f2_label = "O(M²)"
        title = 'Complejidad vs Cantidad de Medios (N fijo = 25)'
        xlabel = 'Cantidad de Medios (M)'

    c, _ = sp.optimize.curve_fit(f, x, y_reales)
    c2, _ = sp.optimize.curve_fit(f2, x, y_reales)

    y_predichos = f(x, c[0], c[1])
    y_predichos2 = f2(x, c2[0], c2[1])
    r = np.abs(y_predichos - y_reales)
    r2 = np.abs(y_predichos2 - y_reales)

    # Gráfico de tiempos
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y_reales, color='blue', label='Tiempos medidos', zorder=5)

    x_smooth = np.linspace(min(x), max(x), 500)
    y_smooth = f(x_smooth, c[0], c[1])
    y_smooth2 = f2(x_smooth, c2[0], c2[1])

    if is_vary_n:
        label1 = rf'Ajuste {f_label}: ${c[0]:.2e} \cdot 2^N + {c[1]:.2e}$'
        label2 = rf'Ajuste {f2_label}: ${c2[0]:.2e} \cdot N^2 + {c2[1]:.2e}$'
    else:
        label1 = rf'Ajuste {f_label}: ${c[0]:.2e} \cdot M + {c[1]:.2e}$'
        label2 = rf'Ajuste {f2_label}: ${c2[0]:.2e} \cdot M^2 + {c2[1]:.2e}$'

    plt.plot(x_smooth, y_smooth, color='red', linestyle='--', label=label1)
    plt.plot(x_smooth, y_smooth2, color='blue', linestyle='--', label=label2)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"Informe/img/tiempos_{file_suffix}.png", dpi=300)
    plt.close()

    # Gráfico de error
    plt.figure(figsize=(10, 6))
    plt.plot(x, r, color='red', linestyle='--', marker='o', label=rf'Error {f_label}')
    plt.plot(x, r2, color='blue', linestyle='--', marker='o', label=rf'Error {f2_label}')

    plt.title('Error del ajuste')
    plt.xlabel(xlabel)
    plt.ylabel('Diferencias')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"Informe/img/error_{file_suffix}.png", dpi=300)
    plt.close()
    
    print(f"Gráficos para {file_suffix} generados en Informe/img/")

# Generar ambos gráficos
graficar("mediciones_vary_n.txt", "vary_n", is_vary_n=True)
graficar("mediciones_vary_m.txt", "vary_m", is_vary_n=False)
