from models.station import Station
from models.edge import Edge

def build_dynamic_network():
    A = Station("Centro")
    B = Station("Zona Norte")
    C = Station("Aeroporto")

    # Uber é rápido mas o preço inicial pode sofrer alteração dinâmica
    # Ônibus tem preço fixo e é mais lento
    graph = {
        A: [
            Edge(B, "Ônibus", travel_time=40, price=5.0),
            Edge(B, "Uber", travel_time=15, price=15.0)
        ],
        B: [
            Edge(C, "Ônibus", travel_time=30, price=5.0),
            Edge(C, "Uber", travel_time=10, price=12.0)
        ],
        C: []
    }
    return graph, A, C