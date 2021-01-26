from itertools import combinations
n = int(input())

graph = []
lst_Ts = []
lst_Xs = []
for i in range(n):
    data = input().split()
    graph.append(data)
    for j in range(n):
        if data[j] == 'T':
            lst_Ts.append((i,j))
        elif data[j] == 'X':
            lst_Xs.append((i,j))

combs = list(combinations(lst_Xs, 3))

def check_cross(x, y, graph):
    da = [0,0,1,-1]
    db = [1,-1,0,0]
    for i in range(4):
        a,b = x,y
        while True:
            na = a + da[i]
            nb = b + db[i]
            if na < 0 or na > n-1 or nb < 0 or nb > n-1:
                break
            elif graph[na][nb] == 'O':
                break
            elif graph[na][nb] == 'X':
                a,b = na, nb
            else:
                return False
    return True

def possible():
    for comb in combs:
        n_graph = []
        for i in range(n):
            n_graph.append(graph[i][:])
        
        for x,y in comb:
            n_graph[x][y] = 'O'
        checking = True
        for x, y in lst_Ts:
            if not check_cross(x,y,n_graph):
                checking = False
                break
        if checking:
            return True
    return False

print("YES" if possible() else "NO")
