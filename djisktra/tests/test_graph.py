import unittest
from djisktra import Graph

class TestGraph(unittest.TestCase):

    def test_graphy(self):
        G = Graph()
        G.add_edge(1, 2, 3)
        G.add_edge(1, 3, 2)
        self.assertAlmostEqual(G.get_edge_weight(1,2), 3, 'Should be 3')

if __name__ == '__main__':
    unittest.main()