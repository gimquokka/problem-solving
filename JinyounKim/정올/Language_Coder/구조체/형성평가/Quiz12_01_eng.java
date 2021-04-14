import java.util.Scanner;

class PersonalInfo1 {
    String name;
    String phone;
    String address;

    PersonalInfo1() { }

    PersonalInfo1(String _name, String _phone, String _address) {
        name = _name;
        phone = _phone;
        address = _address;
    }

    void out() {
        System.out.println("name : " + name);
        System.out.println("tel : " + phone);
        System.out.println("addr : " + address);
    }


}

class Quiz12_01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        PersonalInfo1 person1 = new PersonalInfo1(sc.next(), sc.next(), sc.next());

        person1.out();
    }
}
