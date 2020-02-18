import matplotlib.pyplot as plt
import networkx as nx
G = nx.read_gexf('vk-friends-51253754.gexf')
pos = nx.spring_layout(G,k=0.15,iterations=20)

# nx.draw(G, with_labels=False)

nx.draw(G, pos, node_size = 2, node_color = 'red')

plt.show()