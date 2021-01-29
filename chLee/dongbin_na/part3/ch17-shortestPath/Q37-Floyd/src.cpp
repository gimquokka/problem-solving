//n개 도시 (1<=n<=100)
//m개의 버스 (1<=m<=100000)
//각 버스마다 비용이 있음
//A->B 필요한 비용의 최솟값 구하기
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

#define INF 987654321

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> vm(n+1, vector<int>(n+1));
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<n+1; j++) {
            vm[i][j] = INF;
        }
        vm[i][i] = 0;
    }
    for (int i=0; i<m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        vm[a][b] = min(c, vm[a][b]);
    }

    for (int i=1; i<n+1; i++) {
        for (int a=1; a<n+1; a++) {
            for (int b=1; b<n+1; b++) {
                vm[a][b] = min(vm[a][b], vm[a][i]+vm[i][b]);
            }
        }
    }

    for (int a=1; a<n+1; a++) {
        for (int b=1; b<n+1; b++) {
            if (vm[a][b] == INF)
                cout << 0 << " ";
            else
                cout << vm[a][b] << " ";
        }
        cout << endl;
    }
    return 0;
}