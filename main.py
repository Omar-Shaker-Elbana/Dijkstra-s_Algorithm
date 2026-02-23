from dijkstra import Dijkstra, get_path
from testing import build_tricky_graph

if __name__ == "__main__":
    graph = build_tricky_graph()
    start_node = 'A'
    routes = Dijkstra(graph, start_node)
    
    for node in sorted(routes.keys()):
        result = get_path(routes, node)
        if result is not None:
            print(f"Shortest path from {start_node} to {node}: {' -> '.join(result['path'])} (Distance: {result['distance']})")
        else:
            print(f"No path from {start_node} to {node}.")