# 효율적인 풀이
(왼쪽에는)sunday를 (오른쪽에는)saturday로 변경하는 비용 계산하는 테이블 이용
(0,0)~(0,8) 초기화(0,1,2,...,8), (0,0)~(6,0) 초기화(0,1,2,...,6)
각 row마다 진행을 해주는데 dp[i][j] = dp[i-1][j-1] if x = y , dp[i][j] = 1 + min(dp[i][j-1] (삽입), dp[i-1][j] (삭제), dp[i-1][j-1] (교체)) else 
# 실수한 부분
string 객체는 reverse(), sort()존재 x(list에만)
단, sorted(string) -> 알파벳 정렬 후 list로 return함!
string = list(string)
string.reverse()  reverse()는 return하는 값 없음 **주의!**
string = "".join(list(string).reverse())

string = string[::-1]