def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    dp = [[0]*(m+1) for _ in range(n+1)]

    # 공백 문자에 대하여 각각 초기화
    for i in range(0, n+1):
        dp[i][0] = i
    for j in range(0, m+1):
        dp[0][j] = j
    
    for x in range(1, n+1):
        for y in range(1, m+1):
            # 두 문자열의 같은 위치의 문자가 같은 경우 => 대각선 + 1 
            if str1[x-1] == str2[y-1]:
                dp[x][y] = dp[x-1][y-1]
            # 두 문자열의 같은 위치의 문자가 다른 경우 => min(대각(교체), 위(삭제), 왼쪽(삽입)) + 1
            else:
                dp[x][y] = 1 + min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1])
    
    return dp[n][m]

# str2 = 'sunday'
# str1 = 'saturday'

str1 = input()
str2 = input()

print(edit_dist(str1, str2))
