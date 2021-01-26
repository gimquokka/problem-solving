#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> weak, vector<int> dist) {
    int answer = 0;
    vector<int> wd(weak.size());
    for (int i=0; i<weak.size(); i++) {
        if (i < weak.size()-1){
            wd.push_back(weak[i+1]-weak[i]);
        } else {
            wd.push_back(weak[0]+n-weak[i]);
        }
    }

    for (int nofsel=1; nofsel<dist.size(); nofsel++) {
        vector<int> select(dist.size());
        for (int i=0; i<nofsel; i++) {
            select[i] = 1;
        }
        do {
            vector<int> window; //덮개
            for (int i=0; i<select.size(); i++) {
                if(select[i] == 1) {
                    window.push_back(dist[i]);
                }
            }

            vector<bool> isChecked; //check여부 확인
            for (int i=0; i<weak.size(); i++) {
                isChecked.push_back(false);
            }

            {
                
            }
        } while(prev_permutation(select.begin(), select.end()));
    }

    return answer;
}