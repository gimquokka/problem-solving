#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> num;
vector<int> sel;
int cal() {
    int result = num[0];
    for (int i=1; i<num.size(); i++) {
        if (sel[i-1] == 0){
            result += num[i];
        } else if (sel[i-1] == 1){
            result -= num[i];
        } else if (sel[i-1] == 2){
            result *= num[i];
        } else if (sel[i-1] == 3){
            result /= num[i];
        }
    }
    return result;
}

int main() {
    int N;
    cin >> N;
    num.reserve(N);
    for (int i=0; i<N; i++) {
        int tmp;
        cin >> tmp;
        num.push_back(tmp);
    }
    for (int i=0; i<4; i++) {
        int tmp;
        cin >> tmp;
        while(tmp--) {
            sel.push_back(i);
        }
    }

    int max = -1000000001;
    int min = 1000000001;
    do {
        int tmp = cal();
        max = max<tmp?tmp:max;
        min = min>tmp?tmp:min;
    } while(next_permutation(sel.begin(), sel.end()));

    cout << max << endl;
    cout << min << endl;
    return 0;
}