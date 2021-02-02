//아기상어
//NxN크기의 공간에 물고기 M마리와 아기상어 1마리가 이따!!
//모든 물고기는 크기를 가지고 있고, 아기상어는 크기 2!!!
//자신의 크기보다 큰 물고기 있는 칸은 못지나감
//자신의 크기보다 작은 물고기만 먹을 수 있다
// 이동 결정
// 1. 더 이상 먹을 수 있는 물고기가 없다면 엄마상어에게 도움 요청
// 2. 먹을 수 있는 고기가 1마리면 물고기 먹으러 감
// 3. 1마리 이상이면 거리가 가장 가까운 물고기 먹으러 감
//  - 거리 = 지나야하는 칸의 최솟값
//  - 거리가 동일하다면, 가장위에있는 물고기, 가장 왼쪽에 있는 물고기 (x,y 작은 순서)
//이동에 1초가 걸림
//자신의 크기와 같은 수의 물고기를 먹으면 크기 1 증가
//엄마도움없이 어디까지 클 수 있을까?
#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int dx[] = {-1, 0, 0, 1}; //위 왼 오 아
int dy[] = {0, -1, 1, 0};

int main() {
    int size_shark = 2; //아기상어 사이즈
    pair<int,int> pos;

    int N;
    cin >> N;
    vector<vector<int>> m(N, vector<int>(N));
    //priority_queue<FISH> fish; //{ {x,y}, size }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> m[i][j];
            if (m[i][j] == 9) {
                pos = {i,j};
                m[i][j] = 0;
            }
        }
    }
    int result_time = 0;
    int eat_cnt = 0;
    while(true) { //pos이 한 번 바뀔 때 마다 함
        vector<vector<int>> visit(N, vector<int>(N,-1));
        priority_queue<pair<int, pair<int,int>>, vector<pair<int, pair<int,int>>>, greater<pair<int, pair<int,int>>>> q; //{ {x,y}, dist }
        q.push({0, pos});
        visit[pos.first][pos.second] = 0;

        bool doEat = false; //먹었니?
        // 먹을 수 있는걸 발견하면 망설이지말고 먹어!!
        while (!q.empty() && !doEat) {
            int cx = q.top().second.first;
            int cy = q.top().second.second;
            int cd = q.top().first;
            q.pop();
            for (int i=0; i<4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                int nd = cd + 1;
                if (nx<0 || nx>=N || ny<0 || ny>=N) continue;
                if (visit[nx][ny] == -1) {
                    if (m[nx][ny] <= size_shark){ //지나갈 수 있어!!
                        if (m[nx][ny]!=0 && size_shark > m[nx][ny]) { //물고기 있고, 먹을 수 있어!!
                            pos = {nx,ny};
                            m[nx][ny] = 0;
                            result_time += nd; //이만큼 이동한 거만큼 시간 쓴 거임
                            eat_cnt++;
                            if (eat_cnt == size_shark) {
                                eat_cnt = 0;
                                size_shark += 1;
                            }
                            doEat = true; //먹었으면 다시 그 자리부터 bfs돌려야지
                            break;
                        } else { //먹을 수 없어 ㅠ
                            visit[nx][ny] = nd;
                            q.push({nd, {nx,ny}});
                        }
                    }
                }
            }
        }
        
        if (!doEat) { //탐색이 끝났는데도 못먹었으면 엄마 콜하셈 ㅋ
            cout << result_time << endl;
            return 0;
        }
        
    }

    return 0;
}