#!/usr/bin/env python3
"""
Module Docstring
"""
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
    points[0] = 1


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
