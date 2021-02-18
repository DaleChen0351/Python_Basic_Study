




graph = {
"L" : ["i","k"],
'i' : ["e", "Y", "L"],
"k" : ["o", "u", "L"],
"e" : ["i"],
"Y" : ["i"],
"o" : ["k"],
"u" : ["k"]
}


def bfs(graph, s):
    printout = ""
    queue = []
    seen = set()
    queue.append(s)
    seen.add(s)
    parent={}
    parent[s] = None
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)  #
                parent[node] = vertex
        #print(vertex)

    return parent


par = bfs(graph, "L")

v = "Y"

while v is not None:
    print(v)
    v = par[v]
