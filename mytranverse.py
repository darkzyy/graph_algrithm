from pygraph.classes.digraph import digraph

def tranverse(dg):
    node_list = dg.nodes()
    stack = []
    for u in node_list:
        neighborslist = dg.neighbors(u)
        while neighborslist:
            stack.append((u,neighborslist[0]))
            dg.del_edge((u,neighborslist[0]))
    for edge in stack:
        a,b=edge
        dg.add_edge((b,a))

