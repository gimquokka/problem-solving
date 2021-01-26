#include <iostream>
#include <string>

using namespace std;

int sizeofint(int data)
{
    int pos = 1;
    for (int i = 0; ; i++, pos++)
    {
        if ((data /= 10) <= 0)
            break;
    }
    return(pos);
}

int main() {
    string s;
    cin >> s;

    int result = s.size();
    for (int len=1; len<=s.size(); len++) {
        int pos=0;
        string toCom = s.substr(pos, len);

        int tmp_res = 0;
        int cnt=0;
        while (1) {
            pos += len;
            if (pos >= s.size()) {
                break;
            }

            string tmp = s.substr(pos,len);
            if (toCom.compare(tmp) == 0) {
                //같으면 개수 증가
                cnt ++;
            } else {
                //다르면 tmp_res에 추가될 압축 문자열 사이즈 더함
                if (cnt == 1) {
                    tmp_res += toCom.size();
                } else {
                    tmp_res += toCom.size() + sizeofint(cnt);
                }
                //초기화
                cnt = 1;
                toCom = tmp;
            }
        }

        
    }

    cout << result << endl;
    return 0;
}