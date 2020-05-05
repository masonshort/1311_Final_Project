import networkx as nx
import matplotlib.pyplot as plt
from functions.drawings import show_weighted_graph, draw_subtree
from functions.prims_functions import cost, min_prims_edge, spans, valid_edges


def prims_algorithm(G, draw = False):
    T = nx.Graph()
    T.add_node(next(iter(G.nodes())))
    
    if draw == True:
        draw_subtree(G, T)
                
    while not spans(G,T):
        e = min_prims_edge(G,T)
        #print(valid_edges(G,T))
        T.add_edge(e[0], e[1], weight = cost(e, G))
        T.add_node(e[0])
        #print(spans(G,T))
    if draw == True:
        draw_subtree(G, T)

    return T


