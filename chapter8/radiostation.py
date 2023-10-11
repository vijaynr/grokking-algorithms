stations = {
    "kone": set(["id","nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
final_stations = set()


def pick_stations(states: set):
    while states:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states -= states_covered
        final_stations.add(best_station)
    print(final_stations)


pick_stations(states)
