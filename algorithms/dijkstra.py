import heapq

def dijkstra(graph, start, criterion="time"):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}
    used_transport = {node: None for node in graph}

    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distances[current_node]:
            continue

        for edge in graph[current_node]:
            neighbor = edge.destination
            
            # Escolha do custo baseada no critério
            if criterion == "price":
                cost = edge.price
            elif criterion == "transfers":
                # Penaliza a mudança de transporte
                last_t = used_transport[current_node]
                cost = 1 if (last_t and edge.transport != last_t) else 0.1
            else:
                cost = edge.weight

            new_dist = current_dist + cost

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                used_transport[neighbor] = edge.transport
                heapq.heappush(queue, (new_dist, neighbor))

    return distances, previous, used_transport

