import networkx as nx

#Function incident_edges finds all of the edges connected
#to the first node.
def incident_edges(G,T):
    
    incident_edges = set()
    
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                incident_edges.add(e)
    
    return incident_edges

#Function valid_edges takes the edges returned in incident_edges
#and returns the edge if it is not already found in the subtree T
def valid_edges(G,T):
    
    incident = incident_edges(G,T)
    valid = set()
    
    for e in incident:
        for v in e:
            if v not in T.nodes():
                valid.add(e)
                
    return valid 

#Function to test if the subtree T spans the weighted graph G
def spans(G,T):
    G_set = set(G.nodes())
    T_set = set(T.nodes())
    
    return (G_set == T_set)

#Returns cost, or weight of edge given 
def cost(e,G):
    weight = nx.get_edge_attributes(G, 'weight')
    return weight[e]

#Function min_prims_edge finds the smallest weight of the valid edges given    
def min_prims_edge(G,T):    
    valid = valid_edges(G,T)
    min_edge = next(iter(valid))    

    for e in valid:
        if cost(e,G) < cost(min_edge,G):
            min_edge = e
    
    return min_edge
