#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};
int main() {
    int n,k;
    cin >> n >> k;
    vector<vector<int>> map(n+1, vector<int>(n+1));
    queue<pair<int,pair<int,int>>> q;
    vector<pair<int,pair<int,int>>> tmp;
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<n+1; j++) {
            cin >> map[i][j];
            if (map[i][j] != 0) {
                tmp.push_back({map[i][j],{i,j}});
            }
        }
    }

    int s,x,y;
    cin >> s >> x >> y;

    sort(tmp.begin(), tmp.end());
    for (auto e : tmp) {
        q.push(e);
    }

    int time = 0;
    while(!q.empty() && time <= s) {
        time ++;
        int cnum = q.front().first;
        int cx = q.front().second.first;
        int cy = q.front().second.second;
        q.pop();

        for (int i=0; i<4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if (nx<1 || nx>n || ny<1 || ny>n) continue;
            if (map[nx][ny] == 0) {
                map[nx][ny] = cnum;
                q.push({cnum,{nx,ny}});
            }
        }
    }
    
    cout << map[x][y] << endl;


    return 0;
}