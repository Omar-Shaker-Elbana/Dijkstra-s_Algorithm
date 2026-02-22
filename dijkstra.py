def Dijkstra(g, node):
    
    graph_dict = g.graph
    if node not in graph_dict.keys() or len(graph_dict.keys()) == 1:
        return {node: [0, node]}
    
    table = {}
    table[node] = [0, node]
    visited = set()
    current = node
    relation = graph_dict.get(current, [])
    path = 0
    
    while True:
        
        nxt = None
        nxt_path = float("inf")
        visited.add(current)     
        
        for i in relation:
            if (path + i[1]) < table.get(i[0], [float("inf")])[0]:
                table[i[0]] = [path + i[1], current]
        
        for x,y in table.items():
            if y[0] < nxt_path and x not in visited:
                nxt, nxt_path = x, y[0]
        
        if nxt is None:
            break
           
        current = nxt
        relation = graph_dict.get(current, [])
        path = table[current][0]
    
    unvisited = set(graph_dict.keys()) - visited
    for u in unvisited:
        table[u] = [float("inf"), None]
        
    return table
