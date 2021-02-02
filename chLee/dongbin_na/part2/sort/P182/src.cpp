#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n,k;
    cin >> n >> k;

    vector<int> a;
    vector<int> b;
    for (int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        a.push_back(tmp);
    }
    for (int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        b.push_back(tmp);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end(), greater<>());

    for (int i=0; i<k; i++) {
        if (a[i] > b[i]) {
            break;
        }
        int tmp = a[i];
        a[i] = b[i];
        b[i] = tmp;
    }

    int sum = 0;
    for (auto e : a) {
        sum += e;
    }

    cout << sum;
    
    return 0;
}