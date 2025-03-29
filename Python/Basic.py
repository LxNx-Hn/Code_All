# 1. 변수와 데이터 타입
x = 10            # 정수형 변수
name = "Alice"    # 문자열 변수
pi = 3.14159      # 실수형 변수
is_active = True  # 불리언 변수

# 2. 조건문
if x > 5:
    print(f"{name} says: x is greater than 5.")  # f-string을 사용한 문자열 포매팅
else:
    print(f"{name} says: x is not greater than 5.")

# 3. 반복문
for i in range(3):  # range는 0부터 2까지 반복
    print(f"Looping: {i}")

# 4. 함수 정의
def greet(person):
    return f"Hello, {person}!"

# 함수 호출
message = greet(name)
print(message)

# 5. 리스트 (리스트는 순서가 있는 자료형)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # 리스트에 요소 추가
print(f"Fruits: {fruits}")

# 6. 딕셔너리 (key-value 쌍으로 데이터를 저장)
person_info = {"name": "Alice", "age": 30, "city": "Wonderland"}
print(f"Person Info: {person_info}")

# 7. 클래스와 객체지향 프로그래밍 (OOP)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# 객체 생성
person1 = Person("Alice", 30)
print(person1.introduce())

# 8. 예외 처리 (try-except)
try:
    result = 10 / 0  # 0으로 나누기
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

# 9. 리스트 컴프리헨션 (리스트 내포)
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# 10. 모듈과 임포트 (외부 모듈 사용)
import math
print(f"Pi value from math module: {math.pi}")
