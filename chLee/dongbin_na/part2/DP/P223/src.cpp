#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define mod 796796

int dp[1001];
int main () {
    int N;
    cin >> N;

    dp[0] = 1;
    dp[1] = 1;
    for (int i=2; i<=N; i++) {
        dp[i] = (dp[i-1] + dp[i-2]*2)%mod;
    }

    cout << dp[N];

    return 0;
}