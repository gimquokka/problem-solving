//못생긴 수
//: 2,3,5만을 소인수로 갖는 수 (1은 못생긴 수)
//n번째 못생긴 수를 찾으시오~
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool dp[1001]; //i가 못생긴 수 인지 확인
int ugly[1000];

int main() {
    int n;
    cin >> n;

    // 2배, 3배, 5배를 위한 인덱스
    int i2 = 0, i3 = 0, i5 = 0;
    // 처음에 곱셈 값을 초기화
    // 2의배수, 3의배수, 5의 배수
    // 공배수는 동시에 처리되니까 걱정 ㄴㄴ
    int next2 = 2, next3 = 3, next5 = 5;

    ugly[0] = 1; // 첫 번째 못생긴 수는 1
    // 1부터 n까지의 못생긴 수들을 찾기
    for (int l = 1; l < n; l++) {
        // 가능한 곱셈 결과 중에서 가장 작은 수를 선택
        ugly[l] = min(next2, min(next3, next5));
        // 인덱스에 따라서 곱셈 결과를 증가
        // 한꺼번에 올라갈수도 있어용
        if (ugly[l] == next2) {
            i2 += 1;
            next2 = ugly[i2] * 2;
        }
        if (ugly[l] == next3) {
            i3 += 1;
            next3 = ugly[i3] * 3;
        }
        if (ugly[l] == next5) {
            i5 += 1;
            next5 = ugly[i5] * 5;
        }
    }

    // n번째 못생긴 수를 출력
    cout << ugly[n - 1] << '\n';

    /* 이것도 O(N)아닌가?
    dp[1] = true;
    int cnt = 1;
    for (int i=2; ; i++) {
        dp[i] = true;
        if (i%2!=0 && i%3!=0 && i%5!=0) {
            dp[i] = false;
        } else {
            if (i%2==0) {
                dp[i] = dp[i]&&dp[i/2];
            }
            if (i%3==0) {
                dp[i] = dp[i]&&dp[i/3];
            }
            if (i%5==0) {
                dp[i] = dp[i]&&dp[i/5];
            }
        }
        if (dp[i]) cnt++;
        if (cnt == n) {
            cout << i << endl;
            return 0;
        }
    }
    */
    return 0;
}