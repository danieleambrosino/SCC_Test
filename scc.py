from graphs import WHITE, GREY, BLACK

time = 0
nodes_sorted_by_end_time = []


def dfs_visit(node):
    global time, nodes_sorted_by_end_time
    time += 1
    node.discover_time = time
    node.colour = GREY
    for son in node.sons:
        if son.colour == WHITE:
            son.parent = node
            dfs_visit(son)
    node.colour = BLACK
    time += 1
    node.end_time = time
    nodes_sorted_by_end_time.append(node)


def depth_first_search(graph):
    nodes = graph.nodes
    for node in nodes:
        if node.colour == WHITE:
            dfs_visit(node)


def strongly_connected_components(graph):
    depth_first_search(graph)
    graph.transpose()

    nodes = graph.nodes
    scc_list = []

    def visit(node):
        scc = []

        def _visit(nod):
            nod.colour = GREY
            for son in nod.sons:
                if son.colour == WHITE:
                    son.parent = nod
                    _visit(son)
            nod.colour = BLACK
            scc.append(nod)

        _visit(node)
        return scc

    global nodes_sorted_by_end_time
    for node in nodes:
        node.colour = WHITE

    for node in reversed(nodes_sorted_by_end_time):
        if node.colour == WHITE:
            scc_list.append(visit(node))

    return scc_list
