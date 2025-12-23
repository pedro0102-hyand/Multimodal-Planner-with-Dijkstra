def format_route(result):
    print("\n🗺️ Rota detalhada:\n")

    path = result["path"]

    for i in range(len(path) - 1):
        station, _ = path[i]
        next_station, transport = path[i + 1]

        print(f"{station}")
        print(f"  └─ {transport} → {next_station}")

    print("\n⏱️ Tempo total:", result["total_time"], "min")
    print("🔄 Baldeações:", result["transfers"])

