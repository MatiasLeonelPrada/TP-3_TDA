import pulp

def hitting_set_lineal(A, B):
    """
    A: Set/Lista de elementos (jugadores disponibles).
    B: Lista de sets (cada set contiene los jugadores pedidos por un medio).
    """
    jugadores = list(A)
    # Aclaramos que vamos a minimizar el número de jugadores seleccionados
    prob = pulp.LpProblem("Minimum_Hitting_Set_Scaloneta", pulp.LpMinimize)

    # variables binarias para cada jugador disponible
    x = pulp.LpVariable.dicts("jugador", jugadores, cat=pulp.LpBinary)
    # Funcion a optimizar: minimizar el número de jugadores seleccionados
    prob += pulp.lpSum([x[j] for j in jugadores]), "Minimizar_jugadores"

    # cada conjunto debe tener al menos un jugador seleccionado
    for i, subset in enumerate(B):
        prob += pulp.lpSum([x[j] for j in subset if j in x]) >= 1, f"Cobertura_Medio_{i+1}"

    # resolver sin mensajes de log
    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    mejor_solucion = [j for j in jugadores if x[j].varValue == 1.0]
    return mejor_solucion


if __name__ == "__main__":
    # Mismo set de pruebas del script original
    jugadores_convocados = {"Messi", "Roncaglia", "Mateo Messi", "De Paul", "Dibujo Martínez", "Scaloni_Jr"}

    prensa_deseos = [
        {"Roncaglia", "Messi"},        # Medio 1
        {"Mateo Messi"},               # Medio 2
        {"De Paul", "Mateo Messi"},    # Medio 3
        {"Dibujo Martínez", "Messi"}   # Medio 4
    ]

    solucion = hitting_set_lineal(jugadores_convocados, prensa_deseos)
    print(f"La Scaloneta mínima para el amistoso es: {solucion}")
    print(f"Tamaño del conjunto (k mínimo): {len(solucion)}")