//L개의 알파벳 소문자, C개의 종류
//3<=L<=C<=15
//최소 한 개의 모음
//최소 두 개의 자음
//알파벳 오름차순
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isM(char x) {
    if (x == 'a' ||x == 'e' ||x == 'i' ||x == 'o' ||x == 'u') {
        return true;
    }
    return false;
}

 vector<char> res;

//현재 길이, c배열, L, C, 자음개수, 모음개수
void go(int ind, int len, vector<char>& c, int L, int C, int j, int m) {
    if (len == L) {
        if (j < 2) {
            return;
        }
        if (m < 1) {
            return;
        }
        //display res
        for (auto r : res) {
            cout << r;
        }
        cout << endl;
    }
    
    for (int i=ind; i<C; i++) {
        char tmp = c[i];
        res.push_back(tmp);
        if (!isM(tmp)) { //자음이면
            go(i+1, len+1, c, L, C, j+1, m);
        } else { //모음이면
            go(i+1, len+1, c, L, C, j, m+1);
        }
        res.pop_back();
    }
}

int main() {
    int L,C;
    cin >> L >> C;
    vector<char> c(C);
    for (int i=0; i<C; i++) {
        cin >> c[i];
    }
    sort(c.begin(), c.end());
    go(0, 0, c, L, C, 0, 0);

    return 0;
}