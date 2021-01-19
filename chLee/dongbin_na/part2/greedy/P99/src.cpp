#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n,k;
    cin >> n >> k;

    int cnt = 0;
    // 만약 시간초과가 난다면, n이 k의 배수가 될때 까지 뺄 1을 '한 번에' 빼버리면 됨
    while (n != 1) {
        if (n%k == 0) {
            n /= k;
        } else {
            n -= 1;
        }
        cnt ++;
    }

cout << cnt << endl;
    return 0;
}