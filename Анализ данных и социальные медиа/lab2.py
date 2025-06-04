import networkx as nx

G = nx.path_graph(30)

for i in range(12, 19):
    for j in range(i + 1, 19):
        G.add_edge(i, j)

G.add_edge(0, 2)
G.add_edge(27, 29)

centrality = nx.eigenvector_centrality_numpy(G)

for n in centrality:
    print("c(", n, ")=", centrality[n])
