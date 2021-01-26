#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;



//TRUEorFALSE, -1orX, -1orY 반환
//X,Y는 보가 있는 위치
vector<int> isBO(int x, int y, vector<vector<int>>& m) {
    //x,y+1에 보가 있으면, true리턴
    if (find(m.begin(), m.end(), vector<int> {x,y+1,1}) != m.end()) {
        return vector<int> {true, x, y+1};
    //x,y+1에 기둥, 보 아무것도 없으면 false리턴
    } else if (find(m.begin(), m.end(), vector<int> {x,y+1,0}) == m.end()) {
        return vector<int> {true, -1, -1};
    }

    //x,y+1에 기둥이 있으면, x,y+1에대해서 재귀호출
    if (find(m.begin(), m.end(), vector<int> {x,y+1,0}) != m.end()) {
        return isBO(x,y+1,m);
    }
}

vector<vector<int>> wrong_solution(int n, vector<vector<int>> build_frame) {
    vector<vector<int>> m; //여기에 [x,y,a] 형식으로 구조물을 쌓아 나갈거임
    //n은 벽면의 길이
    //build_frame은 [x,y,a,b]형식
    for (int i=0; i<build_frame.size(); i++) {
        int x,y,a,b;
        x=build_frame[i][0];
        y=build_frame[i][1];
        a=build_frame[i][2];
        b=build_frame[i][3];
        
        if (b==1) { //설치
            if (a==0) { //기둥
                //기둥을 해당 위치에 설치하기 위해선
                //해당 구조물과 닿는 구조물이 하나 있어야 함
                //1.바닥
                if (y==0) { //y==0이면 바닥이지요
                    m.push_back(vector<int> {x,y,a});
                    continue;
                }
                //2.기둥
                //아래 기둥이 있으려면 x,y-1에 기둥이 존재해야함
                if (find(m.begin(), m.end(), vector<int> {x,y-1,0}) != m.end()) {
                    m.push_back(vector<int> {x,y,a});
                    continue;
                }
                //3.보
                //x,y 또는 x-1,y에 보가 있어야 함
                if (find(m.begin(), m.end(), vector<int> {x,y,1}) != m.end()
                || find(m.begin(), m.end(), vector<int> {x,y-1,1}) != m.end()) {
                    m.push_back(vector<int> {x,y,a});
                    continue;
                }
            } else if (a==1) { //보
                //보를 x,y에 설치하기 위해선
                //1. 기둥
                //x,y-1 혹은 x+1,y-1에 기둥이 필요함
                if (find(m.begin(), m.end(), vector<int> {x,y-1,0}) != m.end()
                || find(m.begin(), m.end(), vector<int> {x+1,y-1,0}) != m.end()) {
                    m.push_back(vector<int> {x,y,a});
                    continue;
                }
                //2. 보
                //x-1,y에설치된 보와 x+1,y에 설치된 보가 동시에 있어야 한다
                if (find(m.begin(), m.end(), vector<int> {x-1,y,1}) != m.end()
                && find(m.begin(), m.end(), vector<int> {x+1,y,1}) != m.end()) {
                    m.push_back(vector<int> {x,y,a});
                    continue;
                }
            }
        //삭제를 완성시키지 못하였다
        } else if (b==0) { //삭제
            if (a==0) { //기둥
                //x,y에 설치되어있는 기둥을 삭제하기 위해선
                //기둥위의 구조물에 따라 다르다
                //1. x,y+1에 아무것도 없다
                if (find(m.begin(), m.end(), vector<int> {x+1,y,0})==m.end()
                &&find(m.begin(), m.end(), vector<int> {x+1,y,1})==m.end()) {
                    m.erase(find(m.begin(), m.end(), vector<int> {x,y,a}));
                    continue;
                }
                //2. x,y+1에 뭔가가 있다
                //이 경우엔, 기둥들 위에 보가 있는지 없는지에 따라 다르다
                vector<int> tmp = isBO(x,y,m);
                bool isbo = tmp[0];
                //2-1. 보가 있을 때            
                //2-2. 보가 없을 때
                //는 삭제못함...
                //무시!
            } else if (a==1) { //보

            }
        }
    }
    return m;
}

/*official solution*/
bool possible(vector<vector<int> > answer) {
    for (int i = 0; i < answer.size(); i++) {
        int x = answer[i][0];
        int y = answer[i][1];
        int stuff = answer[i][2];
        if (stuff == 0) { // 설치된 것이 '기둥'인 경우
            bool check = false;
            // '바닥 위'라면 정상
            if (y == 0) check = true;
            // '보의 한 쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            for (int j = 0; j < answer.size(); j++) {
                if (x - 1 == answer[j][0] && y == answer[j][1] && 1 == answer[j][2]) {
                    check = true;
                }
                if (x == answer[j][0] && y == answer[j][1] && 1 == answer[j][2]) {
                    check = true;
                }
                if (x == answer[j][0] && y - 1 == answer[j][1] && 0 == answer[j][2]) {
                    check = true;
                }
            }
            if (!check) return false; // 아니라면 거짓(False) 반환
        }
        else if (stuff == 1) { // 설치된 것이 '보'인 경우
            bool check = false;
            bool left = false;
            bool right = false;
            // '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            for (int j = 0; j < answer.size(); j++) {
                if (x == answer[j][0] && y - 1 == answer[j][1] && 0 == answer[j][2]) {
                    check = true;
                }
                if (x + 1 == answer[j][0] && y - 1 == answer[j][1] && 0 == answer[j][2]) {
                    check = true;
                }
                if (x - 1 == answer[j][0] && y == answer[j][1] && 1 == answer[j][2]) {
                    left = true;
                }
                if (x + 1 == answer[j][0] && y == answer[j][1] && 1 == answer[j][2]) {
                    right = true;
                }
            }
            if (left && right) check = true;
            if (!check) return false; // 아니라면 거짓(False) 반환
        }
    }
    return true;
}

vector<vector<int> > solution(int n, vector<vector<int> > build_frame) {
    vector<vector<int> > answer;
    // 작업(frame)의 개수는 최대 1,000개
    for (int i = 0; i < build_frame.size(); i++) {
        int x = build_frame[i][0];
        int y = build_frame[i][1];
        int stuff = build_frame[i][2];
        int operate = build_frame[i][3];
        if (operate == 0) { // 삭제하는 경우
            // 일단 삭제를 해 본 뒤에
            int index = 0;
            for (int j = 0; j < answer.size(); j++) {
                if (x == answer[j][0] && y == answer[j][1] && stuff == answer[j][2]) {
                    index = j;
                }
            }
            vector<int> erased = answer[index];
            answer.erase(answer.begin() + index);
            if (!possible(answer)) { // 가능한 구조물인지 확인
                answer.push_back(erased); // 가능한 구조물이 아니라면 다시 설치
            }
        }
        if (operate == 1) { // 설치하는 경우
            // 일단 설치를 해 본 뒤에
            vector<int> inserted;
            inserted.push_back(x);
            inserted.push_back(y);
            inserted.push_back(stuff);
            answer.push_back(inserted);
            if (!possible(answer)) { // 가능한 구조물인지 확인
                answer.pop_back(); // 가능한 구조물이 아니라면 다시 제거
            }
        }
    }
    // 정렬된 결과를 반환
    sort(answer.begin(), answer.end());
    return answer;
}