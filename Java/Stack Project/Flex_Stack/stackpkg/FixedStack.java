package stackpkg;

public class FixedStack implements IfCharStack{
    private char s[]; // 스택 문자 데이터를 담고있는 배열
    private int toploc; // 삽입과 삭제가 발생하는 스택 top을 가르킴.
                        // 즉, 저장된 문자 데이터의 개 수 정보를 갖는 변수

    public FixedStack(int size) {
        s = new char[size];
        toploc = 0;
    }


    public void push(char ch) {
        if (toploc == s.length) {
            System.out.println("\n- 스택이 가득차 있음 -");
            return;
        }
        s[toploc++] = ch;
    }

    public char pop() {
        if (toploc == 0) {
            System.out.println("\n- 스택이 비어 있음 -");
            return (char) 0;
        }
        return s[--toploc];
    }
}
