// NxM크기의 연구소 (in range [3,8])
// 바이러스의 확산을 막기 위한 벽 - 바이러스는 2에서 상하좌우로 확산
// 0 빈칸, 1벽, 2바이러스
// 세워야 하는 벽은 총 3개
// 안전영역=바이러스가 퍼질 수 없는 곳
// 안전영역의 최대값을 구하여라

#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};

//벽을 실제로 놓고, 직접 바이러스 퍼뜨려서, 안전지대 세보자!
int main() {
    int n,m;
    cin >> n >> m;
    vector<vector<int>> map(n+1, vector<int>(m+1));
    vector<pair<int,int>> wall; //벽이 들어갈 수 있는 자리
    queue<pair<int,int>> vir;
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<m+1; j++) {
            cin >> map[i][j];
            if (map[i][j] != 1 && map[i][j] != 2) {
                wall.push_back({i,j});
            }
            if (map[i][j] == 2) {
                vir.push({i,j});
            }
        }
    }

    //벽을 놓을 수 있는 경우의 수 C(n*m, 3)
    vector<int> sel_wall(wall.size());
    sel_wall[0] = 1;
    sel_wall[1] = 1;
    sel_wall[2] = 1;
    
    int result = 0;
    do {
        vector<vector<int>> tmap(map);

        //벽 넣기
        for (int i=0; i<wall.size(); i++) {
            if (sel_wall[i] == 1) {
                tmap[wall[i].first][wall[i].second] = 1;
            }
        }

        //바이러스 퍼뜨리기
        queue<pair<int,int>> q(vir);
        while (!q.empty()) {
            int cx = q.front().first;
            int cy = q.front().second;
            q.pop();

            for (int i=0; i<4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                //맵 밖
                if (nx<1 || nx>n || ny<1 || ny>m) continue;
                //바이러스 or 벽
                if (tmap[nx][ny] == 2 || tmap[nx][ny] == 1) continue;
                //오직 빈 칸 일때만
                tmap[nx][ny] = 2;
                q.push({nx,ny});
            }
        }

        //count safe_zone
        int safe_zone = 0;
        for (int i=1; i<n+1; i++) {
            for (int j=1; j<n+1; j++) {
                if (tmap[i][j] == 0) {
                    safe_zone++;
                }
            }
        }
        result = max(result, safe_zone);
    //dfs대신 permutaition함수 사용
    //ex. 1 2 3 4-> 1 2 4 3 -> 1 3 2 4 -> 1 3 4 2 
    } while(prev_permutation(sel_wall.begin(), sel_wall.end()));

    cout << result << endl;
    return 0;
}

//시간 복잡도는 O(N^4)인데
//N이 매우 작아서 가능한 풀이 !
//-컴퓨터는 1초에 약 1억번의 연산