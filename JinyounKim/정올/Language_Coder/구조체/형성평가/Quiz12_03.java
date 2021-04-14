import java.util.Scanner;

class rectangle {
    int ld_x, ld_y, ru_x, ru_y;

    rectangle () {}

    rectangle(int _ld_x, int _ld_y, int _ru_x, int _ru_y) {
        ld_x = _ld_x;
        ld_y = _ld_y;

        ru_x = _ru_x;
        ru_y = _ru_y;
    }

    void out() {
        System.out.printf("%d %d %d %d", ld_x, ld_y, ru_x, ru_y);
    }

    void setUnion(rectangle a, rectangle b) {
        ld_x = Math.min(a.ld_x, b.ld_x);
//        System.out.println(ld_x);
        ld_y = Math.min(a.ld_y, b.ld_y);
//        System.out.println(ld_y);
        ru_x = Math.max(a.ru_x, b.ru_x);
//        System.out.println(ru_x);
//        System.out.println(a.ru_y + " " + b.ru_y);
        ru_y = Math.max(a.ru_y, b.ru_y);
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        rectangle a = new rectangle(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
//        System.out.printf("%d %d %d %d \n", a.ld_x, a.ld_y, a.ru_x, a.ru_y);
        rectangle b = new rectangle(sc.nextInt(), sc.nextInt(), sc.nextInt(), sc.nextInt());
//        System.out.printf("%d %d %d %d \n", b.ld_x, b.ld_y, b.ru_x, b.ru_y);

        rectangle c = new rectangle();

        a.setUnion(a, b);
//        System.out.printf("%d %d %d %d", a.ld_x, a.ld_y, a.ru_x, c.ru_y);

        a.out();
    }
}
