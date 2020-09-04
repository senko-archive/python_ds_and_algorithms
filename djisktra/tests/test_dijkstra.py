import unittest
from djisktra import DijkstraSPF, Graph
from djisktra.dijkstra import AbstractDijkstraSPF

class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        nodes = ("S", "T", "A", "B", "C", "D", "E", "F", "G")
        S, T, A, B, C, D, E, F, G = nodes

        graph = Graph()
        graph.add_edge(S, A, 4)
        graph.add_edge(S, B, 3)
        graph.add_edge(S, D, 7)
        graph.add_edge(A, C, 1)
        graph.add_edge(B, S, 3)
        graph.add_edge(B, D, 4)
        graph.add_edge(C, E, 1)
        graph.add_edge(C, D, 3)
        graph.add_edge(D, E, 1)
        graph.add_edge(D, T, 3)
        graph.add_edge(D, F, 5)
        graph.add_edge(E, G, 2)
        graph.add_edge(G, E, 2)
        graph.add_edge(G, T, 3)
        graph.add_edge(T, F, 5)

        dijkstra = DijkstraSPF(graph, S)

        for v in nodes:
            print("%3s %3s" % (v, dijkstra.get_distance(v)))

        self.assertEqual(dijkstra.get_distance(T), 10, 'should be 10')
        self.assertEqual(dijkstra.get_path(T), ["S", "D", "T"], 'should be S->D->T')