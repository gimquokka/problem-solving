from itertools import permutations
n = int(input())
sequence = list(map(int, input().split()))
ops = []
lst = list(map(int, input().split()))

for i in range(4):
    for j in range(lst[i]):
        ops.append(i)
print(sequence)
print(ops)


perms = list(permutations(ops, n-1))
print(perms)
max_result = -1e10
min_result = 1e10

def cal(x,y,op):
    if op == 0:
        return x+y
    elif op == 1:
        return x - y
    elif op == 2:
        return x*y
    elif op == 3:
        if x*y<0:
            return (abs(x)//abs(y))*(-1)
        return x//y           


for perm in perms:
    n_seq = sequence[:]
    
    for i in range(n-1):
        
        n_seq[i+1] = cal(n_seq[i],n_seq[i+1],perm[i])
    
    print(n_seq)
    max_result = max(max_result, n_seq[n-1])
    min_result = min(min_result, n_seq[n-1])

print(max_result)
print(min_result)
