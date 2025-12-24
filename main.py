from data.network_safe import build_safe_network
from services.safe_planner import filter_secure_graph
from services.planner import plan_trip
from utils.formatter import format_route

def main():
    graph, start, end = build_safe_network()
    
    print("--- Planeador de Caminhada Noturna Segura ---")
    print(f"Trajeto: {start.name} -> {end.name}")
    
    try:
        limite = int(input("\nDigite o nível mínimo de segurança desejado (1-10): "))
    except ValueError:
        limite = 1

    # Filtramos o grafo antes do Dijkstra agir
    graph = filter_secure_graph(graph, limite)
    
    # O Dijkstra tentará encontrar o caminho mais rápido dentro das opções seguras
    result = plan_trip(graph, start, end, criterion="time")
    
    if result["total_time"] == float("inf") or not result["path"]:
        print(f"\n❌ Erro: Não existe um caminho seguro o suficiente para o nível {limite}.")
    else:
        print(f"\n✅ Rota encontrada com nível de segurança >= {limite}:")
        format_route(result)

if __name__ == "__main__":
    main()