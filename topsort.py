from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms.generators import generate
from pygraph.algorithms.cycles import find_cycle
from mytranverse import tranverse

dg2 = generate(8,10,directed=True)
node_status = dict()
node_par = dict()
toporder = []

def sweep():
    global node_status
    global node_par
    global dg2
    node_list = dg2.nodes()
    for node in node_list:
        node_status[node] = 'white'
    for node in node_list:
        if(node_status[node] == 'white'):
            node_par[node] = 'none'
            dfs(node)

def dfs(vnode):
    global node_status
    global node_par
    global dg2
    for node in dg2.neighbors(vnode):
        if(node_status[node] == 'white'):
            node_status[node] = 'grey'
            node_par[node] = vnode
            dfs(node)
    node_status[vnode] = 'black'
    toporder.insert(0,vnode)

def main():
    global dg2
    while find_cycle(dg2):
        dg2 = generate(8,10,directed=True)
    sweep()
    print dg2
    print toporder

if __name__ == '__main__':
    main()
