          python3.8 -m pip install networkx
        import matplotlib.pyplot as plt
        import networkx as nx

        G = nx.Graph()
        G.add_node(1)
G.add_node(2)
G.add_nodes_from([3, 4, 5, 6])
G.add_edge(1, 2)  # edge from 1 to 2
G.add_edges_from([(2, 3), (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)])
print(G.nodes)
print(G.edges)
# [1, 2, 3, 4, 5, 6]
# [(1, 2), (2, 3), (3, 4), (3, 5), (3, 6), (4, 5), (5, 6)]
G = nx.Graph()

G.add_nodes_from(range(1, 7))
G.add_edges_from([
    (1, 2), (2, 3), (3, 4), (3, 5), 
    (3, 6), (4, 5), (5, 6)
])
fig, ax = plt.subplots()
layout = nx.shell_layout(G)
nx.draw(G, ax=ax, pos=layout, with_labels=True)
ax.set_title("Simple network drawing")