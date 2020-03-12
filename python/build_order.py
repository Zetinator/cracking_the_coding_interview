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
class Graph():
    """graph from edges
    """
    def __init__(self, nodes, edges=[]):
        self.nodes = set(nodes)
        self.incoming = set()
        self.edges = {}
        for node, neighbor in edges:
            self.incoming.add(neighbor)
            self.edges.setdefault(node, []).append(neighbor)
    def __repr__(self):
        return repr(self.edges)
    def neighbors(self, node):
        return self.edges.get(node, ())

def build_order(graph: Graph)-> list:
    """get topological order, kahn's algorithm
    """
    # find nodes with no incoming edges
    sources = graph.nodes - graph.incoming
    if not sources: raise ValueError('no valid build order')
    # execute standard dfs to find topological order
    res, visited = list(sources), set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited: dfs(neighbor); res.append(neighbor)
    for source in sources: dfs(source)
    return res

# test
nodes = ['a', 'b', 'c', 'd', 'e', 'f']
edges = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
test = Graph(nodes, edges)
print(f'test: {edges}, graph: {test}, build_order: {build_order(test)}')
