from models.station import Station
from models.edge import Edge

def build_network():
    A = Station("Estação A")
    B = Station("Estação B")
    C = Station("Estação C")
    D = Station("Estação D")

    graph = {
        A: [
            # Metrô: rápido mas caro
            Edge(B, "Metrô", travel_time=10, price=5.0, wait_time=2),
            # Ônibus: demorado mas barato
            Edge(C, "Ônibus", travel_time=20, price=2.5, wait_time=5)
        ],
        B: [
            Edge(D, "Trem", travel_time=15, price=4.5, wait_time=3, transfer_penalty=4)
        ],
        C: [
            Edge(D, "Ônibus", travel_time=12, price=2.5, wait_time=2)
        ],
        D: []
    }

    return graph, A, D
