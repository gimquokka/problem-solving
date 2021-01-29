//병사 배치하기
//가장 긴 감소하는 부분수열의 길이 찾기
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    //1로 초기화 안해서 틀림 ㅋ
    vector<int> dp(N,1); //dp[i] : i번째 숫자를 마지막으로 하는 최장 부분수열 길이
    for (int i=1; i<N; i++) {
        int MAX = dp[i];
        for (int k=0; k<i; k++) {
            if (v[i] < v[k]) {
                MAX = max(MAX, dp[k]+1);
            }
        }
        dp[i] = MAX;
    }

    sort(dp.begin(), dp.end());
    cout << N-dp[dp.size()-1] << endl;
    return 0;
}