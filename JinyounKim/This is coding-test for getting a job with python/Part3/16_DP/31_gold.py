import sys 
input = sys.stdin.readline

for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0]*m for _ in range(n)]
    
    # Asign dp table
    for i in range(0, len(a), m):
        dp[i//m] = a[i:i+m]
    print(dp)

    for y in range(1, m):
        for x in range(n):
            upper_left, left, lower_left = 0, 0, 0
            # From upper left
            if x != 0:
                upper_left = dp[x-1][y-1]
            # From left
            left = dp[x][y-1]
            # From lower left
            if x != n-1:
                lower_left = dp[x+1][y-1]
            dp[x][y] += max(upper_left, left, lower_left)
    
    result = 0
    for x in range(n):
        result = max(dp[x][m-1], result)
    print(result)
        
            
