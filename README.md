# 🚇 Sistema Inteligente de Planejamento de Rotas de Transporte

Sistema avançado de planejamento de rotas que utiliza o algoritmo de Dijkstra para encontrar os melhores caminhos em redes de transporte, considerando múltiplos critérios como tempo, preço, confiabilidade e segurança.

## 📋 Descrição

Este projeto implementa um planejador de rotas multimodal que permite aos usuários encontrar o melhor caminho entre dois pontos considerando diferentes fatores:

- **Tempo de viagem**: Rota mais rápida
- **Custo**: Rota mais econômica
- **Confiabilidade**: Rota com maior probabilidade de pontualidade
- **Segurança**: Rotas que passam apenas por áreas seguras
- **Transferências**: Minimiza trocas de transporte

## 🎯 Funcionalidades

### Múltiplos Critérios de Otimização

- **Otimização por tempo**: Considera tempo de viagem, tempo de espera e penalidades de transferência
- **Otimização por preço**: Encontra a rota mais econômica
- **Otimização por confiabilidade**: Usa pesos logarítmicos para maximizar a probabilidade de pontualidade
- **Otimização por transferências**: Penaliza mudanças de modal de transporte
- **Filtragem por segurança**: Permite definir nível mínimo de segurança para as rotas

### Precificação Dinâmica

O sistema suporta ajustes dinâmicos de preço para simular cenários reais de alta demanda (ex: Uber em horários de pico).

### Diferentes Modelos de Rede

O projeto inclui quatro cenários de exemplo:

1. **Rede Básica** (`network.py`): Múltiplos modais (metrô, ônibus, trem)
2. **Rede Dinâmica** (`network_dynamic.py`): Transporte com preços variáveis
3. **Rede Confiável** (`network_reliable.py`): Rotas com diferentes níveis de pontualidade
4. **Rede Segura** (`network_safe.py`): Rotas com classificação de segurança

## 🏗️ Estrutura do Projeto

```
.
├── algorithms/
│   └── dijkstra.py              # Implementação do algoritmo de Dijkstra
├── data/
│   ├── network.py               # Rede básica de transporte
│   ├── network_dynamic.py       # Rede com precificação dinâmica
│   ├── network_reliable.py      # Rede com confiabilidade
│   └── network_safe.py          # Rede com níveis de segurança
├── models/
│   ├── edge.py                  # Classe base para arestas
│   ├── reliable_edge.py         # Aresta com confiabilidade
│   ├── secure_edge.py           # Aresta com nível de segurança
│   └── station.py               # Classe representando estações
├── services/
│   ├── planner.py               # Serviço de planejamento de rotas
│   ├── price_manager.py         # Gerenciamento de preços dinâmicos
│   └── safe_planner.py          # Filtragem por segurança
├── utils/
│   └── formatter.py             # Formatação de saída
└── main.py                      # Ponto de entrada da aplicação
```

## 🚀 Como Usar

### Requisitos

- Python 3.7+
- Biblioteca padrão (heapq, math, random)

### Execução Básica

```bash
python main.py
```

### Exemplo de Uso - Rede Confiável

```python
from data.network_reliable import build_reliable_network
from services.planner import plan_trip
from utils.formatter import format_route

# Construir a rede
graph, start, end = build_reliable_network()

# Planejar rota mais rápida
result = plan_trip(graph, start, end, criterion="time")
format_route(result)

# Planejar rota mais confiável
for edges in graph.values():
    for edge in edges:
        edge.weight = edge.reliability_weight
        
result = plan_trip(graph, start, end, criterion="reliability")
format_route(result)
```

### Exemplo de Uso - Precificação Dinâmica

