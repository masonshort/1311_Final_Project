import networkx as nx
from functions.drawings import show_weighted_graph

G = nx.read_weighted_edgelist('C:\\Users\\Mason Short\\code\\1311_Final\\uhd_weighted_Graphs\\data\\G1.txt', nodetype = int)



#Using the built-in Prim's algorithm in networkx
#to compare to my final answer
mst = nx.minimum_spanning_tree(G,weight='weight',algorithm='prim')
print("answer")
show_weighted_graph(mst)
