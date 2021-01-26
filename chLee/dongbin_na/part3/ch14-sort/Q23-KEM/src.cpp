#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Score {
    public:
        string name;
        int k;
        int e;
        int m;
        
        bool operator < (Score& s) {
            if (this->k > s.k) {
                return true;
            } else if (this->k < s.k) {
                return false;
            }

            if (this->e < s.e) {
                return true;
            } else if (this->e > s.e) {
                return false;
            }

            if (this->m > s.m) {
                return true;
            } else if (this->m < s.m) {
                return false;
            }

            return this->name < s.name;
        }
};

int main () {
    int N;
    cin >> N;
    vector<Score> v(N);
    for (int i=0; i<N; i++) {
        string n;
        int k,e,m;
        cin >> n >> k >> e >> m;
        v[i] = Score{n,k,e,m};
    }

    sort(v.begin(), v.end());

    for (auto e : v) {
        cout << e.name << endl;
    }

    return 0;
}