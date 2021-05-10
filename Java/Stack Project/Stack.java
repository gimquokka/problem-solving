/*
* Simple Stack Datastructure
 */

class Stack {
    private char s[]; // 스택 문자 데이터를 담고있는 배열
    private int toploc; // 삽입과 삭제가 발생하는 스택 top 을 가르킴
                        // 즉 , 저장된 문자 데이터의 개수 정보를 갖는 변수

    // 1. 주어진 크기의 빈 스택을 만드는 생성자
    Stack(int size) {
        s = new char[size]; // 스택 저장공간을 할당
        toploc = 0; // 스택 top 을 초기화
    }

    // 2. 주어진 스택과 동일한 스택을 만드는 생성자
    Stack(Stack ob) {
        toploc = ob.toploc; // 스택 top 을 일치시킴
        s = new char[ob.s.length]; // 스택 저장공간 할당
        // 스택 배열 element 들을 복사
        for (int i = 0; i < toploc; i++)
            s[i] = ob.s[i];
    }

    // 3. 주어진 문자 배열로 스택을 만드는 생성자
    Stack(char a[]) {
        toploc = 0; // 스택 top 을 초기화
        s = new char[a.length]; // 스택 저장공간 할당
        // 스택 배열 element 들을 복사
        for (int i = 0; i < a.length; i++)
            push(a[i]);
    }

    // 주어진 문자를 스택에 삽입하는 메소드
    void push(char ch) {
        if (toploc == s.length) { // 스택이 가득차 있는지 check
            System.out.println("\n- 스택이 가득차 있음 -");
            return;
        }
        s[toploc++] = ch; // 스택 top 에 문자를 복사하고 top 을 증가시킴
    }

    // 스택의 top 으로부터 문자를 읽어오는 메소드
    char pop() {
        if (toploc == 0) { // 스택이 비어 있는지 check
            System.out.println("\n- 스택이 비어 있음 -");
            return (char) 0;
        }
            return s[--toploc]; // 스택 top 에서 문자를 return 시키고 top 을 감소시킴
        }
    }