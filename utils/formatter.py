

def format_route(result):
    print("\n🗺️ Rota detalhada:\n")
    path = result["path"]

    for i in range(len(path) - 1):
        station, _ = path[i]
        next_station, transport = path[i + 1]
        print(f"{station}")
        print(f"  └─ {transport} → {next_station}")

    # Verifica o critério para formatar a saída
    label = "Tempo Total" if result.get("criterion") == "time" else "Custo Total"
    unit = "min" if result.get("criterion") == "time" else "R$"
    
    print(f"\n⏱️ {label}: {result['total_time']} {unit}")
    print(f"🔄 Baldeações: {result['transfers']}")

