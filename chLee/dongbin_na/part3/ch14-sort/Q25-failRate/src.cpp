#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <utility>

using namespace std;
double p[502]; //p[i] i번째 맵을 도전한 사람의 수
                //p[i] - p[i+1]는 i번째를 못 깨고 머물고 있는 사람의 수

bool compare(pair<double,int> a, pair<double,int> b) {
    if (a.first > b.first) {
        return true;
    }
    if (a.first == b.first) {
        return a.second<b.second;
    }
    return false;
    
}

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    map<int,int> m;
    for (auto s_num : stages) {
        for (int i=1; i<=s_num; i++) {
            p[i] += 1;
        }
    }

    vector<pair<double,int>> tmp;
    for (int i=1; i<N+1; i++) {
        if (p[i] == 0) {
            tmp.push_back({0,i});
        } else {
            tmp.push_back({(p[i]-p[i+1])/p[i], i});
        }
    }

    sort(tmp.begin(), tmp.end(), compare);

    for (auto e : tmp) {
        answer.push_back(e.second);
    }
    return answer;
}

int main() {
    auto v = solution(4, vector<int> {4,4,4,4,4});
    return 0;
}