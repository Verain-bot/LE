from funs import Node,toNodes,Search
J1,J2,Target = 4,3,2
start = Node((0,0))
end = Node((0,Target))

@toNodes
def neighbours(node):
    m,n = node.value
    x = set()
    x.add((m,0))
    x.add((0,n))
    x.add((J1,n))
    x.add((m,J2))
    if m+n>=J1:
        x.add((J1,m+n-J1))
    if m+n<J1:
        x.add((m+n,0))
    if m+n>=J2:
        x.add((m+n-J2,J2))
    if m+n<J1:
        x.add((0,m+n))
    return x

print(Search(start,end,neighbours))