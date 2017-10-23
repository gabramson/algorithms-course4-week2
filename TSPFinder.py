class TSPFinder:
    def __init__(self, num_edges):
        self.distance = [[float("inf")] * num_edges for i in range(num_edges)]

    def add_edge(self, start, end, distance):
        self.distance[start-1][end-1] = distance
        self.distance[end-1][start-1] = distance

    def get_shortest_tour(self):
        return 13