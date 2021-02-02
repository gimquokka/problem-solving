#include <iostream>
#include <vector>

using namespace std;

int main() {
    int M,N;
    cin >> M >> N;
    vector<int> isPrime(N+1, true);
    isPrime[1] = false;
    for (int i=2; i*i<=N; i++) {
        if (isPrime[i]) {
            for (int j=2; i*j<=N; j++) {
                isPrime[i*j] = false;
            }
        }
    }

    for (int i=M; i<=N; i++) {
        if (isPrime[i]) {
            printf("%d\n", i);
        }
    }
    return 0;
}