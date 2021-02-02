//N개의 여행지
//도로 - undirected
//여행계획이 주어짐 ex. 2 3 4 3
//그니깐, 두 도시사이의 path가 존재하는지 안하는지 판단해야함
//-> 같은 집합에 속해있는지 판단하는거임
#include <iostream>
#include <vector>

using namespace std;

int find(vector<int>& v, int a) {
    if (v[a] != a) {
        v[a] = find(v, v[a]);
    }
    return v[a];
}

void uni(vector<int>& v, int a, int b) {
    int A = find(v,a);
    int B = find(v,b);
    if (A < B) {
        v[B] = A;
    }
    if (A > B) {
        v[A] = B;
    }
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> plan(M);
    vector<int> parent(N+1);
    for (int i=1; i<N+1; i++) {
        parent[i] = i;
    }

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            int tmp;
            cin >> tmp;
            if (tmp == 1)
                uni(parent, i, j);
        }
    }

    for (int i=0; i<M; i++) {
        cin >> plan[i];
    }

    int tmp = find(parent, plan[0]);
    for (auto p : plan) {
        int tt = find(parent, p);
        if (tmp != tt) {
            cout << "NO" << endl;
            return 0;
        }
        tmp = tt;
    }

    cout << "YES" << endl;
    return 0;
}