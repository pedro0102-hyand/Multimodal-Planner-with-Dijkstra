from models.station import Station
from models.reliable_edge import ReliableEdge

def build_reliable_network():
    A = Station("Ponto Inicial")
    B = Station("Via Expressa")
    C = Station("Linha Férrea")
    D = Station("Destino Final")

    graph = {
        A: [
            # Caminho via Autocarro: rápido mas incerto (70% confiável)
            ReliableEdge(B, "Ônibus", travel_time=10, reliability=0.7),
            # Caminho via Comboio: lento mas garantido (99% confiável)
            ReliableEdge(C, "Trem", travel_time=25, reliability=0.99)
        ],
        B: [
            ReliableEdge(D, "Ônibus", travel_time=10, reliability=0.7)
        ],
        C: [
            ReliableEdge(D, "Trem", travel_time=10, reliability=0.99)
        ],
        D: []
    }
    return graph, A, D