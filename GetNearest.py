__author__ = 'angelee'

from copy import deepcopy
from GetMin import getMin

def getNearest(graph, json_obj, context, film_id):
    edges = context[json_obj["params"]["GetFrom"]].items()

    edges_copy = []

    for edge in edges:
        edges_copy.append(deepcopy(edge))

    context[film_id] = getMinMany(edges_copy)

def getMinMany(edges):

    numPairs = int(len(edges) / 2)
    print(numPairs)
    if numPairs == 0:
        if len(edges) > 0:
            return edges[0][0]
        else:
            return None
    else:
        new_group = []

        for i in range(0, numPairs, 2):
            new_group.append(getMin(edges[i], edges[i + 1]))

        if len(edges) % 2 > 0:
            new_group.append(edges[len(edges) - 1])

        return getMinMany(new_group)
