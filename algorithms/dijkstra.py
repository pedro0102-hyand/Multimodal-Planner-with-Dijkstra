import heapq #fila de prioridade

def dijkstra(graph, start):

    distances = {node: float("inf") for node in graph} #menor tempo até cada estacao
    previous = {node: None for node in graph} #caminho anterior
    used_transport = {node: None for node in graph}

    distances[start] = 0
    queue = [(0, start)] #armazena o vértice inicial na fila de prioridade

    while queue:

        current_dist, current_node = heapq.heappop(queue) #melhor candidato

        if current_dist > distances[current_node]:
            continue

        for edge in graph[current_node]:

            neighbor = edge.destination
            new_dist = current_dist + edge.weigth #relaxamento da aresta

            if new_dist < distances[neighbor]:

                #atualizacao do melhor caminho
                distances[neighbor] = new_dist
                previous[neighbor] = current_node
                used_transport[neighbor] = edge.transport
                heapq.heappush(queue, (new_dist, neighbor))

    return distances, previous, used_transport

