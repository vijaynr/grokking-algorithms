stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

states = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
final_stations = set()


def pick_stations(sts: set):
    while sts:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = sts & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        sts -= states_covered
        final_stations.add(best_station)
    print(final_stations)


pick_stations(states)
