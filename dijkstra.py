def Dijkstra(graph, node):
    graph_dict = graph.graph
    
    result = {node: [0, None],}
    visited = set()
    current = node
    neighbors = graph_dict.get(current, [])
    distance = 0
    
    while True:
        
        nxt = None
        visited.add(current)     
        
        for i in neighbors:
            if (distance + i[1]) < result.get(i[0], [float("inf")])[0]:
                result[i[0]] = [distance + i[1], current]
        
        nxt_distance = float("inf")
        for x,y in result.items():
            if y[0] < nxt_distance and x not in visited:
                nxt, nxt_distance = x, y[0]
        
        if nxt is None:
            break

        current = nxt
        neighbors = graph_dict.get(current, [])
        distance = result[current][0]
    
    unvisited = set(graph_dict.keys()) - visited
    for u in unvisited:
        result[u] = [float("inf"), None]
        
    return result

def get_path(routes, node):
    if routes[node][0] == float("inf"):
        return None  # No path exists

    path = []
    distance = routes[node][0]
    current = node
    
    while current is not None:
        path.append(current)
        current = routes[current][1]
    
    return {"path": path[::-1], "distance": distance}