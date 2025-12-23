from algorithms.dijkstra import dijkstra

def plan_trip(graph, start, end):
    distances, previous, transports = dijkstra(graph, start)

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

    return {
        "total_time": distances[end],
        "transfers": max(0, transfers - 1),
        "path": path
    }
