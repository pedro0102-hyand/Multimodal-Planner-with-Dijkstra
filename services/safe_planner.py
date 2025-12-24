def filter_secure_graph(graph, min_security): #recebe o grafo e o nível mínimo de seguranca
    safe_graph = {} #versao filtrada do grafo original
    for station, edges in graph.items():
        safe_graph[station] = [
            e for e in edges if e.security_level >= min_security
        ]
    return safe_graph