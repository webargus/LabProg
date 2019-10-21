
def minimum(a, b):
    if a < b:
        return a
    return b

def maximum(a, b):
    if a > b:
        return a
    return b

def dijkstra(graph, v1):
    n = len(graph)
    # We'll take advantage of unused main diagonal of graph matrix to save Dijkstra's distance data
    # as we explore vertices into graph
    for ix in range(n):
        graph[ix][ix] = None  # a 'None' value here means infinity in our algorithm version
    # start by assigning 0 for the distance from start vertex
    graph[v1][v1] = 0
    # set current city to start vertex
    current = v1
    v_max_dist = 0      # variable to memoize max. distance (weight sum) to v1
    # Create a list filled with vertex ids, which is necessary to flag vertices as visited
    # as we sift through graph with dijkstra algorithm;
    # we're going to flag visited nodes with 'None' instead of removing
    # them from list, which is a way more costly operation in python
    unvisited = [vertex for vertex in range(n)]
    while 1:
        # check each neighbor of current city
        for neighbor in range(n):
            if neighbor == current:
                continue
            weight = graph[current][neighbor]
            if weight is None:
                continue
            # update neighbor's distance from origin with the shortest distance to it so far
            # notice that None here stands for infinity
            dist_from_current = graph[current][current] + weight
            if (graph[neighbor][neighbor] is None) or (dist_from_current < graph[neighbor][neighbor]):
                graph[neighbor][neighbor] = dist_from_current
        # update max distance to start vertex (v1)
        v_max_dist = maximum(v_max_dist, graph[current][current])
        # mark current node as visited (None) in unvisited list, for we won't visit it again
        unvisited[current] = None
        # before we loop back, take the next unvisited city with the shortest distance
        # so far from previous vertex, for our current city
        # break out if the shortest distance results infinite, which means that the city is unreachable
        shortest = None
        for x in unvisited:
            if x is None:  # city already visited
                continue
            if graph[x][x] is None:  # infinite distance
                continue
            if (shortest is None) or (shortest > graph[x][x]):
                shortest = graph[x][x]
                current = x
        if shortest is None:
            break
    return v_max_dist


"""def print_graph(graph):
    for row in graph:
        print("".join(["{:<10s}".format(str(x)) for x in row]))
    print(30*"-")
"""

n, m = (int(x) for x in input().split())

# create nXn static graph matrix, for we won't be appending any more vertices to it
graph = [[None for x in range(n)] for y in range(n)]

for ix in range(m):
    u, v, w = (int(x) for x in input().split())
    if (graph[u][v] is None) or (graph[u][v] > w):
        graph[u][v] = graph[v][u] = w

# print_graph(graph)
global_min_dist = None
for v in range(n):
    v_max_dist = dijkstra(graph, v)
    if global_min_dist is None:
        global_min_dist = v_max_dist
    else:
        global_min_dist = minimum(global_min_dist, v_max_dist)
#    print_graph(graph)

print(global_min_dist)



"""let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
2 for each edge (u,v)
3    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
4 for each vertex v
5    dist[v][v] ← 0
6 for k from 1 to |V|
7    for i from 1 to |V|
8       for j from 1 to |V|
9          if dist[i][j] > dist[i][k] + dist[k][j] 
10             dist[i][j] ← dist[i][k] + dist[k][j]
11         end if"""











