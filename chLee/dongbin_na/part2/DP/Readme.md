# 다이나믹 프로그래밍
: 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 푸는 방식
- 분할정복 문제(ex. 퀵 정렬)와 차이점
    : 다이나믹 프로그래밍은 문제들이 서로 영향을 미침
## 탑 다운 (Top Down)
- 메모제이션 (Memozation)
- 한 번 구한 결과를 메모리 공간에 메모해두고, 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 방식
    ~~~cpp
    //피보나치
    int fibo(int x) {
        if (x==1 or x==2) {
            return 1;
        }
        if (dp[x] != 0) {
            return dp[x];
        }
        dp[x] = fibo(x-1) + fibo(x-2);
        return dp[x];
    }
    ~~~
## 바텀 업 (Bottom Up)
- DP테이블
- DP테이블을 순차적으로 채워나가는 방식
    ~~~cpp
    //피보나치
    dp[1] = 1;
    dp[2] = 1;
    for (int i=3; i<n+1; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    ~~~