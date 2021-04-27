from itertools import combinations

n,m = map(int,input().split())
num = list(map(int,input().split()))
all_case = list(combinations(num, 2)) #combinations 함수는 num C 2의 경우의 수를 튜플로 출력한다.
overlap_case = 0

for i in all_case:
    if i[0]==i[1]:
        overlap_case+=1

result = len(all_case)-overlap_case
print(result)



