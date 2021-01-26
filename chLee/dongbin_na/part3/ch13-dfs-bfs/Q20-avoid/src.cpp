#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
int N;

bool inMap(int x, int y) {
    return x>=0 && x<N && y>=0 && y<N;
}
bool isOK(vector<vector<char>> tm, vector<pair<int,int>> s, vector<pair<int,int>> t) {
    for (auto xy : t) {
        int cx = xy.first;
        int cy = xy.second;
        int nx = cx;
        int ny = cy;
        //오른쪽
        while (true) {
            ny ++;
            if (!inMap(nx,ny)) break;
            if (tm[nx][ny] == 'S') {
                return false;
            }
            if (tm[nx][ny] == 'O') {
                break;
            }
        }
        //왼쪽
        nx = cx;
        ny = cy;
        while (true) {
            ny --;
            if (!inMap(nx,ny)) break;
            if (tm[nx][ny] == 'S') {
                return false;
            }
            if (tm[nx][ny] == 'O') {
                break;
            }
        }
        //위
        nx = cx;
        ny = cy;
        while (true) {
            nx --;
            if (!inMap(nx,ny)) break;
            if (tm[nx][ny] == 'S') {
                return false;
            }
            if (tm[nx][ny] == 'O') {
                break;
            }
        }
        //아래
        nx = cx;
        ny = cy;
        while (true) {
            nx ++;
            if (!inMap(nx,ny)) break;
            if (tm[nx][ny] == 'S') {
                return false;
            }
            if (tm[nx][ny] == 'O') {
                break;
            }
        }
    }
    return true;
}

int main() {
    cin >> N;
    vector<vector<char>> m(N, vector<char>(N));
    vector<pair<int,int>> t_list;
    vector<pair<int,int>> s_list;
    vector<pair<int,int>> v_list;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> m[i][j];
            if (m[i][j] == 'S') {
                s_list.push_back({i,j});
            } else if (m[i][j] == 'T') {
                t_list.push_back({i,j});
            } else {
                v_list.push_back({i,j});
            }
        }
    }
    vector<int> sel(v_list.size());
    sel[0] = 1;
    sel[1] = 1;
    sel[2] = 1;

    do {
        vector<vector<char>> tm(m);
        //벽 넣기
        for (int i=0; i<v_list.size(); i++) {
            if (sel[i] == 1) {
                tm[v_list[i].first][v_list[i].second] = 'O';
            }
        }

        if (isOK(tm,s_list,t_list)) {
            cout << "YES" << endl;
            return 0;
        }

        //벽 빼기
        for (int i=0; i<v_list.size(); i++) {
            if (sel[i] == 1) {
                tm[v_list[i].first][v_list[i].second] = 'X';
            }
        }
    } while(prev_permutation(sel.begin(), sel.end()));

    cout << "NO" << endl;
    return 0;
}