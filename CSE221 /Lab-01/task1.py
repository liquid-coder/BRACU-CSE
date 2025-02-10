
inp = open("input1.txt",'r')
out = open("output1.txt", "w")
f = inp.readlines()

def find_parent(node, parent):
    if parent[node] == node:
        return node
    parent[node] = find_parent(parent[node], parent)
    return parent[node]

def union_sets(node1, node2, parent, size):
    root1 = find_parent(node1, parent)
    root2 = find_parent(node2, parent)

    if root1 != root2:
        if size[root1] < size[root2]:
            root1, root2 = root2, root1
        parent[root2] = root1
        size[root1] += size[root2]


N, K = map(int, f[0].split())
f = f[1:]
parent = [i for i in range(N+1)]
size = [1] * (N+1)

for _ in range(K):
    Ai, Bi = map(int, f[_].split())
    union_sets(Ai, Bi, parent, size)
    out.writelines(f"{size[find_parent(Ai, parent)]}\n") 
    
inp.close() 
out.close() 
