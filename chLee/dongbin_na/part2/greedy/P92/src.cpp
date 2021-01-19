#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
    int n,m,k;
    cin >> n >> m >> k;
    vector<int> v(n);
    for (int i=0; i<n; i++) {
        cin >> v[i];
    }

    int sum = 0;
    sort(v.begin(), v.end(), greater<>());
    
    //어차피 가장 큰 값(first)과 두 번째로 큰 값(second)만 쓰임
    //각 값이 몇 번 쓰이는지만 알면 됨 (fcnt, scnt)
    int first = v[0];
    int fcnt = (m/(k+1))*k + m%(k+1); //개수가 왜 이런지는 잘 생각해보면 바로 나옴
    int second = v[1];
    int scnt = m/(k+1);
    sum += first*fcnt + second*scnt;

    cout << sum << endl;
    return 0;
}

