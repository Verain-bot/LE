from funs import *
import itertools
start = Node(
    (
        (1,),
        (2,3),
    )
)
end = Node(
    (
        (3,2,1),
    )
)

@toNodes
def neighbours(node):
    state = list(node.value)
    n = set()
    for i,j in itertools.combinations(range(len(state)),2):
        cpy = state[:]
        x = list(cpy.pop(i))
        y = list(cpy.pop(j-1))

        x2,y2 = x[:],y[:]
        cpy2 = cpy[:]
        
        y.append(x.pop(-1))
        x2.append(y2.pop(-1))
        x,y,x2,y2 = tuple(x),tuple(y),tuple(x2),tuple(y2)


        if len(x)>0:
            cpy.insert(i,x)
        cpy.insert(j,y)

        cpy2.insert(i,x2)
        if len(y2)>0:
            cpy2.insert(j,y2)
        
        n.add(tuple(cpy))
        n.add(tuple(cpy2))
    for i in range(len(state)):
        cpy = state[:]
        x = list(cpy.pop(i))
        if len(x)<=1:
            continue
        y = [x.pop(-1)]
        cpy.insert(i,tuple(x))
        cpy.append(tuple(y))
        n.add(tuple(cpy))
    return n


print(*Search(start,end,neighbours),end='\n\n',sep='\n')                            #BFS
print(*Search(start,end,neighbours,is_BFS=False),end='\n\n',sep='\n')               #DFS
print(*Search(start,end,neighbours,is_BFS=False,depthLimit=5),end='\n\n',sep='\n')  #Depth Limited Search

