import networkx as nx
from algorithms.prims_algorithm import prims_algorithm

#Final testing of my code on three seperate weighted graphs
G1 = nx.read_weighted_edgelist('.\data\G1.txt', nodetype = int)
G1 = nx.Graph(G1)

G2 = nx.read_weighted_edgelist('.\data\G2.txt', nodetype = int)
G2 = nx.Graph(G2)

G3 = nx.read_weighted_edgelist('.\data\G3.txt', nodetype = int)
G3 = nx.Graph(G3)

prims_algorithm(G1, draw = True)
print('----------')
prims_algorithm(G2, draw = True)
print('----------')
prims_algorithm(G3, draw = True)

