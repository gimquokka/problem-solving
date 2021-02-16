import sys
input = sys.stdin.readline

N = int(input())
data = [0]*N
for i in range(N):
    m, d, m1, d1 = input().split()
    a = int(m+d) if len(d) == 2 else int(m+'0'+d)
    b = int(m1+d1) if len(d) == 2 else int(m1+'0'+d)
    data[i] = (a, b)
data.sort()

"""
# [clear]
# Check input data
print(data)
"""

'''
1. 시작일이 0301보다 작을때 0 반환

3. 뒤에 오는 수가 전의 값의 포함되지 않을 때 0 반환
4. 최대 값이 1201보다 작을때 0 반환

2. 뒤에 오는 수가 전의 범위를 포함할때 전의 값 지워야함
6. 현재 검색하는 수중 앞에서 부터 탐색하여 앞쪽에서 매칭이 되면 사이 값들 삭제
5. 뒤 오는 수가 현재의 최대값보다 작으면 삭제


7. 최대 값이 1201보다 크면 return len(data[:i+1])
'''


def solve():

    # 1. 시작일이 0301보다 작을때 0 반환
    if data[0][0] > 301:
        return print(0)

    ans = []
    ans.append(data[0])
    for i in range(N-1):
        # 2. 뒤에 오는 수가 전의 범위를 포함할때 전의 값 지워야함
        for j in range(len(ans)):
            add = False
            if ans[-1][0] == data[i][0] and ans[-1][1] < data[i][1]:
                ans.pop()
                add = True
            else:
                break
            if add:
                ans.append(data[i])


    # for i in range(N):
solve()
