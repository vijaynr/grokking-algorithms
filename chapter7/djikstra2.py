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

infinity = float("inf")
n = len(graph)
visited = set()
costs = {}
parents = {}


def init(start_node):
    visited.add(start_node)
    for node in graph.keys():
        costs[node] = infinity
        parents[node] = None


def find_path(start_node):
    init(start_node)
    node = start_node
    while node is not None:
        cost = costs[node]
        for neighbor in graph[node].keys():
            new_cost = (cost if cost != infinity else 0) + graph[node][neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        visited.add(node)
        node = find_low_cost_node()
    print(costs)
    print(parents)


def find_low_cost_node():
    low_cost = infinity
    low_cost_node = None
    for node in costs.keys():
        cost = costs[node]
        if low_cost > cost and not visited.__contains__(node):
            low_cost = cost
            low_cost_node = node
    return low_cost_node


find_path("start")