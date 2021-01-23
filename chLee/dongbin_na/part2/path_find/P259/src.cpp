#include <iostream>
#include <algorithm>

using namespace std;

#define INF 987654321

int dp[101][101];

int main() {
    int N, M;
    cin >> N >> M;
    for (int i=1; i<N+1; i++) {
        for (int j=1; j<N+1; j++) {
            if (i==j) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = INF;
            }
        }
    }

    while(M--) {
        int tmpV1, tmpV2;
        cin >> tmpV1 >> tmpV2;
        dp[tmpV2][tmpV1] = 1;
        dp[tmpV1][tmpV2] = 1;
    }

    for (int k=1; k<N+1; k++) {
        for (int a=1; a<N+1; a++) {
        for (int b=1; b<N+1; b++) {
            dp[a][b] = min(dp[a][k]+dp[k][b], dp[a][b]);
        }
        }
    }

    int X,K;
    cin >> X >> K;

    if (dp[1][K] == INF || dp[K][X] == INF) {
        cout << -1;
    } else {
        cout << dp[1][K] + dp[K][X];
    }
    return 0;
}