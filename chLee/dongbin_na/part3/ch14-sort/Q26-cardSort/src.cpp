#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

void reSort(vector<int>& v) {
    int toInsert = 0;
    for (int i=1; i<v.size(); i++) {
        if (v[toInsert] > v[i]) {
            swap(v[toInsert], v[i]);
            toInsert = i;
        }
    }
}

int main() {
    int N;
    cin >> N;
    /* 너무 느린 방법 O(N^2)
    vector<int> card(N);
    for (int i=0; i<N; i++) {
        cin >> card[i];
    }

    int sum = 0;
    while (card.size() > 1) {
        card[1] += card[0];
        sum += card[1];
        card.erase(card.begin()); //O(1)
        reSort(card);
    }
    */

    /*Heap을 사용한 O(NlogN)풀이*/
    priority_queue<int> card;
    for (int i=0; i<N; i++) {
        int tmp;
        cin >> tmp;
        card.push(tmp);
    }

    int sum = 0;
    while (card.size() > 1) {
        int first = card.top();
        card.pop();
        int second = card.top();
        card.pop();

        sum += (first+second);

        card.push(sum);
    }
    
    return 0;
}