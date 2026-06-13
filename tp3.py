def hitting_set_backtracking(A, B):
    """
    A: Lista de elementos (jugadores disponibles).
    B: Lista de sets (cada set contiene los jugadores pedidos por un medio).
    """
    #  A a lista
    jugadores = list(A)
    n = len(jugadores)
    m = len(B)

    # Peor caso inicial: todos
    mejor_solucion = list(A)

    # Para optimizar, precalculamos qué conjuntos B_i cubre cada jugador
    # conjuntos_por_jugador[j] guardará los índices de los medios que quieren al jugador j
    conjuntos_por_jugador = {j: set() for j in jugadores}
    for i, subset in enumerate(B):
        for jugador in subset:
            if jugador in conjuntos_por_jugador:
                conjuntos_por_jugador[jugador].add(i)

    def backtrack(idx, conjunto_actual, medios_cubiertos):
        nonlocal mejor_solucion

        # CASO BASE 1: Si se cubren a todos los medios de prensa
        if len(medios_cubiertos) == m:
            if len(conjunto_actual) < len(mejor_solucion):
                mejor_solucion = list(conjunto_actual)
            return

        # PODA
        if len(conjunto_actual) >= len(mejor_solucion):
            return

        # CASO BASE 2: Si ya no hay jugadores para evaluar pero no se cubrio a todos
        if idx == n:
            return

        jugador_actual = jugadores[idx]

        # OPCIÓN 1: INCLUIR al jugador actual
        nuevos_medios = conjuntos_por_jugador[jugador_actual]
        medios_cubiertos_actualizado = medios_cubiertos | nuevos_medios

        conjunto_actual.append(jugador_actual)
        backtrack(idx + 1, conjunto_actual, medios_cubiertos_actualizado)
        conjunto_actual.pop()  # Deshacer cambio (Backtrack)

        # OPCIÓN 2: NO INCLUIR al jugador actual
        backtrack(idx + 1, conjunto_actual, medios_cubiertos)

    backtrack(0, [], set())

    return mejor_solucion


if __name__ == "__main__":
    jugadores_convocados = {"Messi", "Roncaglia", "Mateo Messi", "De Paul", "Dibujo Martínez", "Scaloni_Jr"}

    prensa_deseos = [
        {"Roncaglia", "Messi"},  # Medio 1
        {"Mateo Messi"},  # Medio 2
        {"De Paul", "Mateo Messi"},  # Medio 3
        {"Dibujo Martínez", "Messi"}  # Medio 4
    ]

    solucion = hitting_set_backtracking(jugadores_convocados, prensa_deseos)
    print(f"La Scaloneta mínima para el amistoso es: {solucion}")
    print(f"Tamaño del conjunto (k mínimo): {len(solucion)}")
