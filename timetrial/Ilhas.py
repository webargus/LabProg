
import Graph


graph = Graph.Graph()

graph.extend([Graph.Node(x + 1) for x in range(4)])
graph.add_edge(graph[1], graph[0], 5)
graph.add_edge(graph[0], graph[2], 4)
graph.add_edge(graph[1], graph[2], 6)
graph.add_edge(graph[3], graph[1], 8)
graph.add_edge(graph[2], graph[3], 12)

for island in range(1, 4):

    # calculate min dist from server to island
    graph.dijkstra(graph[0], graph[island])

    min_dist = Graph.Graph.INFINITE
    max_dist = 0

    for vertex in graph:
        dist = vertex.get_data()            # read distance result
        if (dist != 0) and (dist < min_dist):
            min_dist = dist
        if (dist != Graph.Graph.INFINITE) and (dist > max_dist):
            max_dist = dist

    print(max_dist - min_dist)
















