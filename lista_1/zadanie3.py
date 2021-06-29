import networkx as nx
import matplotlib.pyplot as plt



G = nx.Graph()


pos = nx.spring_layout(G)
# nx.draw_networkx_labels(G, pos)
#nx.circular_ladder_graph(n, create_using=None)
nx.draw_circular(G)
plt.axis('equal')
plt.show()


