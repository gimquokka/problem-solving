#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main () {
    int n;
    cin >> n;
    vector<int> v;
    while (n--) {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }

    sort(v.begin(), v.end(), greater<>());

    for (auto e : v) {
        cout << e << " ";
    }
    return 0;
}