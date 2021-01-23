#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int dp[101];

int main () {
    int N;
    cin >> N;
    vector<int> w(N);
    for (int i=0; i<N; i++) {
        cin >> w[i];
    }

    // dp[i] : 'i번째를 털었을 때, 최대 식량'
    // 1. 이게 맞나?
    // 2. 이게 맞아도, sort를 한 번 더 해야한다
    /*
    dp[0] = 0;
    dp[1] = w[0];
    dp[2] = w[1];
    for (int i=3; i<=N; i++) {
        dp[i] = max(dp[i-2], dp[i-3]) + w[i-1];
    }
    */

    // dp[i]의 정의를 'i번째 도착했을때, 최대 식량' 이라고 하면
    // dp[i] = max(dp[i-1], dp[i-2]+w[i]) 
    dp[0] = 0;
    dp[1] = w[0];
    for (int i=2; i<=N; i++) {
        dp[i] = max(dp[i-1], dp[i-2]+w[i-1]);
    }
    return 0;
}