#include <iostream>
#include <map>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    map<int,int> m;
    for (int i=0; i<N; i++) {
        int tmp;
        cin >> tmp;
        m[tmp] += 1;
    }

    int cnt = 0;
    for (auto e : m) {
        int tmp = e.second; //K무게의 개수, m[k]
        N = N-tmp; 
        cnt += N*tmp;
    }

    cout << cnt << endl;
    return 0;
}