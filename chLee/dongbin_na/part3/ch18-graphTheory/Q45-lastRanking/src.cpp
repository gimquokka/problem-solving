//최종 순위
//n개 팀 참가
//1번부터 n번까지 번호 매겨져 있음
//상대적인 순위가 바뀐 팀의 목록만 공개
//ex. 작년엔 13팀 순위가 6팀보다 높았는데, 이번엔 반대라면 (6, 13) 이런식으로 공개
//작년 순위 + 공개된 목록 => 올해 순위 예측하기
//1. 올 해 순위 만들수 없다면 "?"
//2. 데이터에 일관성이 없어서 순위 정할 수 없으면 "IMPOSSIBLE"
//3. 등수 정할 수 있으면 1등부터 모두 출력
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> grade(n+1); //grade[i] : i등을 한 팀의 번호 ex.grade[2]=1 -> 2등을 한 건 1팀
        for (int g=1; g<n+1; g++) {
            cin >> grade[g];
        }
        vector<vector<int>> A(n+1, vector<int>(n+1,0)); //A[i][j] = 1 : i->j
        vector<int> ind(n+1);
        for (int i=1; i<n+1; i++) {
            int t = grade[i];
            for (int j=i+1; j<n+1; j++) {
                A[t][grade[j]] = 1;
                ind[grade[j]] += 1;
            }
        }

        //아래 정보를 바탕으로 directed그래프 수정하기
        //indegree배열도 만들자
        int m;
        cin >> m;
        for (int i=0; i<m; i++) {
            int a, b;
            cin >> a >> b;
            if (A[a][b] == 1) {
                A[a][b] = 0;
                A[b][a] = 1;
                ind[b] -= 1;
                ind[a] += 1;
            } else if (A[a][b] == 0) {
                A[a][b] = 1;
                A[b][a] = 0;
                ind[a] -= 1;
                ind[b] += 1;
            }
        }

        //위상 정렬
        //중간에 0이 안나오면 IMPOSSIBLE출력
        int cnt = 0;
        bool flag = true;
        queue<int> q;
        for (int i=1; i<n+1; i++) {
            if (ind[i] == 0) {
                q.push(i);
                cnt ++;
            }
        }

        if (cnt==0) {
            flag = false;
        }


        vector<int> result;
        while (!q.empty() && flag) {
            int cv = q.front();
            q.pop();
            result.push_back(cv);
            for (int i=1; i<n+1; i++) {
                if (A[cv][i] == 1) {
                    A[cv][i] = 0;
                    ind[i] -= 1;
                    if (ind[i] == 0) {
                        q.push(i);
                    }
                }
            }
        }

        //출력
        if (result.size() == n) {
            for (auto v : result) {
                cout << v << " ";
            }
        } else {
            cout << "IMPOSSIBLE" ;
        }
        cout << endl;
        
    }
    return 0;
}