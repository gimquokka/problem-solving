#include <iostream>
#include <vector>

using namespace std;

int find_parent(vector<int>& v, int x) {
    if (v[x] != x) {
        v[x] = find_parent(v, v[x]);
    } 
    return v[x];
}

void union_parent(vector<int>& v, int a, int b) {
    a = find_parent(v, a);
    b = find_parent(v, b);
    if (a < b) {
        v[b] = a;
    } else {
        v[a] = b;
    }
}

int main() {
    int N,M;
    cin >> N >> M;
    vector<int> parent(N+1);
    for (int i=0; i<N+1; i++) {
        parent[i] = i;
    }
    while (M--) {
        int x,a,b;
        cin >> x >> a >> b;
        switch (x) {
            case 0: //union
                union_parent(parent, a, b);
                break;
            case 1: //find
                if (find_parent(parent, a) == find_parent(parent, b)) {
                    cout << "YES" << endl;
                } else {
                    cout << "NO" << endl;
                }
                break;
        }
    }
    return 0;
}