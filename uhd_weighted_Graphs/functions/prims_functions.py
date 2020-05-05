import networkx as nx


def incident_edges(G,T):
    
    incident_edges = set()
    
    for e in G.edges():
        for v in T.nodes():
            if v in e:
                incident_edges.add(e)
    
    return incident_edges


def valid_edges(G,T):
    
    incident = incident_edges(G,T)
    valid = set()
    
    for e in incident:
        for v in e:
            if v not in T.nodes():
                valid.add(e)
                
    return valid 


def spans(G,T):
    G_set = set(G.nodes())
    T_set = set(T.nodes())
    
    return (G_set == T_set)

    
def cost(e,G):
    weight = nx.get_edge_attributes(G, 'weight')
    return weight[e]

    
def min_prims_edge(G,T):    
    valid = valid_edges(G,T)
    min_edge = next(iter(valid))    

    for e in valid:
        if cost(e,G) < cost(min_edge,G):
            min_edge = e
    
    return min_edge
