#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<int> dd;

int leave(int h) {
    int sum = 0;
    for (auto d : dd) {
        if (d > h) {
            sum += (d-h);
        }
    }
    return sum;
}

int main () {
    int max = 0;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        int tmp;
        cin >> tmp;
        dd.push_back(tmp);
        max = tmp>max?tmp:max;
    }

    int s = 0;
    int e = max;
    int result = 0;
    while(s <= e) {
        int m = (s+e)/2;
        if (leave(m) < M) {
            e = m-1;
        } else {
            result = m;
            s = m+1;
        }
    }

    cout << result << endl;

    return 0;
}