""" Test TSFFinder """
import TSPFinder

def test_answer():
    """ tests TSPFinder """
    tsp_finder = TSPFinder.TSPFinder(4)
    tsp_finder.add_edge(1, 2, 2)
    tsp_finder.add_edge(1, 3, 1)
    tsp_finder.add_edge(1, 4, 4)
    tsp_finder.add_edge(2, 3, 3)
    tsp_finder.add_edge(2, 4, 5)
    tsp_finder.add_edge(3, 4, 6)
    assert tsp_finder.get_shortest_tour() == 13
    