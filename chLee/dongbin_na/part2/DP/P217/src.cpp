#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int X;
int dp[30001]; //i를 만드는데 필요한 최소 횟수

int main() {
    cin >> X;
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    for (int i=4; i<=X; i++) {
        int min = dp[i-1];
        if (i%5 == 0) {
            min = min>dp[i/5]?dp[i/5]:min;
        }
        if (i%3 == 0) {
            min = min>dp[i/3]?dp[i/3]:min;
        } 
        if (i%2 == 0) {
            min = min>dp[i/2]?dp[i/2]:min;
        }        
        dp[i] = min + 1;
    }

    cout << dp[X] << endl;
    
    return 0;
}