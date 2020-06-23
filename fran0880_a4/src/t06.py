'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-02-04"
-------------------------------------------------------
'''
from prims import prims
from Graph import Graph, Edge
# data = (
#     ('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 7), ('B', 'C', 6), ('B', 'G', 4),
#     ('C', 'E', 1), ('C', 'F', 8), ('D', 'E', 5), ('E', 'F', 4), ('F', 'G', 2)
# )
data = (
    ('A', 'B', 3), ('A', 'C', 3), ('B', 'C', 4), ('B', 'H', 6), ('C', 'E', 6),
    ('C', 'D', 3), ('D', 'G', 7), ('E', 'G', 4), ('E', 'F', 7), ('F', 'I', 5),
    ('F', 'H', 3),  ('G', 'I', 9),  ('H', 'I', 4)
)

edge_list = []
for i in range(len(data)):
    edge_list.append(Edge(data[i][0], data[i][1], data[i][2]))
graph = Graph(edge_list)
start_node = 'A'
graph.node_names()
edges, total = prims(graph, start_node)

print('Edges:', len(edges))
print('Total:', total)