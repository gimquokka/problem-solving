#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;

int find_parent(int* v, int x) {
    if (v[x] != x) {
        v[x] = find_parent(v, v[x]);
    } 
    return v[x];
}

void union_parent(int* v, int a, int b) {
    a = find_parent(v, a);
    b = find_parent(v, b);
    if (a < b) {
        v[b] = a;
    } else {
        v[a] = b;
    }
}

class CC {
    public:
        int cost;
        int a;
        int b;
        CC (int c, int a, int b) {
            this->cost = c;
            this->a = a;
            this->b = b;
        }
        bool operator < (CC &a) {
            return this->cost < a.cost;
        }
};

int main() {
    int N; //노드 개수
    int M; //간선 개수 - 무방향
    cin >> N >> M;
    vector<CC> edges;
    int* parent = new int[N+1];

    //parent 초기화
    for (int i=1; i<N+1; i++) {
        parent[i] = i;
    }
    //간선 리스트 초기화
    while (M--) {
        int a,b,cost;
        cin >> a >> b >> cost;
        edges.push_back(CC(cost,a,b));
    }
    sort(edges.begin(), edges.end());

    int result = 0;
    int last;
    for (int i=0; i<edges.size(); i++) {
        int a = edges[i].a;
        int b = edges[i].b;
        int cost = edges[i].cost;

        if (find_parent(parent, a) != find_parent(parent, b)) {
            union_parent(parent,a,b);
            result += cost;
            last = cost;
        }
    }

    cout << result-last << endl;

    return 0;
}