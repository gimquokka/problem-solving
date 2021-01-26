#include <iostream>
#include <vector>
#include <utility>
using namespace std;


void rotate(vector<vector<int>>& key){
    int n = key.size();
    // https://hsdevelopment.tistory.com/298
    for (int i = 0; i < n / 2; i++){
        for (int j = i; j < n - 1 - i; j++){
            int Top = key[i][j]; // Top ← 위쪽
            
            key[i][j] = key[n-1-j][i]; // 위쪽 ← 왼쪽
            key[n-1-j][i] = key[n-1-i][n-1-j]; // 왼쪽 ← 아래쪽
            key[n-1-i][n-1-j] = key[j][n-1-i]; // 아래쪽 ← 오른쪽
            key[j][n-1-i] = Top; // 오른쪽 ← Top(위쪽)
        }
    }
}

/*
bool check(vector<vector<int>>& cplock) {
    int N = cplock.size();
    for (auto vp : cplock) {
        for (auto v : vp) {
            if (vp != )
        }
    }
    
    return true;
}
*/

bool wrong_solution(vector<vector<int>> key, vector<vector<int>> lock) {
    int M = key.size();
    int N = lock.size();
    vector<pair<int,int>> slots;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (lock[i][j]==0) {//slot
                slots.push_back({i,j});
            }
        }
    }

    for (int i=-M+1; i<N; i++) {
    for (int j=-M+1; j<N; j++) { //i,j에 key의 0,0이 위치했을 때,
        int numRotate = 4;
        while(numRotate--) {
            rotate(key);
            int cnt = 0;//채워진 홈의 개수
            for (auto XY : slots) {
                // lock에서 i,j는 그 위에있는 key에선 kx,ky임
                int kx = XY.first - i;
                int ky = XY.second - j;
                // key 밖에있는 홈이거나, 그 홈을 못채우면 그냥 break
                if (kx<0 || kx >=M || ky<0 || ky>=M)    break; 
                if (key[kx][ky] == 0)   break;
                //채울 수 있으면, 채운 홈의 개수 하나 증가
                cnt ++;
            }

            // 홈을 다 채웠으면 true반환
            if (cnt == slots.size()) {
                return true;
            }
        }
        
    }
    }
    
    return false;
}

// 자물쇠의 중간 부분이 모두 1인지 확인
bool check(vector<vector<int> > newLock) {
    int lockLength = newLock.size() / 3;
    for (int i = lockLength; i < lockLength * 2; i++) {
        for (int j = lockLength; j < lockLength * 2; j++) {
            if (newLock[i][j] != 1) {
                return false;
            }
        }
    }
    return true;
}

bool solution(vector<vector<int> > key, vector<vector<int> > lock) {
    int n = lock.size();
    int m = key.size();
    // 자물쇠의 크기를 기존의 3배로 변환
    vector<vector<int> > newLock(n * 3, vector<int>(n * 3));
    // 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            newLock[i + n][j + n] = lock[i][j];
        }
    }

    // 4가지 방향에 대해서 확인
    for (int rotation = 0; rotation < 4; rotation++) {
        rotate(key); // 열쇠 회전
        for (int x = 0; x < n * 2; x++) {
            for (int y = 0; y < n * 2; y++) {
                // 자물쇠에 열쇠를 끼워 넣기
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        newLock[x + i][y + j] += key[i][j];
                    }
                }
                // 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if (check(newLock)) return true;
                // 자물쇠에서 열쇠를 다시 빼기
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < m; j++) {
                        newLock[x + i][y + j] -= key[i][j];
                    }
                }
            }
        }
    }
    return false;
}

int main() {
    vector<vector<int>> key = {{0,0,0},{1,0,0},{0,1,1}};
    vector<vector<int>> lock = {{1,1,1},{1,1,0},{1,0,1}};
    bool tmp = solution(key, lock);
    cout << tmp ;
    return 0;
}