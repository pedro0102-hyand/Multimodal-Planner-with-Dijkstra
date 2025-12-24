import math
from models.edge import Edge

class ReliableEdge(Edge):
    def __init__(self, destination, transport, travel_time, price=0.0, reliability=1.0):
        super().__init__(destination, transport, travel_time, price)
        # reliability: chance de 0.0 a 1.0 de chegar no horário
        self.reliability = reliability
        
        # O peso para o Dijkstra será o logaritmo negativo da confiabilidade.
        # Quanto maior a probabilidade (perto de 1.0), menor será o peso (perto de 0).
        # Se reliability for 1.0, -log(1.0) = 0 (custo zero de incerteza).
        if reliability > 0:
            self.reliability_weight = -math.log(reliability)
        else:
            self.reliability_weight = float('inf')