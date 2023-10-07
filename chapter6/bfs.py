from collections import deque


def is_connected(graph: dict, start, end):
    checked = []
    q = deque()
    if not graph.keys().__contains__(start):
        return False
    q.append(start)
    while len(q) != 0:
        item = q.popleft()
        if checked.__contains__(item):
            continue
        if item == end:
            return True
        checked.append(item)
        q += graph[item]
    return False


graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}

print(is_connected(graph, "alice", "you"))
