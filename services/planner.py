from algorithms.dijkstra import dijkstra

def plan_trip(graph, start, end, criterion="time"):
    distances, previous, transports = dijkstra(graph, start, criterion)

    path = []
    current = end
    transfers = 0
    last_transport = None

    while current:
        transport = transports[current]
        if transport and transport != last_transport:
            transfers += 1
            last_transport = transport

        path.append((current.name, transport))
        current = previous[current]

    path.reverse()

    total_cost = 0
    if distances[end] != float("inf"):
        # Se o critério for tempo, a distância é o tempo
        # Se o critério for preço, a distância é o preço total acumulado
        total_cost = distances[end]

    return {
        "total_time": total_cost,
        "transfers": max(0, transfers - 1),
        "path": path,
        "criterion": criterion # Adicionamos o critério para o formatador saber o que exibir
    }
