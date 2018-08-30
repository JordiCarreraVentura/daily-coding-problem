# This problem was asked by Facebook.
# 
# A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the graph connected. For example, any binary tree is minimally-connected.
# 
# Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as either an adjacency matrix or adjacency list.


import random


def generate_graph(nodes=3, min_x=0, max_x=10, min_y=0, max_y=10):
    graph = set([])
    while len(graph) < nodes:
        x = random.randint(min_x, max_x + 1)
        y = random.randint(min_y, max_y + 1)
        node = (x, y)
        if node in graph:
            continue
        if not graph:
            graph.add(node)
            continue
        attached = False
        for _x, _y in graph:
            if abs(x - _x) <= 1 and abs(y - _y) <= 1:
                attached = True
        if attached:
            graph.add(node)
    return list(graph)



def is_minimal(graph):

    l = len(graph)
    for i in range(l - 1):
        x, y = graph[i]
        connections = [(x, y)]
        for j in range(i + 1, l):
            _x, _y = graph[j]
            
            # graph is not minimal because it contains an undirected duplicate
            # (in undirected graphs, (0, 1) == (1, 0))
            if (x, y) == (_y, _x):
                return 'undirected_duplicate', [(x, y), (_x, _y)], False

            # graph may be not minimal; we keep adding to its list of connections
            # any vertices around it; if at the end it turns out a vertex has no
            # connections, removing it would cause the graph to break so it is
            # a minimal graph
            if abs(x - _x) <= 1 and abs(y - _y) <= 1:
                connections.append((_x, _y))
        
        if len(connections) > 2:
            return 'non_minimal', connections, False
            
    return 'minimal', [], True


if __name__ == '__main__':

    # generates connected graphs where all nodes are connected
    # but not necessarily minimally connected:
    for graph in [generate_graph() for i in range(20)]:
        for node in graph:
            print node
        case, reason, minimal = is_minimal(graph)
        print 'case:', case
        print 'reason:', reason
        print 'minimal:', minimal
        print
