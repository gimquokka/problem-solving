#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
    int n;
    cin >> n;
    vector<vector<int>> t(n);
    vector<vector<int>> dp(n);
    for (int i=0; i<n; i++) {
        for (int j=0; j<i+1; j++) {
            int tmp;
            cin >> tmp;
            t[i].push_back(tmp);
        }
    }
    dp[0].push_back(t[0][0]);

    int MAX = 0;
    for (int i=1; i<n; i++) {
        for (int j=0; j<i+1; j++) {
            int num;
            if (j==0) {
                num = dp[i-1][j] + t[i][j];
            } else if (j==i) {
                num = dp[i-1][j-1] + t[i][j];
            } else {
                num = max(dp[i-1][j], dp[i-1][j-1]) + t[i][j];
            }
            dp[i].push_back(num);
            if (i==n-1) {
                MAX = max(MAX, dp[i][j]);
            }
        }
    }
    
    cout << MAX << endl;
    return 0;
}