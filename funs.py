class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self,value):
        self.arr.append(value)
    
    def isEmpty(self):
        return len(self.arr)==0
    
    def pop(self):
        return self.arr.pop(-1)
class Queue:
    def __init__(self):
        self.arr = []
    
    def push(self,value):
        self.arr.append(value)
    
    def isEmpty(self):
        return len(self.arr)==0
    
    def pop(self):
        return self.arr.pop(0)
    
    def __repr__(self):
        return repr(self.arr)
class Node:
    def __init__(self,Value,Parent=None,depth = 0):
        self.value = Value
        self.parent = Parent
        self.depth = depth
    
    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)
    
    def __repr__(self):
        return repr(self.value)
def Search(start,end,Neighbours,is_BFS=True,depthLimit=-1):
    discovered = set()
    if is_BFS:
        queue = Queue()
    else:
        queue = Stack()
    queue.push(start)
    while not queue.isEmpty():
        node = queue.pop()
        discovered.add(node)

        if node == end:
            sol = []
            while node.parent is not None:
                sol.append(node)
                node = node.parent
            sol.reverse()
            return sol

        for neighbour in Neighbours(node):
            if neighbour not in discovered:
                if depthLimit>0:
                    if depthLimit>=node.depth:
                        queue.push(neighbour)
                else:
                    queue.push(neighbour)
    return False
def HillClimbing(start,Heuristic,Neighbours):
    node = start
    while True:
        new = max(Neighbours(node),key=lambda x: Heuristic(x))
        if Heuristic(node)>=Heuristic(new):
            sol = []
            while node.parent is not None:
                sol.append(node.value)
                node = node.parent
            sol.reverse()
            return sol
        node = new
def toNodes(fun):
    def inner(*args,**kwargs):
        return [Node(x,args[0],args[0].depth+1) for x in fun(*args,**kwargs)]
    return inner
