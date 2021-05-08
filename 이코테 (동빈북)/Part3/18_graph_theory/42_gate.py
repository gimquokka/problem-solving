"""
g: num of gate
p: 들어올 비행기의 개수
g_i: 비행기를 넣을 수 있는 범위 1 ~ g_1

answer: g_i에 해당되는 최대 비행기의 개수를 출력
ex) 
2 2
2 1 
3 3
3 => x (1~3 x)

0 1 2 3 4 5 6
    2 2 => (4 > 3)
"""
import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

# Initialization
gate = [0]*(g+1)
answer = 0
for i in range(p):
    g_i = int(input())
    gate[g_i] += 1

for ~    
# 1 ~ g_i까지의 합이 g_i보다 크다는 것은 게이트가 부족하다는 뜻임으로
if sum(gate[:g_i+1]) > g_i:
    if answer == 0:
        answer = sum(gate)-1

# 게이트가 부족하지 않았음을 때
if answer == 0:
    print(p)
# 게이트가 부족하였을 때
else:
    print(answer)