#include <iostream>
#include <algorithm>

using namespace std;

int map[100][100];

int main() {
    int n,m;
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> map[i][j];
        }
    }

    for (int i=0; i<n; i++){
        sort(map[i], map[i]+m);
    }

    int max = -1;
    for (int i=0; i<n; i++) {
        if (map[i][0] > max) {
            max = map[i][0];
        }
    }

    cout << max << endl;
    return 0;
}