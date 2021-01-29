#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//i-1번쨋날까지 일한 돈을 i번째 날에 받는다고 전제 (N+1까지 체크해야함)
//dp[i]는 i번쨋날 받을 수 있는 가장 큰 금액
int dp[15+2]; 

int main() {
  int N;
  cin >> N;
  vector<int> T(N+1);
  vector<int> P(N+1);
  for (int i=1; i<N+1; i++) {
    cin >> T[i] >> P[i];
  }

  dp[0] = 0;
  dp[1] = 0; //dp[1]은 0번쨋날 까지 번 돈이니깐 무조건 0임
  for (int i=2; i<=N+1; i++) {
    //k번째 일 해서, i-1번째 까지 일을 다 끝낼 수 있으면 ( k-T[k]+1 > i )
    //k번쨋날 까지 번 돈 + P[k]를 i번쨋날 받을 수 있음
    //그 중 가장 큰 값을 dp[i]에 입력.
    for (int k=1; k<i; k++) {
      if (k+T[k]-1 < i) {
        dp[i] = max(dp[i], dp[k]+P[k]);
      }
    }
  }

  //N일 까지 한 일은 N+1일에 정산받을 수 있다(전제)
  cout << dp[N+1] << endl;
  return 0;
}