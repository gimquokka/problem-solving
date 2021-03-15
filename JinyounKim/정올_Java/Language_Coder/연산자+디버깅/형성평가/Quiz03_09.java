import java.util.Calendar;

public class Quiz03_09 {
    public static void main(String[] args){
        int a = 0;
        Calendar cal = Calendar.getInstance();

        a = cal.get(Calendar.YEAR) - 1900;
        a += cal.get(Calendar.MONTH);
        a += cal.get(Calendar.DATE);
        System.out.println(cal.get(Calendar.MONTH));
        System.out.println(cal.get(Calendar.DATE));

        System.out.printf("%d %d %d\n", 0, 121, 138);
    }

}
