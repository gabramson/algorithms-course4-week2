""" Contains class TSPFinder """
import itertools
import math

class TSPFinder:
    """ find shortest tour in small graphs """
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.distance = [[float("inf")] * num_edges for i in range(num_edges)]

    def add_edge(self, start, end, distance):
        """ adds an edge to the graph """
        self.distance[start-1][end-1] = distance
        self.distance[end-1][start-1] = distance

    def get_shortest_tour(self):
        """ computes the shortest tour """
        shortest_path = [[float("inf")] * self.num_edges for i in range(0, 2**self.num_edges-1)]
        shortest_path[0][0] = 0
        for m in range(2,self.num_edges+1):
            print(m)
            for s in self.set_iterator(m):
                for j in self.vertex_iterator(s):
                    if j == 0:
                        continue
                    s_minus_j = s-(1<<j)
                    for k in self.vertex_iterator(s_minus_j):
                        try_value = shortest_path[s_minus_j-1][k] + self.distance[k][j]
                        if try_value < shortest_path[s-1][j]:
                            shortest_path[s-1][j] = try_value
        shortest_tour = float("inf")      
        s = (1<<self.num_edges)-1
        for j in self.vertex_iterator(s):
            try_value = shortest_path[s-1][j] + self.distance[j][0]
            if try_value < shortest_tour:
                shortest_tour = try_value
        return shortest_tour

    def set_iterator(self, size):
        for i in tuple(itertools.combinations(range(1, self.num_edges),size-1)):
            s = 1
            for j in i:
                s += 1 << j
            yield s
        
    def vertex_iterator(self, set_value):
        for i in range (0, math.ceil(math.log2(set_value+1))):
            if (set_value >> i) & 1:
                yield i



        
    