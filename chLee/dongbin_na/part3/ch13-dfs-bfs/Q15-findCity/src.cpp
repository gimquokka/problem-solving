//1~N도시
//M개 간선 (directed)
//최단거리가 정확히 k인 모든 도시번호 출력
#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

int main() {
    int n,m,k,x; //도시개수, 간선개수, 거리정보, 출발도시 정보
    cin >> n >> m >> k >> x;

    vector<vector<int>> graph(n+1);
    for (int i=0; i<m; i++) {
        int a,b;
        cin >> a >> b;
        graph[a].push_back(b);
    }

    vector<int> dist(n+1);
    for (int i=1; i<n+1; i++) {
        dist[i] = 987654321;
    }
    priority_queue<pair<int,int>> q;
    dist[x] = 0;
    q.push({-dist[x], x});
    while (!q.empty()) {
        int cn = q.top().second;
        int cc = -q.top().first;
        q.pop();
        for (int i=0; i<graph[cn].size(); i++) {
            int nn = graph[cn][i];
            int nc = cc + 1;
            if (nc < dist[nn]) {
                dist[nn] = nc;
                q.push({-dist[nn], nn});
            }
        }
    }

    int cnt = 0;
    vector<int> ans;
    for (int i=0; i<dist.size(); i++) {
        if (dist[i] == k) {
            ans.push_back(i);
        }
    }
    
    if (ans.size() == 0) {
        cout << -1;
    } else {
        sort(ans.begin(), ans.end());
        for (auto e : ans) {
            cout << e << endl;
        }
    }
    return 0;
}