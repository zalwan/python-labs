import networkx as nx
import matplotlib.pyplot as plt

# Buat/inisiasi graph
G = nx.Graph()

# Tambahkan edges dengan bobot
edges = [
    ("A", "C", 2),
    ("A", "B", 4),
    ("C", "B", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("E", "F", 3),
    ("D", "F", 6),
]

G.add_weighted_edges_from(edges)

# Definisikan node awal dan akhir
start_node = "A"
end_node = "F"

# Jalankan algoritma Dijkstra
shortest_path = nx.dijkstra_path(G, start_node, end_node)
shortest_distance = nx.dijkstra_path_length(G, start_node, end_node)

print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)

# Visualisasi graf
# pos = nx.spring_layout(G, seed=42)

# Visualisasi Posisi node manual biar mirip kayak di soal
pos = {
    "A": (4, 4),
    "B": (3, 2),
    "C": (2, 3),
    "D": (2, 1),
    "E": (1, 2),
    "F": (1, 0),
}

# Warna node
node_colors = []
for node in G.nodes():
    if node == "A":
        node_colors.append("green")
    elif node == "F":
        node_colors.append("orange")
    else:
        node_colors.append("red")

# Gambar node dan edges
# nx.draw(
#     G,
#     pos,
#     with_labels=True,
#     node_color="lightblue",
#     node_size=2000,
#     font_size=12,
#     font_weight="bold",
# )

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=12,
    font_weight="bold"
)


# Gambar bobot edges
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Sorot jalur terpendek
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=path_edges,
    edge_color="red",
    width=3,
)

plt.title("Visualisasi Graf dan Jalur Terpendek (Dijkstra)")
plt.show()
