#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int N,M;
    cin >> N >> M;
    vector<vector<int>> m(N+1, vector<int> (N+1));
    vector<pair<int,int>> house;
    vector<pair<int,int>> chicken;

    for (int i=1; i<N+1; i++) {
        for (int j=1; j<N+1; j++) {
            int tmp;
            cin >> tmp;
            if (tmp == 1) {
                house.push_back({i,j});
            }
            if (tmp == 2) {
                chicken.push_back({i,j});
            }
        }
    }

    int numChick = chicken.size();
    vector<int> select(numChick);
    for (int i=0; i<M; i++) {
        select[i] = 1;
    }

    int min_cityD = 987654321;
    do {
        int city_d = 0;
        for (auto h : house) {
            int min_d = 987654321;
            for (int i=0; i<numChick; i++) {
                int tmp = abs(h.first-chicken[i].first) + abs(h.second-chicken[i].second); 
                min_d = min(tmp, min_d);
            }
            city_d += min_d;
        }
        min_cityD = min(min_cityD, city_d);
    } while(prev_permutation(select.begin(), select.end()));
    
    
    cout << min_cityD;

    return 0;
}