#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main () {
    int N,C;
    cin >> N >> C;
    vector<int> houses(N);
    for (int i=0; i<N; i++) {
        cin >> houses[i];
    }
    sort(houses.begin(), houses.end());

    //파라메트릭 서치
    int min_gap = 1;
    int max_gap = houses[houses.size()-1]-houses[0];
    int result = 0;
    while (min_gap <= max_gap) {
        int current_gap = (min_gap+max_gap)/2;
        int cnt = 1;
        
        int justBefore = houses[0];
        for (int i=1; i<N; i++) {
            if (houses[i]-justBefore >= current_gap) {
                justBefore = houses[i];
                cnt ++;
            }
        }

        if (cnt >= C) {
            min_gap = current_gap+1;
            result = current_gap;
        } else {
            max_gap = current_gap-1;
        }
    }

    cout << result << endl;

    return 0;
}