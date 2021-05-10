public class StackProject {
    public static void main(String[] args) {
        Stack s1 = new Stack(10);
        char name[] = {'김','하','늘'};
        Stack s2 = new Stack(name);
        char ch;
        int i;

        for(i=0; i < 11; i++){
            s1.push((char) ('가' + i));
        }

        Stack s3 = new Stack(s1);

        ch = s1.pop();

        System.out.print("Stack s1 의 내용 : ");
        for(i=0; i < 10; i++) {
            ch = s1.pop();
            System.out.print(ch);
        }
        System.out.println("");

        System.out.print("Stack s2 의 내용 : ");
        for(i=0; i <3; i++) {
            ch = s2.pop();
            System.out.print(ch);
        }
        System.out.println("");

       System.out.print("Stack s3 의 내용 : ");
       for(i=0; i < 10; i++) {
           ch = s3.pop();
           System.out.print(ch);
       }
       System.out.println("");

    }
}
