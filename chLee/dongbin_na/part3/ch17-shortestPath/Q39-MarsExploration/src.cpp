//화성 탐사
#include <iostream>
#include <vector>
#include <utility>
#include <queue>

using namespace std;
#define INF 987654321

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};
bool inMap(int x, int y, int n) {
    return x>=0 && x<n && y>=0 && y<n;
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        int N;
        cin >> N;
        vector<vector<int>> map(N, vector<int>(N));
        vector<vector<int>> visit(N, vector<int>(N));
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                cin >> map[i][j];
                visit[i][j] = INF;
            }
        }

        priority_queue<pair<int,pair<int,int>>> q;
        q.push({-map[0][0], {0,0}});
        visit[0][0] = map[0][0];
        int cnt = 0;
        while(!q.empty()) {
            int ccost = -q.top().first;
            int cx = q.top().second.first;
            int cy = q.top().second.second;
            q.pop();
            cnt ++;
            for (int i=0; i<4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (!inMap(nx, ny, N)) continue;
                if (visit[nx][ny] > ccost + map[nx][ny]) {
                    visit[nx][ny] = ccost + map[nx][ny];
                    q.push({-visit[nx][ny], {nx, ny}});
                }
            }
        }
        cout << cnt << endl;
        cout << visit[N-1][N-1] << endl;
    }
    return 0;
}