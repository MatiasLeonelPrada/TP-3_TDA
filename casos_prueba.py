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

with open("mediciones.txt", "w") as f:
    for n, m in [(10, 5), (12, 6), (14, 7), (16, 8), (18, 9), (20, 10), (22, 11), (24, 12), (26, 13), (28, 14), (30, 15)]:
        A, B = generar_caso_aleatorio(n, m, max_jugadores_por_medio=4)
        
        start_time = time.time()
        res = hitting_set_backtracking(A, B)
        end_time = time.time()
        tiempo = end_time - start_time
        
        print(f"{n:<15}{m:<15}{tiempo:<20.6f}{len(res)}")
        f.write(f"{n},{tiempo}\n")
