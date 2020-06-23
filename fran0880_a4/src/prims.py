'''
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Matthew Francis
ID:      180920880    
Email:   fran0880@mylaurier.ca
__updated__ = "2019-02-06"
-------------------------------------------------------
'''
from Graph import Edge
from Graph import Graph
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq

def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """ 
    edges =[]
    total = 0
    visited = ['A']
    pq = Priority_Queue()
    
    edges_to_node = graph.edges_by_node(start_node)
    array_to_pq(pq, edges_to_node)
    
    while not pq.is_empty() and len(visited) != len(graph.node_names()):
        route = pq.remove()
        while route.end in visited and route.start in visited:
            route = pq.remove()
        
        visited.append(route.end)
        edges.append(route)
        total += route.distance
        
        edge = graph.edges_by_node(route.end)
        
        for i in range(len(edge)):
            if edge[i].end not in visited:
                pq.insert(edge[i])
    return edges, total
                                    
    