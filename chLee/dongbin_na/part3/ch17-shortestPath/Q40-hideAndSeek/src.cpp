// 숨바꼭질
#include <iostream>
#include <vector>
#include <utility>
#include <queue>
#include <algorithm>

using namespace std;
#define INF 987654321

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

int main() {
    int n,m;
    cin >> n >> m;
    vector<vector<int>> map(n+1, vector<int>(0));
    vector<int> visit(n+1);
    for (int j=1; j<n+1; j++) {
        visit[j] = INF;
    }
    for (int i=0; i<m; i++) {
        int a,b;
        cin >> a >> b;
        map[a].push_back(b);
        map[b].push_back(a);
    }

    priority_queue<pair<int,int>> q;
    visit[1] = 0;
    q.push({visit[1],1});
    
    while(!q.empty()) {
        int ccost = -q.top().first;
        int cnode = q.top().second;
        q.pop();
        for (auto nnode : map[cnode]) {
            if (visit[nnode] > ccost+1) {
                visit[nnode] = ccost + 1;
                q.push({-visit[nnode], nnode});
            }
        }
    }

    int max = 0;
    int firstInd = 0;
    int cnt = 0;
    for (int i=visit.size()-1; i>0; i--) {
        if (max < visit[i]) {
            max = visit[i];
            firstInd = i;
            cnt = 1;
        } else if (max == visit[i]) {
            cnt ++;
            firstInd = i;
        }
    }

    cout << firstInd << " ";
    cout << max << " ";
    cout << cnt << " ";


    return 0;
}