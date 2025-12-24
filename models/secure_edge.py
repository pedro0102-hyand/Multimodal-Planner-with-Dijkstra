from models.edge import Edge

class SecureEdge(Edge):
    def __init__(self, destination, transport, travel_time, price = 0.0, security_level = 10):
        super().__init__(destination, transport, travel_time, price)
        self.security_level = security_level