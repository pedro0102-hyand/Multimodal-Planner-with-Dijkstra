class Station:
    def __init__(self, name: str):
        self.name = name
    
    # Permite comparação entre objetos Station (necessário para o heapq)
    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return f"Station ({self.name})"
