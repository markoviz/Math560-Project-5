"""
Math 560
Project 5
Fall 2021

Partner 1:GEN XU (Net id: 1082087)
Partner 2:
Date:12/1
"""

# Import math, itertools, and time.
import math
import itertools
import time

# Import the Priority Queue.
from p5priorityQueue import *

################################################################################

"""
Prim's Algorithm
"""
def prim(adjList, adjMat):
    # initialize all cost to infinity, prev to None and visited to False
    for vertex in adjList:
        vertex.cost = math.inf
        vertex.prev = None
        vertex.visited = False

    # pick an start vertex. here let the first vertex be start vertex
    # set start.cost = 0
    vertex = adjList[0]
    vertex.cost = 0

    # make a priority queue using cost for sorting
    Q = PriorityQueue(adjList)

    # if priority queue is not empty
    while not Q.isEmpty():
        # get the next unvisited vertex and visit it
        vertex = Q.deleteMin()
        vertex.visited = True

        # for each edge out of vertex
        for neigh in vertex.neigh:
            # if the edge leads out, update
            if not neigh.visited:
                if neigh.cost > adjMat[vertex.rank][neigh.rank]:
                    neigh.cost = adjMat[vertex.rank][neigh.rank]
                    neigh.prev = vertex # mark neigh.prev as the vertex
    return

################################################################################

"""
Kruskal's Algorithm
Note: the edgeList is ALREADY SORTED!
Note: Use the isEqual method of the Vertex class when comparing vertices.
"""
def kruskal(adjList, edgeList):
    # initialize all singleton sets for each vertex
    for vertex in adjList:
        makeset(vertex)

    # initialize the empty MST
    X = []

    # loop through edges in order
    for edge in edgeList:
        # if the min edge crosses a cut, add it to MST
        u = edge.vertices[0]
        v = edge.vertices[1]
        # if u and v are not connected by an edge
        if find(u) != find(v):
            X.append(edge) # append the edge
            union(u, v)
    return X

################################################################################

"""
Disjoint Set Functions:
    makeset
    find
    union

These functions will operate directly on the input vertex objects.
"""

"""
makeset: this function will create a singleton set with root v.
"""
def makeset(v):
    # initialize v by set v.pi=v and v.height=0
    v.pi = v
    v.height = 0
    return

"""
find: this function will return the root of the set that contains v.
Note: we will use path compression here.

"""
def find(v):
    # if v is not at the root
    if v != v.pi:
        # set v.pi be the root
        v.pi = find(v.pi)
    # return the root, which is parent of v now
    return v.pi

"""
union: this function will union the sets of vertices v and u.
"""
def union(u,v):
    # find the root of the tree for u
    # find the root of the tree for v
    ru = find(u)
    rv = find(v)

    # if  sets of u and v are the same, return
    if ru == rv:
        return
    # make shorter set point to taller set
    if ru.height > rv.height:
        rv.pi = ru
    elif ru.height < rv.height:
        ru.pi = rv
    else:
        # same height, break tie
        ru.pi = rv
        # tree got taller, increase rv.height by 1
        rv.height += 1
    return

################################################################################

"""
TSP
"""
def tsp(adjList, start):
    # initialize by setting all vertex unvisited
    for vertex in adjList:
        vertex.visited = False
    # set a tour set and a stack
    tour = []
    neigh_list = [] # stack
    # set start vertex visited and append it to stack
    start.visited = True
    neigh_list.append(start)

    # if the stack is not empty
    while len(neigh_list) > 0:
        # vertex is one popped by stack
        # visit it and append it to tour
        vertex = neigh_list.pop()
        vertex.visited = True
        tour.append(vertex.rank)
        # traverse vertex in vertex.mstN
        for neigh in vertex.mstN:
            # append all the unvisited vertices to stack
            if not neigh.visited:
                neigh_list.append(neigh)

    # append the start vertex to finish the tour
    tour.append(start.rank)
    return tour

################################################################################

# Import the tests (since we have now defined prim and kruskal).
from p5tests import *

"""
Main function.
"""
if __name__ == "__main__":
    verb = False # Set to true for more printed info.
    print('Testing Prim\n')
    print(testMaps(prim, verb))
    print('\nTesting Kruskal\n')
    print(testMaps(kruskal, verb))
