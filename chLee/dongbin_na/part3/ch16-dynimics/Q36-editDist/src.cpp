//편집 거리(distance)
//두 문자열 A,B -> A를 편집하여 B로 만들고자 한다
//A를 편집할 땐
//- 삽입(insert): 특정한 위치에 하나의 문자를 삽입
//- 삭제(Remove): 특정한 위치에 있는 하나의 문자를 삭제합니다.
//- 교체(Replace): 특정한 위치에 있는 하나의 문자를 다른 문자로 교체합니다.
//편집거리 = A를 편집하여 B로 만들기 위한 연산의 수
//최소 편집거리 계산!!
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

/*틀린 답
int samecnt(string A, string B) {
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    int i=0, j=0;
    int cnt=0;
    while (i<A.size() && j<B.size()) {
        if (A[i] == B[j]) {
            cnt ++;
            i++;
            j++;
        } else if (A[i] < B[j]) {
            i++;
        } else {
            j++;
        }
    }
    return cnt;
}*/

/* official 답 */
// 최소 편집 거리(Edit Distance) 계산을 위한 다이나믹 프로그래밍
int editDist(string str1, string str2) {
    int l1 = str1.size();
    int l2 = str2.size();
    vector<vector<int>> dp(l1+1, vector<int>(l2+1));
    for (int i=0; i<l1+1; i++) {
        dp[i][0] = i;
    }
    for (int j=0; j<l2+1; j++) {
        dp[0][j] = j;
    }

    for (int i=1; i<l1+1; i++) {
        for (int j=1; j<l2+1; j++) {
            if (str1[i-1] == str2[j-1]) {
                dp[i][j] = dp[i-1][j-1];
            } else {
                dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
        }
    }

    return dp[l1][l2];
}


int main(void) {
    string A;
    string B;
    cin >> A >> B;

    /* 틀린 답
    int same = samecnt(A,B);
    cout << abs((double)B.size()-same) << endl;
    */
    cout << editDist(A,B);
    return 0;
}