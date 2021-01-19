#include <iostream>
#include <queue>
#include <utility>
#include <string>
using namespace std;

string map[201];
bool visit[201][201];
int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

class XY {
    public:
        int x;
        int y;
        int len;
        XY(int x, int y, int len) {
            this->x = x;
            this->y = y;
            this->len = len;
        }
};

int main() {
    int N,M;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        cin >> map[i];
    }

    int len = 1;
    visit[0][0] = true;
    queue<XY> q;
    q.push(XY(0,0,len));
    while (true) {
        int cx = q.front().x;
        int cy = q.front().y;
        int clen = q.front().len;
        q.pop();
        if (cx == N-1 && cy == M-1) {
            cout << clen;
            break;
        }

        for (int n=0; n<4; n++) {
            int nx = cx + dx[n];
            int ny = cy + dy[n];
            if (visit[nx][ny]) continue;
            if (!(0<=nx&&nx<N&&0<=ny&&ny<M)) continue;
            if (map[nx][ny] == '0') continue;
            q.push(XY(nx,ny,clen+1));
            visit[nx][ny] = true;
        }
    }

    return 0;
}