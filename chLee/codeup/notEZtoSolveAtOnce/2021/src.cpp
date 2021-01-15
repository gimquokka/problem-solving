#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> val;
vector<int> cnt;

void swap(vector<int>& v, int x, int y) {
    int temp = v[x];
    v[x] = v[y];
    v[y] = temp;

}
void quicksort(vector<int> &vec, int L, int R) {
    int i, j, mid, piv;
    i = L;
    j = R;
    mid = L + (R - L) / 2;
    piv = vec[mid];

    while (i<R || j>L) {
        while (vec[i] < piv)
            i++;
        while (vec[j] > piv)
            j--;

        if (i <= j) {
            swap(vec, i, j);
            swap(val, i, j);
            i++;
            j--;
        } else if (j < i){
            if (i < R)
                quicksort(vec, i, R);
            if (j > L)
                quicksort(vec, L, j);
            return;
        }
    }
}


int main() {
    int N;
    map<int,int> m;
    cin >> N;

    int answer = 0;

    int c = 0;
    while (N--) {
        int tmp;
        scanf("%d", &tmp);
        m[tmp] += 1;
    }

    for (auto it : m) {
        val.push_back(it.first);
        cnt.push_back(it.second);
    }

    quicksort(cnt, 0, cnt.size()-1);

    int order = cnt.size()-1; //cnt가 큰 것부터 볼 것이야
    int fc = cnt[order];
    vector<int> fv;
    vector<int> sv;
    while (order >= 0) { //finding most-max group
        if (cnt[order] < fc) {
            fc = cnt[order];
            break;
        }
        fv.push_back(val[order]);
        order --;
    }

    if (fv.size() > 1) { //should find answer only in first group
        sort(fv.begin(), fv.end());
        answer = *(fv.end()-1) - fv[0];
    } else {
        if (order >= 0) { //finding second-max group
            while (order >= 0) { //finding second-max group
                if (cnt[order] < fc) {
                    break;
                }
                sv.push_back(val[order]);
                order --;
            }
            sort(sv.begin(), sv.end());
            int t1 = abs(fv[0] - sv[0]);
            int t2 = abs(fv[0] - sv[sv.size()-1]);
            answer = t1>t2?t1:t2;
        } else { //no leave entity - sensors have only one value
            answer = 0;
        }
    }
    
    cout << answer << endl;

    return 0;
}