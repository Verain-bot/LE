class BST:
    def __init__(self, arr : list) -> None:
        self.arr = arr
        self.root = None
        self.height = 0
        self.makeBST()
    
    class Node:
        def __init__(self,value = 0,parent=None,right=None,left=None,level = 0, position = 1) -> None:
            self.parent = parent
            self.value = value
            self.right = right
            self.left = left
            self.level = level
            self.position = position

        def __repr__(self) -> str:
            return str(self.value)

    def makeBST(self):
        self.root = self.Node(self.arr[0])
        for value in self.arr[1:]:
            node = self.root
            
            while node is not None:
                if value > node.value:
                    if node.right is not None:
                        node = node.right
                    else:

                        node.right = self.Node(value, node, level=node.level+1, position = 2*node.position)
                        self.height = max(self.height, node.right.level)
                        break
                    
                else:
                    if node.left is not None:
                        node = node.left
                    else:
                        node.left = self.Node(value,node,level=node.level+1, position=2*node.position-1)
                        self.height = max(self.height, node.left.level)
                        break
    
    def inorderTraversal(self, node = None):
        if node is not None:
            yield node
            yield from self.inorderTraversal(node.left)
            yield from self.inorderTraversal(node.right)

    def print(self):
        node = self.root
        level = -1
        start = 2**(self.height+1) -1 
        while (level := level+1) <= self.height:
            start = start//2
            n2p = list(filter(lambda x: x.level == level, self.inorderTraversal(self.root)))
            a2p = ['\t']*(2**(self.height+1))
            div = (2**(self.height-level+1)) 
            for i in n2p:
                a2p[start+ div*(i.position-1)] = i
            print(*a2p)


class Heap:
    
    def __init__(self, arr : list) -> None:
        self.arr = arr
        self.root = None
        self.height = 0
        
        self.heapify()
    
    def heapify(self):
        pass
    
    


        


x = [10,20,50,3,6,0.5,0,0.3]
x = BST(x)
x.print()