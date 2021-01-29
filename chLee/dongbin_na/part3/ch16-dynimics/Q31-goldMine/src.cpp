#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    int T;
    cin >> T;
    while (T--) {
        int n,m;
        cin >> n >> m;
        vector<vector<int>> mine(n+1, vector<int>(m+1));
        vector<vector<int>> dp(n+1, vector<int>(m+1));
        
        for (int i=1; i<n+1; i++) {
            for (int j=1; j<m+1; j++) {
                cin >> mine[i][j];
                if (j==1) {
                    dp[i][j] = mine[i][j];
                }
            }
        }

        int MAX = 0;
        for (int j=2; j<m+1; j++) {
            for (int i=1; i<n+1; i++){
                if (i==1) {
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]);
                } else if (i==m) {
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]);
                } else {
                    dp[i][j] = max({dp[i][j-1], dp[i-1][j-1], dp[i+1][j-1]});
                }        
                dp[i][j] += mine[i][j];
                if (j==m) {
                    MAX = max(MAX, dp[i][j]);
                }
            }
        }
        
        cout << MAX << endl;
    }
    return 0;
}