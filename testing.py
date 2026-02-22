from graph import Graph

def build_tricky_graph():
    g = Graph()
    # Unique vertex labels
    for v in list("ABCDEFGHIJKLMN") + ["X", "Y", "Z"]:
        g.add_vertex(v)

    # ---- Core structure with "gotchas" ----
    # A has two main ways toward D: one short-in-weight (via C), one short-in-hops (via B) but heavier.
    g.add_edge('A','B',7)
    g.add_edge('A','C',2)
    g.add_edge('C','D',2)
    g.add_edge('B','D',10)

    # Connect D into a big cycle E–F–G–H–I–J–E (with traps and chords)
    g.add_edge('D','E',1)

    # Trap: E–F is huge; looks close on the drawing but costs a lot
    g.add_edge('E','F',50)

    # Better entry to the cycle from C
    g.add_edge('C','F',5)

    # Zero-weight edge: Dijkstra must handle 0 just fine
    g.add_edge('F','G',0)

    # Continue the cycle with moderate weights
    g.add_edge('G','H',3)
    g.add_edge('H','I',1)
    g.add_edge('I','J',1)
    g.add_edge('J','E',1)

    # Cheap long ladder: B–K–L–M–D (many edges, tiny weights)
    g.add_edge('B','K',1)
    g.add_edge('K','L',1)
    g.add_edge('L','M',1)
    g.add_edge('M','D',1)

    # Chords/shortcuts across the cycle to create alternate routes
    g.add_edge('D','J',2)      # chord inside the cycle
    g.add_edge('E','N',2)      # side branch out of the cycle
    g.add_edge('N','G',2)      # reconnects near G (forms another loop)

    # Tempting but suboptimal hop
    g.add_edge('C','K',8)

    # “Looks like a shortcut” but usually worse than going around
    g.add_edge('A','H',20)

    # Alternative routes interconnecting ladder and cycle
    g.add_edge('G','M',6)
    g.add_edge('L','H',9)

    # Disconnected island to test unreachable handling
    g.add_edge('X','Y',4)
    g.add_edge('Y','Z',5)

    return g

# Quick peek (optional)
if __name__ == "__main__":
    g = build_tricky_graph()
    # print("Vertices:", g.amount)            # 17
    # print("Neighbors of C:", graph_dict['C'])  # should show [['A',2], ['D',2], ['F',5], ['K',8]] in some order
    # print("Neighbors of X:", graph_dict['X'])  # [['Y',4]]
