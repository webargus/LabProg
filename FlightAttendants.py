
def minimum(a, b):
    if a < b:
        return a
    return b

def maximum(a, b):
    if a > b:
        return a
    return b

def dijkstra(graph, v1):
    # We'll take advantage of idle main diagonal of graph matrix to save Dijkstra's distance data
    # as we explore vertices into graph
    for ix in range(n):
        graph[ix][ix] = None  # a 'None' value here means infinity
    # start by assigning 0 for the distance from start vertex
    graph[v1][v1] = 0
    # set current city to start vertex
    current = v1
    v_max_dist = 0      # variable to memoize max. distance (weight sum) to v1
    for i in range(n):
        unvisited[i] = i
    while 1:
        # check each neighbor of current city
        for neighbor in range(n):
            if neighbor == current:
                continue
            weight = graph[maximum(current, neighbor)][minimum(current, neighbor)]
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
        for x in range(n):
            if unvisited[x] is None:  # city already visited
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

# create nXn/2 static graph matrix, for we won't be appending any more vertices to it
# and we'll be using only the half below its main diagonal, since we expect a bidirectional graph input
graph = [[None for x in range(y+1)] for y in range(n)]

# Create a list filled with vertex ids, which is necessary to flag them as visited
# as we sift through graph with dijkstra algorithm;
# we're going to flag visited nodes with 'None' instead of removing
# them from list, which would be a way more costly operation in python
unvisited = [vertex for vertex in range(n)]

# fill in only lower half of matrix with edge inputs
for ix in range(m):
    u, v, w = (int(x) for x in input().split())
    temp = u
    u = maximum(u, v)
    if v == u:
        v = temp
    if (graph[u][v] is None) or (graph[u][v] > w):      # discard longest edge weight (longest distance)
        graph[u][v] = w

# print_graph(graph)        # debugging
global_min_dist = None
for v in range(n):
    v_max_dist = dijkstra(graph, v)
    if global_min_dist is None:
        global_min_dist = v_max_dist
    else:
        global_min_dist = minimum(global_min_dist, v_max_dist)
#    print_graph(graph)     #debugging

print(global_min_dist)













