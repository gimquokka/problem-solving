#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    /* 시도1 - 잘못된 풀이
    vector<int> p(N);
    vector<bool> dp;
    for (int i=0; i<N; i++) {
        cin >> p[i];
    }
    sort(p.begin(), p.end());

    dp.push_back(true); //dp[0] = true;
    int num = 1; //dp[num] 판별
    while (true) {
         dp.push_back(false); //dp[num] = false
         for (int i=0; i<N; i++) {
             if (p[i] > num) break;
             dp[num] = dp[num-p[i]];
             if (dp[num]) {
                 break;
             }
         }
         num++;
    }
    */

   /*공식 답*/
   vector<int> arr;
   for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        arr.push_back(x);
    }

    sort(arr.begin(), arr.end());

    int target = 1;
    for (int i = 0; i < N; i++) {
        // 만들 수 없는 금액을 찾았을 때 반복 종료
        if (target < arr[i]) break;
        target += arr[i];
    }

    // 만들 수 없는 금액 출력
    cout << target << '\n';
    return 0; 
}