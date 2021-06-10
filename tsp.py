import itertools 

graph = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

minCost= 99999
for p in itertools.permutations(range(4)):
    cost = sum(graph[p[i]][p[(i+1)%4]] for i in range(4))
    seq = p if cost<minCost else seq
    minCost = min(cost,minCost)
print(minCost,seq)