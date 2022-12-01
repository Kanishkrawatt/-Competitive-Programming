#  Tree is A graph that has no cycles , and a rooted tree is a tree in which one vertex has been designated the root.
# For this problem , assume that the edges of the trees are oriented away from the root,
# for example if the edges are (r,u) (r,v) (r,w) where r is the root , then the edges are grom r to u , r to v and r to w, respectively
# In a rooted tree, the parent of a vertex v is the vertex connected directly to v on the parth to the root 
#  Every vertex has a unique parent expcept the Root which has no paren .
#  A child of a vertex v is a vertex of which v is the parent.

from sqlite3 import Cursor


data={}
n = int(input())
for i in range(1,n+1):
    loc = int(input())
    data[i] = loc
Counts = []
count=-1
for i in data:
    if(data[i]==-1):
        if(count!=-1):
            Counts.append(count)
        count=1
    else:
        if(data[i]==count):
            count+=1
Counts.append(count)
print(max(Counts))