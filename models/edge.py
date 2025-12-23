class Edge:
    def __init__(
            self,
            destination,
            transport: str,
            travel_time: int,
            wait_time: int = 0,
            transfer_penalty: int = 0
    ):
        self.destination = destination
        self.transport = transport
        self.weigth = travel_time + wait_time + transfer_penalty