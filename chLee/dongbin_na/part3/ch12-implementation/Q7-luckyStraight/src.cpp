#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int c1=0, c2=0;
    for (int i=0; i<s.size(); i++) {
        if (i<s.size()/2) {
            c1 += s[i]-'0';
        } else {
            c2 += s[i]-'0';
        }
    }

    if (c1 == c2) {
        cout << "LUCKY";
    } else {
        cout << "READY";
    }
    
    return 0;
}