#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define mod 796796
int main () {
    int N,M;
    cin >> N >> M;

    vector<int> dp(M+1);
    vector<int> p(N);
    for (int i=0; i<N; i++) {
        cin >> p[i];
    }
    for (int i=1; i<=M; i++) {
        dp[i] = 987654321;
    }
    
    sort(p.begin(), p.end());

    dp[0] = 0;
    for (int i=0; i<N; i++) {
        for (int j=p[i]; j<=M; j++) {
            dp[j] = min(dp[j], dp[j-p[i]]+1);
        }
    }

    if (dp[M] == 987654321) {
        cout << -1;
    } else {
        cout << dp[M];
    }

    return 0;
}