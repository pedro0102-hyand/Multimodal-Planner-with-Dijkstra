import heapq

def dijkstra(graph, start):

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
            new_dist = current_dist + edge.weigth

            if new_dist < distances[neighbor]:

                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                used_transport[neighbor] = edge.transport
                heapq.heappush(queue, (new_dist, neighbor))

    return distances, previous, used_transport