```python
from data.network_dynamic import build_dynamic_network
from services.price_manager import apply_dynamic_pricing
from services.planner import plan_trip

graph, start, end = build_dynamic_network()

# Aplicar aumento de preço no Uber (simulando horário de pico)
multiplier = apply_dynamic_pricing(graph, transport_type="Uber", multiplier=2.0)
print(f"Preços do Uber aumentaram {multiplier}x")

# Planejar rota considerando os novos preços
result = plan_trip(graph, start, end, criterion="price")
```

### Exemplo de Uso - Rotas Seguras

```python
from data.network_safe import build_safe_network
from services.safe_planner import filter_secure_graph
from services.planner import plan_trip

graph, start, end = build_safe_network()

# Filtrar apenas rotas com segurança >= 7
safe_graph = filter_secure_graph(graph, min_security=7)

result = plan_trip(safe_graph, start, end, criterion="time")
```

## 🧮 Algoritmo

### Dijkstra com Critérios Múltiplos

O algoritmo de Dijkstra foi adaptado para suportar diferentes funções de custo:

```python
# Tempo (padrão)
cost = edge.weight  # travel_time + wait_time + transfer_penalty

# Preço
cost = edge.price

# Confiabilidade
cost = -log(reliability)  # Peso logarítmico

# Transferências
cost = 1 if mudou_transporte else 0.1
```

### Cálculo de Confiabilidade

Para rotas confiáveis, usamos pesos logarítmicos que permitem calcular a probabilidade total do caminho:

```
Peso = -ln(confiabilidade)
Probabilidade_Total = e^(-soma_dos_pesos)
```

Exemplo: Uma rota com confiabilidade 99% em cada trecho terá maior probabilidade total que uma rota com 70% de confiabilidade.

## 📊 Modelos de Dados

### Station (Estação)

```python
Station("Nome da Estação")
```

### Edge (Aresta Básica)

```python
Edge(
    destination=station_b,
    transport="Metrô",
    travel_time=10,
    price=5.0,
    wait_time=2,
    transfer_penalty=4
)
```

### ReliableEdge (Aresta Confiável)

```python
ReliableEdge(
    destination=station_b,
    transport="Trem",
    travel_time=25,
    reliability=0.99  # 99% de chance de pontualidade
)
```

### SecureEdge (Aresta Segura)

```python
SecureEdge(
    destination=station_b,
    transport="Caminhada",
    travel_time=15,
    security_level=9  # Escala de 1-10
)
```

## 💡 Casos de Uso

1. **Planejamento de Viagem Urbana**: Encontre a rota mais rápida ou barata usando transporte público
2. **Logística e Entregas**: Otimize rotas considerando múltiplos fatores
3. **Aplicativos de Mobilidade**: Compare opções de transporte (ônibus vs. Uber)
4. **Sistemas de Navegação**: Rotas que evitam áreas perigosas
5. **Análise de Confiabilidade**: Escolha rotas com maior chance de pontualidade

## 🔧 Extensões Possíveis

- Adicionar suporte para horários específicos (time-dependent routing)
- Implementar A* para melhor performance em grafos grandes
- Adicionar interface gráfica ou API REST
- Integrar com dados reais de transporte público
- Suporte para múltiplos destinos (problema do caixeiro viajante)
- Adicionar restrições de acessibilidade
- Implementar algoritmos de roteamento multiobjetivo

## 📝 Notas Técnicas

- O algoritmo usa uma fila de prioridade (heap) para eficiência O((E + V) log V)
- Suporta grafos direcionados e ponderados
- Lida corretamente com ciclos e múltiplas arestas entre nós
- A classe Station implementa `__lt__` para compatibilidade com heapq

## 🤝 Contribuindo

Contribuições são bem-vindas! Áreas de interesse:

- Novos critérios de otimização
- Algoritmos alternativos (A*, Bellman-Ford)
- Visualização de rotas
- Casos de teste
- Documentação

## 📄 Licença

Este projeto é open source e está disponível para uso educacional e comercial.

---

**Desenvolvido com Python 🐍 | Algoritmos de Grafos 📊 | Otimização de Rotas 🗺️**