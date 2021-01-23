#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool bs(int t, vector<int>& v) {
    int s = 0;
    int e = v.size()-1;
    while (s <= e) {
        int m = (s+e)/2;
        if (t == v[m]) {
            return true;
        }
        if (v[m] < t) {
            s = m+1;
        }
        if (v[m] > t) {
            e = m-1;
        }
    }

    return false;
}

int main () {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i=0; i<n; i++) {
        cin >> v[i];
    }
    int m;
    cin >> m;
    vector<int> v2(m);
    for (int i=0; i<m; i++) {
        cin >> v2[i];
    }
    
    sort(v.begin(), v.end());

    for (int i=0; i<m; i++) {
        bool tmp = bs(v2[i], v);
        if (tmp) 
            cout << "yes" << " ";
        else 
            cout << "no" << " ";
    }

    return 0;
}