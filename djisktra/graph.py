from io import StringIO

class Graph:
    def __init__(self, adjacency_list=dict(), edge_weights=dict()):
        self.__adjacency_list = adjacency_list.copy()
        self.__edge_weights = edge_weights.copy()
        self.__all_nodes = set()
        if bool(self.__edge_weights) is True:
            self.add_elements(self, self.__edge_weights)

    def add_elements(self, edge_dict):
        self.__all_nodes.update(edge_dict.keys())

    def add_edge(self, start, end, weight):
        self.__edge_weights[start, end] = weight
        if start not in self.__adjacency_list:
            self.__adjacency_list[start] = set()
        self.__adjacency_list[start].add(end)
        self.__all_nodes.update([start, end])

    def get_edge_weight(self, start, end):
        return self.__edge_weights[start, end]

    def get_adjacent_nodes(self, start):
        return self.__adjacency_list.get(start, set())

    def get_nodes(self):
        """ Return all nodes in this graph. """
        return self.__adjacency_list.keys()

    def get_number_of_nodes(self):
        return len(self.__all_nodes)

    def __str__(self):
        io = StringIO()
        N = self.get_number_of_nodes()
        print("Directed, acyclic graph with %d nodes" % N, file=io)
        for u in self.get_nodes():
            adj = self.get_adjacent_nodes(u)
            print("Node %s: connected to %d nodes" % (u, len(adj)), file=io)
        return io.getvalue()

    def print(self):
        print(self.__adjacency_list)
        print(self.__edge_weights)