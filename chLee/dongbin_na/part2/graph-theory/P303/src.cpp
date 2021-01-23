#include <iostream>
#include <queue>
#include <vector>
#include <utility>
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

vector<int> graph[501];
int time[501];
int result[501];
int indegree[501];

int main() {
    int V; //노드 개수
    cin >> V;
    for (int i=1; i<V+1; i++) {
        cin >> time[i];
        result[i] = time[i];
        while (true) {
            int tmp;
            cin >> tmp;
            if (tmp == -1) break;
            graph[tmp].push_back(i);
            indegree[i] += 1;
        }
    }

    queue<int> q;
    for (int i=1; i<V+1; i++) {
        if (indegree[i] == 0)
            q.push(i);
    }

    //위상 정렬
    while (!q.empty()) {
        int current = q.front();
        q.pop();
        for (auto e : graph[current]) {
            result[e] = max(result[e], result[current]+time[e]);
            indegree[e] -= 1;
            if (indegree[e] == 0) {
                q.push(e);
            }
        }
    }
    
    for (int i=1; i<V+1; i++) {
        cout << result[i] << endl;
    }



    return 0;
}