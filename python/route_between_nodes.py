"""4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
class Graph():
    """directed graph from adjacency list
    """
    def __init__(self, init={}):
        self.nodes = set()
        self.edges = init
        for node, neighbors in init.items():
            self.nodes.add(node)
    def __repr__(self):
        return repr(self.edges)
    def neighbors(self, node):
        return self.edges.get(node, ())

def find_route(graph: Graph, start: str, end: str)-> bool:
    """explore all connected components with the standard dfs
    """
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited: dfs(neighbor)
    dfs(start)
    return end in visited

# test
init = {'a': ('b',),
        'b': ('c',),
        'c': ('e', 'd'),
        'd': ('b',),
        'e': ('f',),
        'f': ('g',),
        'g': ('h',),
        'i': (),
        'j': ('a'),
        }
test = Graph(init)
start, end = 'a', 'i'
start, end = 'a', 'e'
print(f'graph: {test}, find_route? {find_route(test, start, end)}')
