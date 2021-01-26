#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <utility>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> houses(N+1);
    for (int i=1; i<N+1; i++) {
        cin >> houses[i];
    }

    pair<int,int> minimum = {987654321, 0};
    for (int i=1; i<N+1; i++) {
        int an_pos = houses[i];
        int dist_sum = 0;
        for (int j=1; j<N+1; j++) {
            dist_sum += abs(houses[j] - an_pos);
        }
        minimum = dist_sum<minimum.first? pair<int,int>{dist_sum,an_pos}: minimum;
    }

    cout << minimum.second;

    return 0;
}