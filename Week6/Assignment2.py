# You are given an undirected graph of n vertices umbered from 0 to n-1
# and m edges between them. Each edge og the graph is weighted,each weight is a positive
# integer. You are given the list of eadges along with their weights, but the 
# list is damaged: some of the weight is lost.
# you want the length of the shorted path between vertices s and t in the 
# graph to be exclty L.
# Is it possible to restore somre or all of the missing weights to make this happen
import sys

class Graph:
    def __init__(self,Nodes):
        self.nodes=Nodes
        self.adj_list={}
        for node in self.nodes:
            self.adj_list[node]={}


    def add_edge(self,u,v,w):
        self.adj_list[u][v]=w
        self.adj_list[v][u]=w
    
    def print_adj_list(self):
        return self.adj_list

def Dijkstra(graph,source,destination):
    visited=[]
    distance={}
    path={}
    for node in graph.nodes:
        inf = sys.maxsize
        distance[node]=inf
        path[node]=None
    distance[source]=0
    while len(visited)!=len(graph.nodes):
        min_node=None
        for node in graph.nodes:
            if node not in visited and (min_node is None or distance[node]<distance[min_node]):
                min_node=node
        visited.append(min_node)
        for neighbour in graph.adj_list[min_node].keys():
            if distance[neighbour]>distance[min_node]+graph.adj_list[min_node][neighbour]:
                distance[neighbour]=distance[min_node]+graph.adj_list[min_node][neighbour]
                path[neighbour]=min_node
    return distance[destination]

if __name__ == '__main__':
    n,m,l,s,t=list(map(int,input().split()))
    nodes=[]
    for i in range(n):
        nodes.append(i)
    graph=Graph(nodes)
    edge_list=[]
    inf = sys.maxsize
    for i in range(m):
        u,v,w=list(map(int,input().split()))
        edge_list.append((u,v,w))
    for u,v,w in edge_list:
        if(w==0):
            graph.add_edge(u,v,inf)
        else:
            graph.add_edge(u,v,w)
    edge_list = graph.print_adj_list()
    min_weight=Dijkstra(graph,s,t)
    if(m==1):
        if(min_weight==inf):
            print("YES")
        elif(min_weight==l):
            print("YES")
        else:
            print("NO")
    elif(min_weight>=l and min_weight<=inf):
        print("YES")
    else:
        print("NO")
    

