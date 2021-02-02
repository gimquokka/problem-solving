//행성터널
//N개의 행성, 이를 연결하는 터널
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <cmath>

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
    int n;
    cin >> n;
    priority_queue<pair<int,pair<int,int>>> e;
    vector<pair<int,int>> X;
    vector<pair<int,int>> Y;
    vector<pair<int,int>> Z;
    vector<int> parent;
    for (int i=0; i<n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        X.push_back({a,i});
        Y.push_back({b,i});
        Z.push_back({c,i});
        parent.push_back(i);
    }
    sort(X.begin(), X.end(), less<>());
    sort(Y.begin(), Y.end(), less<>());
    sort(Z.begin(), Z.end(), less<>());

    for (int i=1; i<n; i++) {
        e.push({-(X[i].first-X[i-1].first), {X[i].second, X[i-1].second}});
        e.push({-(Y[i].first-Y[i-1].first), {Y[i].second, Y[i-1].second}});
        e.push({-(Z[i].first-Z[i-1].first), {Z[i].second, Z[i-1].second}});
    }

    int cost = 0;
    while(!e.empty()) {
        int ca = e.top().second.first;
        int cb = e.top().second.second;
        int cl = -e.top().first;
        e.pop();
        if (find_s (parent, ca) != find_s (parent, cb)) {
            uni(parent, ca, cb);
            cost += cl;
        }
    }

    cout << cost << endl;
    return 0;
}