__author__ = 'angelee'

def getMin(node1, node2):
    if node1[1] < node2[1]:
        return node1
    elif node2[1] < node1[1]:
        return node2
    else:
        return node1
