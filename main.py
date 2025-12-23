from data.network_dynamic import build_dynamic_network
from services.price_manager import apply_dynamic_pricing
from services.planner import plan_trip
from utils.formatter import format_route

def main():
    graph, start, end = build_dynamic_network()
    
    print("--- Planejador de Viagem: Tarifação Dinâmica ---")
    print(f"Trajeto: {start.name} -> {end.name}")
    
    # Simulação: Detectando alta demanda
    print("\n🔍 Verificando demanda atual para transportes por aplicativo...")
    taxa = apply_dynamic_pricing(graph, transport_type="Uber")
    
    if taxa > 1.0:
        print(f"⚠️ Alerta: Tarifa Dinâmica ativada para Uber (Multiplicador: {taxa}x)")
    else:
        print("✅ Tarifas normais para todos os transportes.")

    # O usuário escolhe se quer economizar dinheiro ou tempo
    print("\nEscolha seu objetivo:")
    print("(1) Menor Tempo (Dijkstra ignora preço)")
    print("(2) Menor Preço (Dijkstra prioriza custo dinâmico)")
    
    opcao = input("Opção: ")
    criterio = "time" if opcao == "1" else "price"

    # O Dijkstra processa o grafo com os novos preços já atualizados
    result = plan_trip(graph, start, end, criterion=criterio)
    format_route(result)

if __name__ == "__main__":
    main()