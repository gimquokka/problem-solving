#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cin >> s;
    string v="";
    int sum=0;
    for(int i=0; i<s.size(); i++) {
        if (s[i]>='A' && s[i]<='Z') {
            v.append(1, s[i]);
        } else {
            sum += s[i]-'0';
        }
    }
    sort(v.begin(), v.end());
    cout << v << sum ;

    return 0;
}