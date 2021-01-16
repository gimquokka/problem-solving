#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

string p1[] = {"", "십", "백", "천"};
string p2[] = {"", "만", "억"};
string digit[] = {"","일","이","삼","사","오","육","칠","팔","구"};

int main() {
    long long n;
    cin >> n;

    vector<string> vans;
    long long tn = n;

    if (n == 0) {
        cout << "영" << endl;
        return 0;
    }

    vector<int> dl;
    while (tn>0) { //dl에 digit분리
        int tmp = tn%10;
        dl.push_back(tmp);    
        tn = (tn-tmp)/10;
    }

    bool isEnd = false; //이거 loop를 더 깔끔하게 못하나?
    for (int i2=0; !isEnd; i2++) {
        bool flag = false;
        for (int i1=0; i1<4 && !isEnd; i1++) {
            int c_digit = dl[i2*4 + i1];
            if (c_digit != 0) {
                if (!flag) {
                    flag = true;
                    vans.push_back(p2[i2]);
                }
                vans.push_back(p1[i1]);
            }
            vans.push_back(digit[c_digit]);

            if (i2*4+i1 == dl.size()-1) {
                isEnd = true;
            }
        }
    }

    reverse(vans.begin(), vans.end());
    for (auto s : vans) {
        cout << s;
    }

    //cout << ans << endl;
    

    return 0;
}
