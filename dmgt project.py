import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_node("node 1")

G.add_nodes_from(["node 2", "node 3"])
G.add_nodes_from([("node 4", {"abc": 123}), ("node 5", {"abc": 0})])

print(G.nodes)
print(G.nodes["node 4"]["abc"]) 

G.add_edge("node 1", "node 2")
G.add_edge("node 1", "node 6")

G.add_edges_from([("node 1", "node 3"), 
                  ("node 3", "node 4")])

G.add_edges_from([("node 1", "node 5", {"weight" : 5}), 
                  ("node 2", "node 4", {"weight" : 5})])
G.add_edges_from([("node 1", "node 6", {"weight" : 4}), 
                  ("node 5", "node 4", {"weight" : 5})])

print(G.nodes)
print(G.edges)

print(G["node 1"])
print(G["node 1"]["node 5"])

print(G["node 2"])
print(G["node 2"]["node 4"])

nx.draw(G)
plt.show()