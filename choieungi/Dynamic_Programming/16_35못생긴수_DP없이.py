#35 못생긴 수
N= int(input())
from itertools import combinations_with_replacement

n=0
equation = (n+1)*(n+2)

#3Hn 에서 n 구하기
while (equation<6000):
    n+=1
    equation = n*(n + 1) * (n + 2)


#x+y+z+w = 10에서 x,y,z,w의 값들을 구한다.
raw_all_case = list(combinations_with_replacement(['x','y','z','w'], n))
all_case = [ ]
for i in raw_all_case:
    all_case.append((i.count('x'),i.count('y'),i.count('z')))

ugly_nums =[ ]
for i in all_case:
    ugly_num = (2**i[0])*(3**i[1])*(5**i[2])
    ugly_nums.append(ugly_num)

ugly_nums.sort()
print(ugly_nums[N-1])