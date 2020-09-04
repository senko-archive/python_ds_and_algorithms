import math


class AbstractDijkstraSPF():
    def __init__(self, graph, start):
        self.__dist = dist = dict()
        self.__prev = prev = dict()
        visited = set()
        queue = set()

        dist[start] = 0
        prev[start] = start
        queue.add(start)

        while queue:
            u = min(queue, key=dist.get)
            for v in self.get_adjacent_nodes(graph, u):
                if v in visited:
                    continue
                alt = self.get_distance(u) + self.get_edge_weight(graph, u, v)
                if alt < self.get_distance(v):
                    dist[v] = alt
                    prev[v] = u
                    queue.add(v)
            queue.remove(u)
            visited.add(u)

    def get_distance(self, u):
        """ Return the length of shortest path from s to u. """
        return self.__dist.get(u, math.inf)

    def get_path(self, v):
        """ Return the shortest path to v. """
        path = [v]
        while self.__prev[v] != v:
            v = self.__prev[v]
            path.append(v)
        return path[::-1]


    @staticmethod
    def get_adjacent_nodes(graph, u):
        raise NotImplementedError

    @staticmethod
    def get_edge_weight(graph, u, v):
        raise NotImplementedError


class DijkstraSPF(AbstractDijkstraSPF):

    @staticmethod
    def get_adjacent_nodes(graph, u):
        return graph.get_adjacent_nodes(u)

    @staticmethod
    def get_edge_weight(graph, u, v):
        return graph.get_edge_weight(u, v)