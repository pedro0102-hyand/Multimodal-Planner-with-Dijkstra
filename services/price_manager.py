import random

# percorre o grafo e ajusta o preco para um tipo específico de transporte
def apply_dynamic_pricing(graph, transport_type="Uber", multiplier = None):

    if multiplier is None:
        multiplier = round(random.uniform(1.0, 2.5), 2)

        for station in graph:
            for edge in graph[station]:
                if edge.transport == transport_type:
                    #preco original é multiplicado pela demanda atual
                    edge.price = round(edge.price * multiplier, 2)
        
        return multiplier