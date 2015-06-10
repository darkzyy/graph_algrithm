
def ufs_init(w,par):
    for key in w:
        w[key] = 1
    for key in par:
        par[key] = None

def find(key,par):
    tmp = key
    while par[tmp]!=None:
        tmp = par[tmp]
    if par[key] != None:
        par[key] = tmp
    return tmp

def union(k1,k2,w,par):
    if w[find(k1,par)] < w[find(k2,par)] :
        par[find(k1,par)] = find(k2,par)
    else:
        par[find(k2,par)] = find(k1,par)

def main():
    w = dict()
    par = dict()
    for i in range(0,10):
        w[i]=i
        par[i]=i
    ufs_init(w,par)
    union(0,1,w,par)
    union(0,2,w,par)
    union(1,3,w,par)
    union(2,4,w,par)
    union(5,6,w,par)
    union(6,7,w,par)
    union(5,8,w,par)
    union(5,9,w,par)
    for i in range(0,10):
        print par[i]

if __name__ == '__main__':
    main()
