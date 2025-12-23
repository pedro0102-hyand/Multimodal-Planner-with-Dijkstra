class Edge:
    def __init__(
            self,
            destination,
            transport: str,
            travel_time: int,
            price: float = 0.0,
            wait_time: int = 0,
            transfer_penalty: int = 0
    ):
        self.destination = destination
        self.transport = transport
        self.travel_time = travel_time
        self.price = price
        self.wait_time = wait_time
        self.transfer_penalty = transfer_penalty
        
        # Corrigido de 'weigth' para 'weight'
        self.weight = travel_time + wait_time + transfer_penalty