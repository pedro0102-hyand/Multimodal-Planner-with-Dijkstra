from data.network import build_network
from services.planner import plan_trip
from utils.formatter import format_route

def main():
    graph, start, end = build_network()
    
    print("Escolha o critério de otimização:")
    print("(1) Tempo Mais Rápido")
    print("(2) Preço Mais Baixo")
    print("(3) Menos Baldeações")
    
    opcao = input("Opção: ")
    mapa_opcoes = {"1": "time", "2": "price", "3": "transfers"}
    criterio = mapa_opcoes.get(opcao, "time")

    result = plan_trip(graph, start, end, criterion=criterio)
    format_route(result)

if __name__ == "__main__":
    main()