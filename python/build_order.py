"""4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""
from collections import Counter
class Graph():
    """graph from edges
    """
    def __init__(self, nodes, edges=[]):
        self.nodes = set(nodes)
        self.in_degrees = Counter()
        self.edges = {}
        for node, neighbor in edges:
            self.in_degrees[neighbor] += 1
            self.edges.setdefault(node, []).append(neighbor)
    def __repr__(self):
        return repr(self.edges)
    def neighbors(self, node):
        return self.edges.get(node, ())

def build_order(graph: Graph)-> list:
    """get topological order, kahn's algorithm
    """
    # find nodes with no incoming edges O(n)
    sources = list(graph.nodes - set(graph.in_degrees.keys()))
    if not sources: raise ValueError('no valid build order')
    # execute modified dfs to find topological order
    res = sources[:]
    def dfs(node):
        for neighbor in graph.neighbors(node):
            graph.in_degrees[neighbor] -= 1
            print(f'current_node: {node}, neighbor: {neighbor}, sources: {sources}, counter: {graph.in_degrees}')
            # when the in_degree counter reaches 0 add node to the remaining sources and res
            if graph.in_degrees[neighbor] == 0:
                del(graph.in_degrees[neighbor])
                res.append(neighbor)
                sources.append(neighbor)
    # iterate kahn's algorithm in the remaining sources
    while sources:
        dfs(sources.pop())
    return res

# test
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
edges = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
test = Graph(nodes, edges)
print(f'test: {test}, build_order: {build_order(test)}')
