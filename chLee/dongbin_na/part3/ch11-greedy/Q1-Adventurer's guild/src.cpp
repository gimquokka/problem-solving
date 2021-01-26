#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> x(N);
    for (int i=0; i<N; i++) {
        cin >> x[i];
    }
    sort(x.begin(), x.end());
    
    /* 잘못된 풀이 - 조건을 잘 확인하지 않음
    int cnt=0;
    while (!x.empty()) {
        int tmp = x[x.size()-1];
        cnt ++;
        while (tmp-- && !x.empty()) {
            x.pop_back();
        }
    }
    */

    /* 옳은 풀이 */
    int cnt = 0;
    int members = 0;
    for (int i=0; i<x.size(); i++) {
        members ++; //멤버 추가
        if (members >= x[i]) { //그룹 내 최고 공포도 <= 멤버 수 이면 그루핑 완료
            cnt ++;
            members = 0;
        }
    }
    cout << cnt << endl;
    

    return 0;
}