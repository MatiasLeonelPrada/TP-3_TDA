import time
import random
from tp3 import hitting_set_backtracking

def generar_caso_aleatorio(num_jugadores, num_medios, max_jugadores_por_medio):
    A = [f"Jugador_{i}" for i in range(num_jugadores)]
    B = []
    for _ in range(num_medios):
        k = random.randint(1, min(max_jugadores_por_medio, num_jugadores))
        subset = set(random.sample(A, k))
        B.append(subset)
    return set(A), B

print(f"{'Jugadores (n)':<15}{'Medios (m)':<15}{'Tiempo (segundos)':<20}{'Tamaño Óptimo'}")
print("-" * 65)

# 1. Fijar Medios (M) y variar Jugadores (N)
M_fijo = 15
# Agregamos más puntos: hasta 34 para que se vea mejor la curva exponencial
sample_sizes_n = [(n, M_fijo) for n in range(10, 35, 2)] 

print("== Midiendo para M fijo (15) y N variable ==")
with open("mediciones_vary_n.txt", "w") as f:
    for n, m in sample_sizes_n:
        A, B = generar_caso_aleatorio(n, m, max_jugadores_por_medio=4)
        start_time = time.time()
        res = hitting_set_backtracking(A, B)
        tiempo = time.time() - start_time
        print(f"N={n:<5} M={m:<5} Tiempo={tiempo:<15.6f} Optimo={len(res)}")
        f.write(f"{n},{tiempo}\n")

# 2. Fijar Jugadores (N) y variar Medios (M)
N_fijo = 25
# Agregamos más puntos: hasta 80 para que se vea mejor la curva lineal vs cuadrática
sample_sizes_m = [(N_fijo, m) for m in range(5, 81, 5)] 

print("\n== Midiendo para N fijo (25) y M variable ==")
with open("mediciones_vary_m.txt", "w") as f:
    for n, m in sample_sizes_m:
        A, B = generar_caso_aleatorio(n, m, max_jugadores_por_medio=4)
        start_time = time.time()
        res = hitting_set_backtracking(A, B)
        tiempo = time.time() - start_time
        print(f"N={n:<5} M={m:<5} Tiempo={tiempo:<15.6f} Optimo={len(res)}")
        f.write(f"{m},{tiempo}\n")

print("\n¡Mediciones generadas en 'mediciones_vary_n.txt' y 'mediciones_vary_m.txt'!")
