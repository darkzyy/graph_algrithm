from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms.generators import generate
from mytranverse import tranverse

dg2 = generate(8,15,directed=True)
node_status = dict()
node_par = dict()

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

def main():
    sweep()
    print node_par
    print dg2
    tranverse(dg2)
    print dg2
    st,pre,post = depth_first_search(dg2,root=0)
    print st

if __name__ == '__main__':
    main()
