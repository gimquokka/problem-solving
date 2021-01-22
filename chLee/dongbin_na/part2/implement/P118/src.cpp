#include <iostream>
#include <algorithm>

using namespace std;

//0-N, 1-E, 2-S, 3-W
int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

int map[50][50]; //1->바다, 0->육지
int visit[50][50];

int main() {
    int N,M; //map size
    cin >> N >> M;

    int A,B,d; //start pos, dir
                // dir - 0(N),1(E),2(S),3(W)
    cin >> A >> B >> d;
    
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> map[i][j];
        }
    }

    int c_dir = d;
    int cx = A;
    int cy = B;
    int flag = 0;
    int cnt = 1;
    while (true) {
        //1. 방향 정하기
        c_dir -= 1;
        c_dir %= 4;
        
        int nx = cx + dx[c_dir];
        int ny = cy + dy[c_dir];

        if (visit[nx][ny] == 0 && map[nx][ny] == 0) {
            visit[nx][ny] = 1;
            cx = nx;
            cy = ny;
            flag = 0;
            cnt ++;
        } else {
            flag ++;
        }

        if (flag == 4) {
            nx = cx - dx[c_dir];
            ny = cy - dy[c_dir];
            if (map[nx][ny] == 0) {
                cx = nx;
                cy = ny;
            } else {
                break;
            }
            flag = 0;
        }


    }

    cout << cnt ;
    return 0;
}