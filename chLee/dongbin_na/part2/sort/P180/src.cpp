#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <Windows.h>
using namespace std;

class student {
    public:
        string name;
        int score;
        bool operator < (student &a) {
            return this->score < a.score;
        } 
};

int main () {
    int n;
    cin >> n;
    vector<student> v;
    while (n--) {
        string ts;
        int tv;
        cin >> ts >> tv;
        v.push_back(student{ts,tv});
    }

    sort (v.begin(), v.end(), less<>());

    for (auto e : v) {
        printf("%s ", e.name);
    }
    
    return 0;
}