import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    amount = range(20)

    G = nx.Graph()
    G.add_nodes_from(amount)

    for x in amount:
        for y in amount:
            G.add_edges_from([(x, y)])

    nx.draw_circular(G, node_color='y', edge_color='#909090', node_size=500)

    plt.axis('equal')
    plt.show()