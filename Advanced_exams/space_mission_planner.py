def check_mission_feasibility(max_crew: int, budget: float, *missions): # each mission look like (name, crew size, budget)
    total_budget = budget
    confirmed = []
    suspended = []
    result = ""
    for mission in missions:
        mission_crew = mission[1]
        mission_budget = mission[2]
        if mission_crew <= max_crew and mission_budget <= total_budget:
            confirmed.append(mission)
            total_budget -= mission_budget
        else:
            suspended.append(mission)
    if len(confirmed) == len(missions):
        result += "All missions are feasible within crew and budget limits.\n"
    if confirmed:
        result += "Confirmed Missions:\n"
        sorted_c = sorted(confirmed, key=lambda x: x[0])
        for m in sorted_c:
            result += f"${m[0]}, crew size: {m[1]}, budget: {m[2]:.2f}\n"
    if suspended:
        result += "Suspended Missions:\n"
        sorted_s = sorted(suspended, key=lambda x: (-x[1], -x[2]))
        for m in sorted_s:
            result += f"!{m[0]}, crew size: {m[1]}, budget: {m[2]:.2f}\n"
    return result.strip()




# print(check_mission_feasibility(
#     5, 100_000_000.0,
#     ("Apollo 11", 3, 10_000_000.0),
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 8_000_000.0)
# ))

# print(check_mission_feasibility(
#     3, 9_000_000.0,
#     ("Apollo 11", 3, 9_000_000.1),
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 3_000_000.0),
#     ("Lunar 5", 3, 9_000_001.0)
# ))

# print(check_mission_feasibility(
#     4, 9_000_000.0,
#     ("Apollo 11", 5, 2_000_000.1),
#     ("Voyager 1", 5, 1_000_000.0),
#     ("Hubble 2", 4, 9_000_000.01),
#     ("Lunar 5", 8, 500_000.0)
# ))

# print(check_mission_feasibility(
#     3, 20_000_000.0,
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 3_000_000.0),
#     ("Lunar 4", 3, 6_000_001.0),
#     ("Apollo 11", 3, 9_000_000.1),
#     ("Hubble 3", 4, 2_000_000.0),
#     ("Lunar 5", 3, 4_000_001.0)
# ))



