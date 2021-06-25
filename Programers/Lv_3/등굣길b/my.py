'''
Strategy
number of way to reaching (x, y)
= N(x, y) = N(x-1, y) + N(x, y-1)
'''

def solution(m, n, puddles):
    # init graph
    graph = [[0]*m for _ in range(n)]
    
    # set start point as 1
    graph[0][0] = 1
    
    # set puddles poin as -1
    for y, x in puddles:
        graph[x-1][y-1] = -1
        
    # DP with n x m graph(= memorization)
    for x in range(0, n):
        for y in range(0, m):
            # if current point is not a puddle
            if graph[x][y] != -1:
                # if upward is not puddle add number of way that (x-1 , y) can reached
                if 0 <= x-1 and graph[x-1][y] != -1:
                    graph[x][y] += graph[x-1][y] 
                # if leftside is not puddle add number of way that (x , y-1) can reached
                if 0 <= y-1 and graph[x][y-1] != -1:
                    graph[x][y] += graph[x][y-1]
    
    
    return graph[n-1][m-1]%(1000000007)


print(solution(4, 3, [[2, 2]]))