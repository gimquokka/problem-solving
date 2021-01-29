//N명 성적이 없어짐
//비교 결과만 있음
//A<B라면, A->B인 간선 그리기
//순위를 정확히 알 수 있는 학생 수 계산하기
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define INF 987654321

int main() {
    int n,m;
    cin >> n >> m;
    //vector<int> rank[501];
    //vector<int> ind(n+1);
    vector<vector<int>> dp(n+1, vector<int>(n+1));
    for (int i=1; i<n+1; i++) {
        for (int j=1; j<n+1; j++) {
            dp[i][j] = INF;
        }
        dp[i][i] = 0;
    }
    for (int i=0; i<m; i++) {
        int a,b;
        cin >> a >> b;
        dp[a][b] = 1;
        //rank[a].push_back(b);
        //ind[b] += 1;
    }

    for (int node=1; node<n+1; node++) {
        for (int a=1; a<n+1; a++) {
            for (int b=1; b<n+1; b++) {
                dp[a][b] = min(dp[a][b], dp[a][node]+dp[node][b]);
            }
        }
    }

    int result = 0;
    for (int i=1; i<n+1; i++) {
        int cnt = 0;
        for (int j=1; j<n+1; j++) {
            if (dp[i][j] == INF && dp[j][i] == INF) continue;
            cnt ++;
        }
        if (cnt == n) 
            result += 1;
    }
    cout << result << endl;

    /* 잘못푼거요...
    // 위상정렬
    int numExact = 0;
    queue<int> q;
    for (int i=1; i<n+1; i++) {
        if (ind[i] == 0) {
            q.push(i);
        }
    }

    while (!q.empty()) {
        int c = q.front();
        q.pop();
        for (auto e : rank[c]) {
            ind[e] -= 1;
            if (ind[e] == 0) {
                q.push(e);
            }
        }
    }
    
    cout << numExact << endl;
    */
    return 0;
}