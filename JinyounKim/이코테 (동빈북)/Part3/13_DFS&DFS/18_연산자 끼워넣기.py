from itertools import permutations

n = int(input())

data = list(map(int, input().split()))

operators = []
oper_cnt = list(map(int, input().split()))
for idx, cnt in enumerate(oper_cnt):
    for _ in range(cnt):
        operators.append(idx)

max_ans = 0
min_ans = int(1e10)
for cases in permutations(operators):
    result = data[0]
    for idx, op in enumerate(cases):
        if op == 0:
            result += data[idx+1]
        elif op == 1:
            result -= data[idx+1]
        elif op == 2:
            result *= data[idx+1]
        elif op == 3:
            if result < 0:
                result = -(abs(result)//data[idx+1])
            else:
                result = result//data[idx+1]
    max_ans = max(result, max_ans)
    min_ans = min(result, min_ans)

print(max_ans)
print(min_ans)