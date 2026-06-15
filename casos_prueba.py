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

for n, m in [(10, 5), (15, 10), (20, 15), (25, 20), (30, 25)]:
    A, B = generar_caso_aleatorio(n, m, max_jugadores_por_medio=3)
    
    start_time = time.time()
    res = hitting_set_backtracking(A, B)
    end_time = time.time()
    
    print(f"{n:<15}{m:<15}{end_time - start_time:<20.6f}{len(res)}")
