
# 가장 긴 증가하는 수열 찾기
def getLIS(array):
    n = len(array)

    # 갱신될 때마다 부분 수열 담는 array
    dp_arrays = [[i] for i in array]
    
    dp = [1]*n
    for i in range(1, n):
        for j in range(0, i):

            if array[j] < array[i]:
                 # dp table 갱신
                if dp[j] + 1 > dp[i]:

                    dp[i] = dp[j] + 1
                    # 갱신된 길이 가진 LIS 담기 
                    # dp_arrays의 j번째 배열에 input array의 i 번째 원소 추가
                    temp = dp_arrays[j][:]
                    temp.append(array[i])
                    dp_arrays[i] = temp

    max_length = 0
    index = 0
    for i in range(n):
        if dp[i] > max_length:
            max_length = dp[i]
            index = i
    return dp_arrays[index]

array = [10,20,10,30,20,50]
LIS = getLIS(array)
print(LIS)
