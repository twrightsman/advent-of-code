import sys
import re
import networkx as nx

# Borrowed Day 9 code to calculate path with highest happiness total

class Guest:
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

    def get_root(self):
        current = self
        while current.parent != None:
            current = current.parent
        return current

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Guest({})'.format(self.name)

instruction_pattern = re.compile(r'^([A-Z][a-z]+) would ([a-z]{4}) ([0-9]+) happiness units by sitting next to ([A-Z][a-z]+).')

relationships = nx.DiGraph()

for line in sys.stdin:
    result = re.match(instruction_pattern, line)

    person1 = result.group(1)
    change_sign = result.group(2)
    if change_sign == 'gain':
        change = int(result.group(3))
    else:
        change = -1 * int(result.group(3))
    person2 = result.group(4)

    relationships.add_edge(person1, person2, weight=change)

levels = {'0': []}
for guest in relationships.nodes():
    levels['0'].append(Guest(guest, None))

for level in range(1, len(relationships.nodes())):
    levels[str(level)] = []
    for parent_node in levels[str(level - 1)]:
        remaining_nodes = [guest for guest in relationships.nodes()]
        remaining_nodes.remove(parent_node.name)

        for remaining_parent in parent_node.get_all_parents():
            remaining_nodes.remove(remaining_parent.name)

        if remaining_nodes:
            for remaining_node in remaining_nodes:
                levels[str(level)].append(Guest(remaining_node, parent_node))

levels[str(len(relationships.nodes()))] = []
for parent_node in levels[str(len(relationships.nodes()) - 1)]:
    levels[str(len(relationships.nodes()))].append(Guest(parent_node.get_root().name, parent_node))

def get_total_weight_of_path(node):
    '''Returns a tuple of the path length and the path that has that length'''
    path_weights = nx.get_edge_attributes(relationships, 'weight')
    path = node.get_all_parents()
    #add the leaf node as the first node in the path
    path.insert(0, node)
    edges = []

    for edge_id in range(1, len(path)):
        edges.append([path[edge_id - 1], path[edge_id]])

    total_path_length = 0
    for edge in edges:
        total_path_length += path_weights[edge[0].name, edge[1].name]
        total_path_length += path_weights[edge[1].name, edge[0].name]

    return (total_path_length, path)

path_lengths = []
for node in levels[str(len(relationships.nodes()))]:
    path_lengths.append(get_total_weight_of_path(node))

#needed a key function to sort the list of tuples by total path length
def getPathLength(item):
    return item[0]

path_lengths = sorted(path_lengths, key=getPathLength)

print(path_lengths[-1])