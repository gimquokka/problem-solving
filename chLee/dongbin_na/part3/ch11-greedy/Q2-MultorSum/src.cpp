#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main() {
    string s;
    cin >> s;
    vector<int> num;
    for (int i=0; i<s.size(); i++) {
        num.push_back(s[i]-48);
    }
    num.push_back(-1); //null 추가

    for (int i=0; i<num.size()-1; i++) {
        if (num[i+1] == -1) {
            break;
        }
        int left = num[i];
        int right = num[i+1];
        if (left==0 || left==1 || right==0 || right==1) {
            right = left+right;
        } else {
            right = left*right;
        }
        num[i+1] = right;
    }

    cout << num[num.size()-2] << endl;
    return 0;
}