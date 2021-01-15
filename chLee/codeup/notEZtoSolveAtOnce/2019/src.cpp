#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a,b,c;
    cin >> a >> b >> c;
    
    double R=-b/(2*a), I=0;

    if (R == 0) {
        R = 0;
    }

    double tmp = b*b - 4*a*c;
    if (tmp < 0) {
        I = sqrt(-tmp)/abs(2*a);
        printf("%0.2lf+%0.2lfi\n", R, I);
        printf("%0.2lf-%0.2lfi\n", R, I);
    } else if (tmp > 0) {
        I = sqrt(tmp)/(2*a);
        printf("%0.2lf\n", R+I); 
        printf("%0.2lf\n", R-I);
    } else if (tmp == 0) {
        printf("%0.2lf\n", R);
    }


    return 0;
}