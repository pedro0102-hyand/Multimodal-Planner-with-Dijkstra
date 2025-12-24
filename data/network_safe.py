from models.station import Station
from models.secure_edge import SecureEdge

def build_safe_network():
    A = Station("Praça Central")
    B = Station("Rua das Flores")
    C = Station("Avenida Iluminada")
    D = Station("Terminal")

    graph = {
        A: [
            # Beco: muito rápido (5min), mas perigoso (nível 2)
            SecureEdge(B, "Caminhada", travel_time=5, security_level=2),
            # Avenida: mais lenta (15min), mas segura (nível 9)
            SecureEdge(C, "Caminhada", travel_time=15, security_level=9)
        ],
        B: [
            SecureEdge(D, "Caminhada", travel_time=5, security_level=3)
        ],
        C: [
            SecureEdge(D, "Caminhada", travel_time=10, security_level=8)
        ],
        D: []
    }
    return graph, A, D