from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms.generators import generate
from mytranverse import tranverse

dg2 = generate(8,10,directed=True)
node_status = dict()
node_par = dict()
stack = []

def sweep1():
    global node_status
    global node_par
    global dg2
    node_list = dg2.nodes()
    for node in node_list:
        node_status[node] = 'white'
    for node in node_list:
        if(node_status[node] == 'white'):
            node_par[node] = 'none'
            dfs1(node)

def dfs1(vnode):
    global node_status
    global node_par
    global dg2
    global stack
    for node in dg2.neighbors(vnode):
        if(node_status[node] == 'white'):
            node_status[node] = 'grey'
            node_par[node] = vnode
            dfs1(node)
    node_status[vnode] = 'black'
    stack.append(vnode)

def sweep2():
    global node_status
    global node_par
    global dg2
    global stack
    node_list = dg2.nodes()
    for node in stack:
        node_status[node] = 'white'
    stack.reverse()
    for node in stack:
        if(node_status[node] == 'white'):
            node_par[node] = 'none'
            node_status[node] = 'grey'
            print '[',
            print node,' ',
            dfs2(node)
            print ']'

def dfs2(vnode):
    global node_status
    global dg2
    for node in dg2.neighbors(vnode):
        if(node_status[node] == 'white'):
            node_status[node] = 'grey'
            print node,' ',
            dfs2(node)
    node_status[vnode] = 'black'


def main():
    sweep1()
    print dg2
    tranverse(dg2)
    sweep2()
    print dg2

if __name__ == '__main__':
    main()
