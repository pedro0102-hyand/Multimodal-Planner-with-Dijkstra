from data.network import build_network
from services.planner import plan_trip
from utils.formatter import format_route

def main():

    graph, start, end = build_network()
    result = plan_trip(graph, start, end)
    format_route(result)

if __name__ == "__main__":
    main()