from algorithms.dijkstra import dijkstra

def plan_trip(graph, start, end):
    distances, previous, transports = dijkstra(graph, start)

    path = [] #lista de rotas
    current = end
    transfers = 0 #contador de baldeacoes
    last_transport = None #troca de modal

    while current:

        #transporte usado para se chegar ao nó
        transport = transports[current]
        #contagem de baldeacoes
        if transport and transport != last_transport:
            transfers += 1
            last_transport = transport

        path.append((current.name, transport))
        current = previous[current]

    path.reverse() #reconstrucao da ordem do caminho

    return {
        "total_time": distances[end],
        "transfers": max(0, transfers - 1),
        "path": path
    }
