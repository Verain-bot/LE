class BST:
    def __init__(self, arr : list) -> None:
        self.arr = arr
        self.root = None
        self.height = 0
        self.makeBST()
    
    def immChildren(self, node):
        s = set()
        if node is None:
            return s

        if node.right is not None:
            s.add('right')
        if node.left is not None:
            s.add('left')
        
        return s

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

    def add(self, value):
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


class Heap(BST):
    
    def __init__(self, arr : list) -> None:
        super().__init__(arr)
        self.heapify(self.root)
    
    def add(self, value):
        super().add(value)
        self.heapify(self.root)


    def heapify(self, node):
        children = self.immChildren(node)
        right = 'right'
        left = 'left'
        if left not in children and right not in children:
            return None
        
        self.heapify(node.left)
        self.heapify(node.right)


        
        if right in children:
            rightVal = node.right.value 
        if left in children:
            leftVal = node.left.value

        if left not in children or (right in children and rightVal >= leftVal) and node.value < rightVal:
            node.right.value, node.value = node.value, node.right.value
            self.heapify(node.right)
        elif node.value < leftVal:
            node.left.value, node.value = node.value, node.left.value
            self.heapify(node.left)
    


        


x = [4, 10, 3, 5, 1]
y = BST(x)
x = Heap(x)
x.add(11)
y.print()
x.print()