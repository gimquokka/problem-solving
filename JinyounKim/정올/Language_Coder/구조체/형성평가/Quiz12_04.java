import java.util.Scanner;

class CoupleInfo {
    Scanner sc = new Scanner(System.in);
    int p_h, m_h;
    double p_w, m_w;

    void in() {
//        System.out.print("아버지의 키와 몸무게? ");
        p_h = sc.nextInt();
        p_w = sc.nextDouble();

//        System.out.print("어머니의 키와 몸무게? ");
        m_h = sc.nextInt();
        m_w = sc.nextDouble();
    }

    void studentInfo() {
        System.out.printf("height : %dcm\n", (p_h + m_h) / 2 + 5);
        System.out.printf("weight : %.1fkg\n", (p_w + m_w) / 2.0 - 4.5);
    }
}

class Main {
    public static void main(String[] args) {
        CoupleInfo couple = new CoupleInfo();

        couple.in();

        couple.studentInfo();
    }
}
