from funs import *
end = Node((
    1,2,3,
    4,5,6,
    7,8,0,
))
start = Node((
    0,1,3,
    4,2,5,
    7,8,6,
))

@toNodes
def neighbours(node):
    state = list(node.value)
    n = set()
    index = state.index(0)
    if index%3 <= 1:
        x = state[:]
        x[index],x[index+1] =x[index+1],x[index]
        n.add(tuple(x))
    
    if index%3 >= 1:
        x = state[:]
        x[index],x[index-1] =x[index-1],x[index]
        n.add(tuple(x))
    
    if index//3 <= 1:
        x = state[:]
        x[index],x[index+3] =x[index+3],x[index]
        n.add(tuple(x))

    if index//3 >= 1:
        x = state[:]
        x[index],x[index-3] =x[index-3],x[index]
        n.add(tuple(x))
    
    return n

def Heuristic(node):
    state = node.value
    x = 0
    for i in range(9):
        x += abs(state.index(i)-end.value.index(i))
    return -x

print(*Search(start,end,neighbours),sep='\n',end='\n\n')            #Using BFS
#It gives very long answer using DFS so in the print ive shown using Depth Limited Search
#If you want to see the output using DFS just remove last argument
print(*Search(start,end,neighbours,is_BFS=False,depthLimit=5),sep='\n',end='\n\n')
print(*HillClimbing(start,Heuristic,neighbours),sep='\n')                     #Using Hill Climbing