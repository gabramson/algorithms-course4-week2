#!/usr/bin/env python3
"""
Module Docstring
"""
import math
import TSPFinder

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    myfile = open("tsp.txt", "r")
    vertices = int(myfile.readline())
    tsp_finder = TSPFinder.TSPFinder(vertices)
    points = [[0,0] for i in range(vertices)]
    i = 0
    for line in myfile:
        values = line.split()
        points[i][0] = float(values[0])
        points[i][1] = float(values[1])
        i += 1
    for i in range(vertices-1):
        for j in range(i+1, vertices):
            tsp_finder.add_edge(i,j, distance(points[i][0], points[i][1], points[j][0], points[j][1]))
    print(tsp_finder.get_shortest_tour())

def distance(x1, x2, y1, y2):
    return math.sqrt((x1-y1)**2 + (x2-y2)**2)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
