#include <iostream>
#include <vector>
#include <cmath>  // math 라이브러리 사용
#include <map>
#include <string>  // string 사용을 위한 헤더

using namespace std;

// 4. 함수 정의 (main 외부에서)
std::string greet(const std::string& person) {
    return "Hello, " + person + "!";
}

int main() {
    // 1. 변수와 데이터 타입
    int x = 10;            // 정수형 변수
    std::string name = "Alice";  // 문자열 변수
    double pi = 3.14159;   // 실수형 변수
    bool is_active = true; // 불리언 변수

    // 2. 조건문
    if(x > 5) {
        std::cout << name << " says: x is greater than 5." << std::endl;
    } else {
        std::cout << name << " says: x is not greater than 5." << std::endl;
    }

    // 3. 반복문
    for (int i = 0; i < 3; i++) {
        std::cout << "Looping: " << i << std::endl;
    }

    // 함수 호출
    std::string message = greet(name);
    std::cout << message << std::endl;

    // 5. 리스트 (vector 사용)
    std::vector<std::string> fruits = {"apple", "banana", "cherry"};
    fruits.push_back("orange");  // 요소 추가
    std::cout << "Fruits: ";
    for (const auto& fruit : fruits) {
        std::cout << fruit << " ";
    }
    std::cout << std::endl;

    // 6. 맵 (딕셔너리와 유사)
    std::map<std::string, std::string> person_info = {{"name", "Alice"}, {"age", "30"}, {"city", "Wonderland"}};
    std::cout << "Person Info: Name: " << person_info["name"] << ", Age: " << person_info["age"] << ", City: " << person_info["city"] << std::endl;

    // 7. 클래스와 객체지향 프로그래밍 (OOP)
    class Person {
    public:
        std::string name;
        int age;

        Person(const std::string& n, int a) : name(n), age(a) {}

        void introduce() {
            std::cout << "Hi, I'm " << name << " and I'm " << age << " years old." << std::endl;
        }
    };

    // 객체 생성
    Person person1("Alice", 30);
    person1.introduce();

    // 8. 예외 처리 (try-catch)
    try {
        int result = 10 / x;
        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error occurred: " << e.what() << std::endl;
    }

    // 9. 배열 컴프리헨션 (리스트 내포) -> C++에서는 `std::vector`로 구현
    std::vector<int> squares;
    for (int i = 0; i < 5; i++) {
        squares.push_back(i * i);
    }
    std::cout << "Squares: ";
    for (const auto& square : squares) {
        std::cout << square << " ";
    }
    std::cout << std::endl;

    // 10. 수학 라이브러리 사용
    std::cout << "Pi value from math library: " << M_PI << std::endl;

    // 만약 M_PI가 정의되지 않으면, 수학적 방법으로 Pi 값을 구할 수 있습니다.
    std::cout << "Pi calculated manually: " << std::atan(1) * 4 << std::endl;

    return 0;
}
