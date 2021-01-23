#include <iostream>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;
#define INF 987654321

vector<pair<int,int>> v[30001]; //인접 리스트
int dist[30001]; //최단 거리 테이블


int main() {
    int N, M, C;
    cin >> N >> M >> C;

    for(int i=1; i<=N; i++) {
        dist[i] = INF;
    }

    for (int i=0; i<M; i++) {
        int X,Y,Z;
        cin >> X >> Y >> Z;
        v[X].push_back({Y,Z});
    }

    priority_queue<pair<int,int>> q;
    q.push({0, C});
    dist[C] = 0;

    while (!q.empty()) {
        int cc = q.top().first;
        int cv = q.top().second;
        q.pop();

        if (dist[cv] < cc)  continue; // 이거 왜 하는지 모르겠음...

        for (auto e : v[cv]) {
            int nv = e.first;
            int nc = cc + e.second;
            if (dist[nv] > nc) {
                dist[nv] = nc;
                q.push({nc, nv});
            }
        }
    }

    int max = 0;
    int cnt = 0;
    for (int i=1; i<=N; i++) {
        int t = dist[i];
        if (t != INF) {
            cnt ++;
            max = max<t?t:max;
        }
    }

    cout << cnt-1 << " " << max;

    return 0;
}