import sys
import math
input = sys.stdin.readline


n, m = map(int, input().split())

# 여러 보석 중에서 색이 같은 보석 개수의 쵀댓값
max_value = 0

numberOfJewerlies = []
for _ in range(m):
    num = int(input())
    numberOfJewerlies.append(num)
    max_value = max(max_value, num)

def binary_search_opt(array, start, end):
    
    
    while True:
        if start > end:
            return 
        # start, start + 1, ..., end 중 중앙값
        mid = start + (end - start) // 2
        # 보석을 각 학생에게 mid개 씩 나눠줄 때(남은 보석은 한 사람에게 다 줌)
        # 보석을 받은 학생 수 계산
        target = 0
        for num in array:
            # 한 종류의 보석에 대해 mid개씩 나줘줄 수 있는 학생 수
            target += math.ceil(num / mid)
        
        # 보석을 다 나눠주었을 때 
        # 보석을 안 받은 학생이 존재하거나 모든 학생이 보석을 받은 경우
        if target <= n:
            # 최적화 된 값을 찾기 위해 
            # result값에 mid값 할당
            result = mid
            
            end = mid - 1
        # mid개씩 나눠줄 때 보석이 남는 경우 
        else:
            start = mid + 1

result = 0
# 1부터 max_value까지 이진 탐색을 이용하여 최적화된 값 찾기
binary_search_opt(numberOfJewerlies, 1, max_value)

print(result)

