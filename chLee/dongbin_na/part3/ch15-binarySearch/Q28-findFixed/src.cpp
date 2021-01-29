#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }

    int s = 0;
    int e = N-1;
    while(s <= e) {
        int mid = (s+e)/2;
        if (mid == v[mid]) {
            cout << mid << endl;
            return 0;
        }
        if (mid < v[mid]) {
            e = mid-1;
        }
        if (mid > v[mid]) {
            s = mid+1;
        }
    }
    cout << -1 << endl;
    return 0;
}