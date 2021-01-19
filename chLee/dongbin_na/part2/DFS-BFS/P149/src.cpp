#include <iostream>
#include <queue>
#include <utility>
#include <string>
using namespace std;

string map[1001];
bool visit[1001][1001];
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

// bfs로 풀장 (물론 dfs로도 풀 수 있음)
int main() {
    int N,M;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> map[i];
    }

    //이차원 배열에 map을 저장했으므로, 인접 행렬을 이용한 bfs다
    //현재 노드의 상하좌우 중 값이 '0'인 노드를 찾아야 함
    int cnt = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            //탐색 시작 node
            if (visit[i][j]) continue;
            if (map[i][j] == '1') continue;
            visit[i][j] = true;
            cnt++;
            queue<pair<int,int>> q;
            q.push({i,j});
            while (!q.empty()) {
                int cx = q.front().first;
                int cy = q.front().second;
                q.pop();
                for (int n=0; n<4; n++) {
                    int nx = cx + dx[n];
                    int ny = cy + dy[n];
                    if (visit[nx][ny]) continue;
                    if (!(0<=nx&&nx<N&&0<=ny&&ny<M)) continue;
                    if (map[nx][ny] == '0'){
                        q.push({nx,ny});
                        visit[nx][ny] = true;
                    }
                }
            }
        }
    }    

    cout << cnt;

    return 0;
}