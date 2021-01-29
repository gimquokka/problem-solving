//정렬된 배열에서 특정 수의 개수 구하기
//N개의 원소 - 오름차순 수열
//x가 등장하는 횟수 구하기
//O(logN)으로 풀기
#include <iostream>
#include <vector>

using namespace std;

int bs (vector<int>& v, int x) {
    int cnt = -1;
    int s = 0;
    int e = v.size()-1;
    while (s <= e) {
        int mid = (s+e)/2;
        if (v[mid] == x) {
            for(int i=0; ;i++) {
                if (v[mid+i] == x) cnt ++;
                else break;
            }
            for(int i=0; ;i--) {
                if (v[mid+i] == x) cnt ++;
                else break;
            }
            return cnt;
        }
        if (v[mid] > x) {
            e = mid-1;
        } else if (v[mid] < x) {
            s = mid+1;
        }
    }
    return cnt;
}

int main () {
    int N,x;
    cin >> N >> x;
    vector<int> v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    cout << bs(v, x) << endl;
    return 0;
}