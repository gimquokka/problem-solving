#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

//방향 오,아,왼,위
//L이면 index-1
//D이면 index+1
int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

// 1초, 128MB
int main() {
    int N,K; //map크기, 사과 갯수
    cin >> N >> K;
    vector<vector<int> > m(N+1, vector<int>(N+1));
    for (int i=0; i<K; i++) {
        int x,y;
        cin >> x >> y;
        m[x][y] = 1; //사과
    }

    int L; //뱀의 방향 변환 횟수
    cin >> L;
    map<int,char> dir;
    for (int i=0; i<L; i++) {
        int X; //게임시작 X초 후, 
        char C; //'L'왼쪽 'D'오른쪽 으로 회전
        cin >> X >> C;
        dir[X+1] = C;
    }

    //t=0일때, 뱀 머리위치 1,1 , 꼬리위치 1,1 , 향한 방향 0 (오른쪽)
    vector<pair<int,int>> pos = {{1,1}}; //마지막원소=머리위치, 첫원소=꼬리위치
    int h_dir = 0;
    
    for (int t=1; ;t++) { //시간이 1초가 지나면
        //t초에 머리방향이 바뀌어야 한다면 바꾸기
        if (dir.find(t) != dir.end()) {
            if (dir[t] == 'L') {
                h_dir -= 1;
            }
            if (dir[t] == 'D') {
                h_dir += 1;
            }
            h_dir %= 4;
        }
        //다음 머리가 향할 곳을 head에 저장
        pair<int,int> head = *(pos.end()-1);
        head.first += dx[h_dir];
        head.second += dy[h_dir];

        //만약 head지점이 벽이라면 t를 출력하고 break
        //만약 head지점이 pos에 포함되어 있다면 t출력 후 break
        //벽이 아니라면 pos에 head를 push
        if (head.first<1 || head.first>N || head.second<1 || head.second>N) {
            cout << t << endl;
            break;
        } else if (find(pos.begin(), pos.end(), head) != pos.end()){
            cout << t << endl;
            break;
        } else {
            pos.push_back(head);
        }

        //head지점이 사과라면 apple_flag = true
        bool apple_flag = false;
        if (m[head.first][head.second] == 1) {
            apple_flag = true;
        }

        //apple_flag가 false일 때만 꼬리 지우기
        if (!apple_flag) {
            pos.erase(pos.begin());
        }
    }

    return 0;
}