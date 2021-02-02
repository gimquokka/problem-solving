//G개의 탑승구 (G,P 100,000)
//P개의 비행기 예정, i번째 비행기는 1번부터 g(i)번 탑승구 중 하나에 도킹해야 함
//도킹하지 않은 탑승구에만 도킹할 수 있음
//도킹할 곳이 없어진 시점에서 공항의 운행을 중지함
//도킹할 수 있는 최대 비행기 수를 출력
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    int G, P;
    cin >> G >> P;
    vector<int> g(P+1);
    map<int,int> m;
    for (int i=1; i<P+1; i++) {
        cin >> g[i];
    }
    
    return 0;
}