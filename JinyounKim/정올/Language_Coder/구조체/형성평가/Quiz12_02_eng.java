import java.util.Arrays;
import java.util.Scanner;

class PersonalInfo2 {
    String name;
    String phone;
    String address;

    PersonalInfo2() {}

    PersonalInfo2(String _name, String _phone, String _address) {
        name = _name;
        phone = _phone;
        address = _address;
    }

    void out() {
        System.out.println("name : " + name);
        System.out.println("tel : " + phone);
        System.out.println("addr : " + address);
    }

//    public int compareTo(PersonalInfo2 personalInfo2) {
//        if (personalInfo2.name)
//    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PersonalInfo2[] pi_arr = new PersonalInfo2[3];

        for (int i = 0; i < 3; i++) {
            pi_arr[i] = new PersonalInfo2(sc.next(), sc.next(), sc.next());
        }

        Arrays.sort(pi_arr, (o1, o2) -> o1.name.compareTo(o2.name));

        pi_arr[0].out();
    }
}
