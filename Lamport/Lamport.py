import networkx as nx
import matplotlib.pyplot as plt

class LamportClock:
    def __init__(self, nodes):
        self.nodes = nodes
        self.clock = [0] * len(nodes)

    def event(self, node):
        self.clock[node] += 1

    def send(self, sender, receiver):
        self.clock[sender] += 1
        self.clock[receiver] += 1

    def draw_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.nodes)
        pos = nx.spring_layout(G)

        labels = {}
        for i in range(len(self.nodes)):
            labels[i] = str(self.nodes[i]) + ':' + str(self.clock[i])

        nx.draw_networkx_nodes(G, pos, nodelist=self.nodes, node_color='white', node_size=1000)
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=14)
        plt.axis('off')
        plt.show()
        
        # create edges between nodes based on the order of events
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                if self.clock[i] < self.clock[j]:
                    G.add_edge(i, j)
                elif self.clock[i] > self.clock[j]:
                    G.add_edge(j, i)

        nx.draw_networkx_edges(G, pos, width=2, arrowsize=30)
        plt.show()



# create a LamportClock object with 4 nodes
clock = LamportClock([0, 1, 2, 3])

# simulate some events and message passing between nodes
clock.event(0)
clock.send(0, 1)
clock.send(1, 2)
clock.event(0)
clock.send(2, 3)
clock.event(1)

# draw the causal ordering graph
clock.draw_graph()
