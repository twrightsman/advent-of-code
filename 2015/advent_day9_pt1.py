import sys
import re
import networkx as nx

line_pattern = re.compile(r'([A-Za-z]+) to ([A-Za-z]+) = ([0-9]+)')

city_graph = nx.Graph()

for line in sys.stdin:
    result = re.match(line_pattern, line)

    node1 = result.group(1)
    node2 = result.group(2)
    distance = int(result.group(3))

    #create the networkx graph using the given edges in the input
    #networkx adds the nodes automatically if not already present
    city_graph.add_edge(node1, node2, weight=distance)

class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def get_all_parents(self):
        '''Returns a list of all of a node's parents, up to the root'''
        parents = []
        current = self
        while current.parent != None:
            parents.append(current.parent)
            current = current.parent

        return parents

    #made these for testing purposes
    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Node({})'.format(self.name)

#needed to create a tree of all possible paths between nodes
#(since the problem is to get the shortest path that includes all nodes,
# the instructions must, for each node, give distances to each other node.
# the code below assumes that is true, rather than checking)

#decided to manage the "tree" with a dictionary of tree levels
levels = {'0': []}
for node in city_graph.nodes():
    levels['0'].append(Node(node, None))

for level in range(1, len(city_graph.nodes())):
    levels[str(level)] = []
    for parent_node in levels[str(level - 1)]:
        remaining_nodes = [node for node in city_graph.nodes()]
        remaining_nodes.remove(parent_node.name)

        for remaining_parent in parent_node.get_all_parents():
            remaining_nodes.remove(remaining_parent.name)

        if remaining_nodes:
            for remaining_node in remaining_nodes:
                levels[str(level)].append(Node(remaining_node, parent_node))

def get_total_weight_of_path(node):
    '''Returns a tuple of the path length and the path that has that length'''
    path_weights = nx.get_edge_attributes(city_graph, 'weight')
    path = node.get_all_parents()
    #add the leaf node as the first node in the path
    path.insert(0, node)
    edges = []

    for edge_id in range(1, len(path)):
        edges.append([path[edge_id - 1], path[edge_id]])

    total_path_length = 0
    for edge in edges:
        try:
            total_path_length += path_weights[edge[0].name, edge[1].name]
        except KeyError:
            total_path_length += path_weights[edge[1].name, edge[0].name]

    return (total_path_length, path)

path_lengths = []
for node in levels[str(len(city_graph.nodes()) - 1)]:
    path_lengths.append(get_total_weight_of_path(node))

#needed a key function to sort the list of tuples by total path length
def getPathLength(item):
    return item[0]

path_lengths = sorted(path_lengths, key=getPathLength)

print(path_lengths[0])