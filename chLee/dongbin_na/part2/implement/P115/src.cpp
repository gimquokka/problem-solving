#include <iostream>
#include <algorithm>

using namespace std;

int dx[] = {-2,2,-2,2,-1,1,-1,1};
int dy[] = {1,1,-1,-1,-2,-2,2,2};
bool inmap(int x, int y) {
    return 0<=x && x<8 && 0<=y && y<8;
}
int main() {
    char c[2];
    scanf("%s", c);
    int cx = c[0] - 97;
    int cy = c[1] - 49;
    int cnt = 0;
    for (int i=0; i<8; i++) {
        int nx = cx + dx[i];
        int ny = cy + dy[i];
        if (inmap(nx,ny)) {
            cnt ++;
        }
    }

    cout << cnt << endl;
    return 0;
}