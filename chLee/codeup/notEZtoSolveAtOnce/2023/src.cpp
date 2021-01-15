#include <iostream>
#include <vector>

using namespace std;

int main() {
    //65-90 -> 1부터 26까지
    vector<int> ans;
    long long n;
    cin >> n;
    
    while (n>0) {
        int tmp = n%26;
        if (tmp == 0) {
            tmp = 26;
        }
        ans.push_back(tmp-1);
        n = (n-tmp)/26;
    }

    for (int i=ans.size()-1; i>=0; i--) {
        printf("%c", ans[i]+65);
    }
    cout << endl;

    return 0;
}
