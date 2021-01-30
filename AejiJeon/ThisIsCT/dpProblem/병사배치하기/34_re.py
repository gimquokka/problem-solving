import sys
input = sys.stdin.readline

def getLISLength(array, n):
    
    dp = [1]*n # 1로 초기화 -> array[i]만을 갖는 부분수열 항상 존재(min) 

    # LIS 점화식 적용
    for i in range(1, n):
        for j in range(0, i):

            if array[j] < array[i]:
                 
                dp[i] = max(dp[i], 1 + dp[j])
                
    return max(dp)
    
n = int(input())
array = list(map(int, input().split()))
array.reverse()

max_length = getLISLength(array, n)

# 빼야되는 최소한의 숫자 수
print(n - max_length)

