#include <iostream>
#include <vector>
using namespace std;

int map[4][4];
char dir;

vector<int> arr1(5);
vector<int> arr2(5);
vector<int> arr3(5);
vector<int> arr4(5);

void split(char);
void push();
void sliding();
void merge(char);

int main() {
    cin >> dir;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> map[i][j];
        }
    }    

    split(dir);
    push();
    sliding();
    merge(dir);
    
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            int tmp = map[i][j]==-1 ? 0 : map[i][j];
            printf("%d ", tmp);
        }
        cout << endl;
    }

    return 0;
}

void split(char d) {
    if (d == 'D') {
    for (int i=0; i<4; i++) {
        arr1[i] = map[3-i][0];
        arr2[i] = map[3-i][1];
        arr3[i] = map[3-i][2];
        arr4[i] = map[3-i][3];
    }
    }else if (d == 'U') {
        for (int i=0; i<4; i++) {
            arr1[i] = map[i][0];
            arr2[i] = map[i][1];
            arr3[i] = map[i][2];
            arr4[i] = map[i][3];
        }
    }else if (d == 'R') {
        for (int i=0; i<4; i++) {
            arr1[i] = map[0][3-i];
            arr2[i] = map[1][3-i];
            arr3[i] = map[2][3-i];
            arr4[i] = map[3][3-i];
        }
    }else if (d == 'L') {
        for (int i=0; i<4; i++) {
            arr1[i] = map[0][i];
            arr2[i] = map[1][i];
            arr3[i] = map[2][i];
            arr4[i] = map[3][i];
        }
    }
    arr1[4] = -1;
    arr2[4] = -1;
    arr3[4] = -1;
    arr4[4] = -1;
}


void push() {
    bool isPushed = false;
    //arr1
    int i = 0;
    while (i<4) {
        i %= 4;
        if (arr1[i] == 0) {
            arr1.erase(arr1.begin()+i);
            arr1.push_back(0);
            i--;
        }
        if (arr1[i] == -1) {
            break;
        }
        i++;
    }
    //arr2
    i = 0;
    while (i<4) {
        i %= 4;
        if (arr2[i] == 0) {
            arr2.erase(arr2.begin()+i);
            arr2.push_back(0);
            i--;
        }
        if (arr2[i] == -1) {
            break;
        }
        i++;
    }
    //arr3
    i = 0;
    while (i<4) {
        i %= 4;
        if (arr3[i] == 0) {
            arr3.erase(arr3.begin()+i);
            arr3.push_back(0);
            i--;
        }
        if (arr3[i] == -1) {
            break;
        }
        i++;
    }
    //arr4
    i = 0;
    while (i<4) {
        i %= 4;
        if (arr4[i] == 0) {
            arr4.erase(arr4.begin()+i);
            arr4.push_back(0);
            i--;
        }
        if (arr4[i] == -1) {
            break;
        }
        i++;
    }
}

void sliding() {
    //arr1
    bool isChange = true;
    while(isChange) { 
        isChange = false;
        for (int i=0; i<4; i++) {
            if (arr1[i] != 0 && arr1[i] == arr1[i+1]) {
                arr1[i] *= 2;
                arr1.erase(arr1.begin() + i + 1);
                arr1.push_back(0);
                isChange = true;
            }
        }
    }

    //arr2
    isChange = true;
    while(isChange) { 
        isChange = false;
        for (int i=0; i<4; i++) {
            if (arr2[i] != 0 && arr2[i] == arr2[i+1]) {
                arr2[i] *= 2;
                arr2.erase(arr2.begin() + i + 1);
                arr2.push_back(0);
                isChange = true;
            }
        }
    }

    //arr3
    isChange = true;
    while(isChange) { 
        isChange = false;
        for (int i=0; i<4; i++) {
            if (arr3[i] != 0 && arr3[i] == arr3[i+1]) {
                arr3[i] *= 2;
                arr3.erase(arr3.begin() + i + 1);
                arr3.push_back(0);
                isChange = true;
            }
        }
    }

    //arr4
    isChange = true;
    while(isChange) { 
        isChange = false;
        for (int i=0; i<4; i++) {
            if (arr4[i] != 0 && arr4[i] == arr4[i+1]) {
                arr4[i] *= 2;
                arr4.erase(arr4.begin() + i + 1);
                arr4.push_back(0);
                isChange = true;
            }
        }
    }
}

void merge(char d) {
    if (d == 'D') {
        for (int i=0; i<4; i++) {
            map[3-i][0] = arr1[i];
            map[3-i][1] = arr2[i];
            map[3-i][2] = arr3[i];
            map[3-i][3] = arr4[i];
        }
    }else if (d == 'U') {
        for (int i=0; i<4; i++) {
            map[i][0] = arr1[i];
            map[i][1] = arr2[i];
            map[i][2] = arr3[i];
            map[i][3] = arr4[i];
        }
    }else if (d == 'R') {
        for (int i=0; i<4; i++) {
            map[0][3-i] = arr1[i];
            map[1][3-i] = arr2[i];
            map[2][3-i] = arr3[i];
            map[3][3-i] = arr4[i];
        }
    }else if (d == 'L') {
        for (int i=0; i<4; i++) {
            map[0][i] = arr1[i];
            map[1][i] = arr2[i];
            map[2][i] = arr3[i];
            map[3][i] = arr4[i];
        }
    }
}
