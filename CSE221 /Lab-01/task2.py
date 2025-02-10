inp = open("input2.txt",'r')
out = open("output2.txt", "w")
f = inp.readlines()

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]:
                    self.rank[root_v] += 1

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst_edges = []
    total_cost = 0

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_edges.append((u, v, w))
            total_cost += w
            if len(mst_edges) == n - 1:
                break

    return mst_edges, total_cost


N, M = map(int, f[0].split())
edges = []
f = f[1:]

for _ in range(M):
    u, v, w = map(int, f[_].split())
    edges.append((u, v, w))

mst_edges, mst_cost = kruskal_mst(edges, N)
remaining_cost = 0

for u, v, w in edges:
    if (u, v, w) not in mst_edges and (v, u, w) not in mst_edges:
        remaining_cost += w

out.writelines(f"{min(mst_cost, remaining_cost)}")

inp.close()
out.close()