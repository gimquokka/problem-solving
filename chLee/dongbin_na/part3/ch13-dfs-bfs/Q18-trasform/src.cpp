//s1 균형잡힌 문자열=(,)개수 같음
//s2 올바른 문자열=(,)짝이 모두 맞음
//s1을 s2로 바꾸는 방법
#include <string>
#include <iostream>
#include <vector>
using namespace std;

bool isBalanced(string w) {
    int sum = 0;
    for (auto c : w) {
        if (c == '(') {
            sum += 1;
        } else {
            sum -= 1;
        }
    }
    return sum==0;
}

bool isRight(string w) {
    int sum = 0;
    for (auto c : w) {
        if (c == '(') {
            sum += 1;
        } else {
            sum -= 1;
        }
        if (sum < 0) {
            return false;
        }
    }

    return sum==0;
}

char reverse(char c) {
    if (c == '(') {
        return ')';
    } else {
        return '(';
    }
}

string solution(string p) {
    // 빈 문자열이면 빈 문자열 반환
    if (p.size() == 0) {
        return "";
    }
    // w를 balanced u,v로 나누기 (u는 min length string)
    string u="";
    string v="";
    for (int i=1; ;i++) {
        u = p.substr(0,i);
        if (isBalanced(u)) {
            v = p.substr(i);
            if (isBalanced(v)) break;
        }
    }
    // if u is right
    if (isRight(u)){
        // return solution(v)
        return u+solution(v);
    // else if u is not right
    } else {
        string tmp = "";
        // 빈 문자열에 '('삽입
        tmp.append(1, '(');
        // 문자열에 solution(v) 삽입
        tmp.append(solution(v));
        // 문자열에 ')'삽입
        tmp.append(1, ')');
        // u[1:u.size]를 나머지 원소를 모두 반대로 해서 문자열에 삽입
        for (int i=1; i<u.size()-1; i++) {
            tmp.append(1, reverse(u[i]));
        }
        // return 문자열
        return tmp;
    }
}

int main () {
    string p = "()))((()";
    cout << solution(p) << endl;

    return 0;
}