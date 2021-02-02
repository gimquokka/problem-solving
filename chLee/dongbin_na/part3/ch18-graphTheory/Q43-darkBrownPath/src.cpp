//어두운 길
//N개의 집, M개의 도로
//0번부터 N-1번까지의 번호로 구분됨
//도로의 길이 = 가로등 비용
//임의의 두 집사이의 경로에 가로등 켤거임
//모든 집 사이의 경로에 가로등을 켤건데, 비용이 최소가 되면 좋겠다!!
#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int find_s (vector<int>& v, int a) {
    if (v[a] != a) {
        v[a] = find_s (v, v[a]);
    }
    return v[a];
}

void uni (vector<int>& v, int a, int b) {
    int A = find_s (v, a);
    int B = find_s (v, b);
    if (A < B) {
        v[B] = A;
    } 
    if (A > B) {
        v[A] = B;
    }
}

int main() {
    int n,m;
    cin >> n >> m;
    priority_queue<pair<int, pair<int,int>>> e;
    vector<int> parent(n);
    for (int i=0; i<n; i++) {
        parent[i] = i;
    }
    //vector<vector<int>> graph(n, vector<int>());
    //vector<int> E(m);
    int len = 0;
    for (int i=0; i<m; i++) {
        int x,y,z;
        cin >> x >> y >> z;
        e.push({-z,{x,y}});
        len += z;
    }

    int wholeCost = 0;
    while(!e.empty()) {
        int ca = e.top().second.first;
        int cb = e.top().second.second;
        int cl = -e.top().first;
        e.pop();
        if (find_s (parent, ca) != find_s (parent, cb)) {
            uni(parent, ca, cb);
            wholeCost += cl;
        }
    }

    cout << len - wholeCost << endl;

    return 0;
}