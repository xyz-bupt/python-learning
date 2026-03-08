#查找x所属集合（对应的树的树根）
def find(x):
    if fa[x] == x:  return x
    return find(fa[x])

"""
def find(x):
    return x if fa[x] == x else find(fa[x])
"""

#v所在集合合并到u所在集合中国
def union(u,v):
    if find(u) != find(v):
        fa[find(v)] = find(u)

#路径压缩
def find(x):
    if fa[x] == x: return x
    fa[x] = find(fa[x])
    return fa[x]



#并查集递归模版
fa = list(range(n+1))
def find(x):
    if fa[x] == x: return x
    fa[x] = find(fa[x])
    return fa[x]
def union(u,v):
    if find(u) != find(v):
        fa[find(v)] = find(u)

