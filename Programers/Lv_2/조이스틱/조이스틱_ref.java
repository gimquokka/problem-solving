/*
참고 사이트:
https://parksuu.github.io/139-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-(java)/
 */

class prog_2_조이스틱 {

    static public int solution(String name) {
        int answer = 0;

        int len = name.length();

        //최대로 가질 수 있는 min값은 끝까지 가는것
        int min_move = len-1;

        for(int i=0; i<len; i++) {
            answer += Math.min(name.charAt(i)-'A', 'Z'-name.charAt(i)+1);

            //좌우: 연속된 A의 등장에 따라 최소 움직임이 달라진다
            int next = i+1;// 현재 다음 위치부터
            //내 다음이 A라면 계속 NEXT++
            while(next<len && name.charAt(next) == 'A')
                next++;

            if (next == len) min_move = Math.min(min_move, i);
            else min_move = Math.min(min_move, i+len-next + i);
        }//for

        answer += min_move;

        return answer;
    }


    public static void main(String[] args) {
        System.out.println(solution("ABAA"));
        System.out.println(solution("BAAAAABBB"));
    }
}