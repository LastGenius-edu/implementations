"""
File: algorithms.py
Project 12.5

Complete the function breadthFirst.

Graph processing algorithms
"""

from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from grid import Grid

INFINITY = "-"

def shortestPaths(g, startLabel):
    startVertex = g.getVertex(startLabel)
    results = Grid(g.sizeVertices(), 3)
    included = list()
    initializeShortestPaths(results, included, g, startVertex)
    computeShortestPaths(results, included, g, startVertex)
    return results

def initializeShortestPaths(results, included, g, startVertex):
    row = 0
    for v in g.vertices():
        results[row][0] = v
        if v == startVertex:
            results[row][1] = 0
            included.append(True)
        elif g.containsEdge(startVertex.getLabel(),
                            v.getLabel()):
            edge = g.getEdge(startVertex.getLabel(),
                             v.getLabel())
            results[row][1] = edge.getWeight()
            results[row][2] = startVertex
            included.append(False)
        else:
            results[row][1] = INFINITY
            results[row][2] = None
            included.append(False)
        row += 1

def computeShortestPaths(results, included,
                         g, startVertex):
    while True:   
        minDistIndex = findVertWithMinDist(results,
                                           included)
        if minDistIndex == -1:
            break
        included[minDistIndex] = True
        for row in range(g.sizeVertices()):
            if not included[row]:
                fromVert = results[minDistIndex][0]
                toVert = results[row][0]
                if g.containsEdge(fromVert.getLabel(),
                                  toVert.getLabel()):
                    edge = g.getEdge(fromVert.getLabel(),
                                     toVert.getLabel())
                    sumDist = addWithInfinity(results[minDistIndex][1],
                              edge.getWeight())
                    if isLessWithInfinity(sumDist, results[row][1]):
                        results[row][1] = sumDist
                        results[row][2] = fromVert
   
def findVertWithMinDist(results, included):
    minIndex = -1
    minDist = INFINITY
    for row in range(results.getHeight()):
        if not included[row]:
            dist = results[row][1]
            if isLessWithInfinity(dist, minDist):
                minDist = dist
                minIndex = row
    return minIndex

def topoSort(g, startLabel = None):  
    stack = LinkedStack()
    g.clearVertexMarks()
    for v in g.vertices():
        if not v.isMarked():
            dfs(g, v, stack)
    return stack

def dfs(g, v, stack):
    v.setMark()
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w, stack)
    stack.push(v)


def spanTree(g, startLabel):
    g.clearVertexMarks()
    unVisitedVertices = set(g.vertices())
    visitedVertices = []
    leastCostEdges = []
    startVertex = g.getVertex(startLabel)
    startVertex.setMark()
    visitedVertices.append(startVertex)
    unVisitedVertices.remove(startVertex)
    while len(unVisitedVertices) != 0:
        edge = findLeastCostEdge(visitedVertices, g)
        if edge is None:
            return leastCostEdges 
        u = edge.getToVertex()
        u.setMark()
        unVisitedVertices.remove(u)
        visitedVertices.append(u)
        leastCostEdges.append(edge)
    return leastCostEdges

def findLeastCostEdge(visitedVertices, g):
    def findLeastCost(v, g):
        resultEdge = None
        minWeight = INFINITY
        for edge in g.incidentEdges(v.getLabel()):
            toVertex = edge.getToVertex()
            if not toVertex.isMarked() and \
               isLessWithInfinity(edge.getWeight(), minWeight):
                minWeight = edge.getWeight()
                resultEdge = edge
        return resultEdge
    leastCostEdge = None
    for v in visitedVertices:
        leastCostEdge = findLeastCost(v, g)
        if leastCostEdge != None:
            return leastCostEdge
    return leastCostEdge

def breadthFirst(g, startLabel):
    """Returns a list of the vertex labels in the
    order in which the vertices were visited."""
    result = list()
    g.clearVertexMarks()
    queue = LinkedQueue()
    queue.add(g.getVertex(startLabel))
    while not queue.isEmpty():
        vertex = queue.pop()
        if not vertex.isMarked():
            vertex.setMark()
            result.append(vertex.getLabel()) 
            for neighbor in g.neighboringVertices(vertex.getLabel()):
                if not neighbor.isMarked():
                    queue.add(neighbor)
    return result
   
def isLessWithInfinity(a, b):
    """Returns False if a == b or a == INFINITY and b != INFINITY.
    Otherwise, returns True if b == INFINITY or returns a < b."""
    if a == INFINITY and b == INFINITY: return False
    elif b == INFINITY: return True
    elif a == INFINITY: return False
    else: return a < b

def addWithInfinity(a, b):
    """If a == INFINITY or b == INFINITY, returns INFINITY.
    Otherwise, returns a + b."""
    if a == INFINITY or b == INFINITY: return INFINITY
    else: return a + b



