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

        # Armazena apenas dados simples para o formatador
        path.append((current.name, transport))
        current = previous[current]

    path.reverse()

    # Cálculo do tempo total real percorrendo o grafo novamente 
    # ou usando a distância se o critério for tempo
    total_time = 0
    if distances[end] != float("inf"):
        # Se o critério for tempo, a distância já é o tempo total
        if criterion == "time":
            total_time = distances[end]
        else:
            # Caso contrário, seria necessário reconstruir os objetos Edge 
            # para somar. Por agora, retornamos o custo do critério.
            total_time = "Calculado por " + criterion

    return {
        "total_time": total_time,
        "transfers": max(0, transfers - 1),
        "path": path
    }
