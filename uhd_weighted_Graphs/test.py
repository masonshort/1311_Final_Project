import networkx as nx
#import matplotlib.pyplot as plt
from functions.drawings import show_weighted_graph, draw_subtree
#from functions.prims_functions import cost, min_prims_edge, spans, incident_edges, valid_edges, prims_algorithm

G = nx.read_weighted_edgelist('C:\\Users\\Mason Short\\code\\1311_Final\\uhd_weighted_Graphs\\data\\G1.txt', nodetype = int)
#G = nx.Graph(G)
#T = nx.read_edgelist('C:\\Users\\Mason Short\\code\\1311_Final\\uhd_weighted_Graphs\\data\\G2.txt', nodetype = int)
#T = nx.Graph(T)


#prims_algorithm(G, next(iter(G.nodes())),draw = True)


mst = nx.minimum_spanning_tree(G,weight='weight',algorithm='prim')
print("answer")
show_weighted_graph(mst)
