# how to visualize a weighted graph?
# how about a hash map of hash maps
graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "finish": 1
    },
    "b": {
        "a": 3,
        "finish": 5
    },
    "finish": {}
}

INF = float("inf")

processed = []


def find_fastest_path(graph, start_node, end_node):
    costs = populate_costs(graph, start_node=start_node)
    parents = populate_parents(graph, start_node=start_node)
    print(costs)
    print(parents)

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors: dict = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    print(costs)
    print(parents)

    fastest_path = [end_node]
    next_node = fastest_path[0]

    while True:
        next_node = parents[next_node]
        fastest_path.append(next_node)
        if next_node == start_node:
            break

    fastest_path.reverse()
    print(fastest_path)


def find_lowest_cost_node(costs):
    lowest_cost = INF
    lowest_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def populate_costs(graph, start_node):
    costs = {}
    for node in graph.keys():
        if start_node != node:
            if graph[start_node].keys().__contains__(node):
                costs[node] = graph[start_node][node]
            else:
                costs[node] = INF
    return costs


def populate_parents(graph, start_node):
    parents = {}
    for node in graph.keys():
        if start_node != node:
            val: dict = graph[start_node]
            if val.__contains__(node):
                parents[node] = start_node
            else:
                parents[node] = None
    return parents


find_fastest_path(graph, "finish", "start")
