import math
from data.network_reliable import build_reliable_network
from services.planner import plan_trip
from utils.formatter import format_route

def main():
    graph, start, end = build_reliable_network()
    
    print("--- Planejador de Rotas Confiáveis ---")
    print("(1) Rota Mais Rápida (Pode atrasar)")
    print("(2) Rota Mais Confiável (Maior chance de pontualidade)")
    
    opcao = input("Escolha: ")
    
    # Se escolher confiabilidade, o planejador deve usar o peso logarítmico
    if opcao == "2":
        for edges in graph.values():
            for edge in edges:
                edge.weight = edge.reliability_weight
        criterio = "reliability"
    else:
        criterio = "time"

    result = plan_trip(graph, start, end, criterion=criterio)
    
    format_route(result)
    
    # Cálculo da probabilidade final para exibição
    if criterio == "reliability":
        prob = math.exp(-result["total_time"]) * 100
        print(f"✅ Probabilidade de sucesso: {prob:.2f}%")

if __name__ == "__main__":
    main()