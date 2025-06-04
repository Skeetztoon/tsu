import networkx as nx

n = 70
p = 0.45

G = nx.erdos_renyi_graph(n,p)
a = 0
for n in G.nodes():
    a = a + G.degree(n)
print(float(a) / len(G.nodes())) # средняя степень вершины
print((n-1)*p) # средняя степень вершины по формуле