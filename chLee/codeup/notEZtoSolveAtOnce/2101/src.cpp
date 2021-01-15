#include <iostream>
#include <cmath>
using namespace std;

int main () {
    long long A,B,C;
    cin >> A;
    int cnt = 0;
    for (long long Al=1; Al<A; Al++) {
        if ((A*A)%Al == 0) {
            long long Ar = (A*A)/Al;
            if ((Al+Ar)%2==0 && (Al-Ar)%2==0) {
                //cout << Al << " " << Ar << endl;
                C = (Al+Ar)/2;
                B = (-Al+Ar)/2;
                if (B>A) {
                    //cout << B << " " << C << endl;
                    cnt ++;
                }
            }
        }
    }

    cout << cnt << endl;
    return 0;
}