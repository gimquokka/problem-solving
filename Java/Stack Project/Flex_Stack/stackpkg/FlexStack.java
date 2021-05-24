package stackpkg;

public class FlexStack implements IfCharStack {
    private char s[];
    private int toploc;

    public FlexStack(int size) {
        s = new char[size];
        toploc = 0;
    }

    public void push(char ch) {
        if (toploc == s.length) {
            char t[] = new char[2 * toploc];
            for (int i = 0; i < toploc; i++) {
                t[i] = s[i];
            }
            s = t;
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
