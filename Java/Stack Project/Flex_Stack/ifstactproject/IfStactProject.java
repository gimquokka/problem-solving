package ifstactproject;

import stackpkg.*;

public class IfStactProject {
    public static void main(String[] args) {

        FixedStack s1 = new FixedStack(10);
        FlexStack s2 = new FlexStack(5);

        IfCharStack iStack;

        char ch;
        int i;
        iStack = s1;

        for (i = 0; i < 11; i++) {
            iStack.push((char) ('가' + i));
        }

        System.out.print("Fixed Stack의 내용: ");
        for (i = 0; i < 11; i++) {
            ch = iStack.pop();
            System.out.print(ch);
        }
        System.out.println("") ;

        iStack = s2;

        for (i = 0; i < 11; i++) {
            iStack.push((char) ('A' + i));
        }

        System.out.print("Flexible Stack의 내용: ");
        for (i = 0; i < 12; i++) {
            ch = iStack.pop();
            System.out.print(ch);
        }
        System.out.println("");
    }

}
