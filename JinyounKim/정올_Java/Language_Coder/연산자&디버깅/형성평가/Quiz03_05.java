import java.util.Scanner;

public class Quiz03_05 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a_height, a_weight, b_height, b_weight;

        System.out.print("민수의 키와 몸무게 입력 ");
        a_height = input.nextInt();
        a_weight = input.nextInt();

        System.out.print("가영이의 키와 몸무게 입력 ");
        b_height = input.nextInt();
        b_weight = input.nextInt();

        System.out.println(((a_height > b_height) && (a_weight > b_weight))?1:0);
    }

}
