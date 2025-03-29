# 1. 변수와 데이터 타입
x = 10            # 정수형 변수
name = "Alice"    # 문자열 변수
pi = 3.14159      # 실수형 변수
is_active = true  # 불리언 변수

# 2. 조건문
if x > 5
  puts "#{name} says: x is greater than 5."
else
  puts "#{name} says: x is not greater than 5."
end

# 3. 반복문
3.times do |i|  # 0부터 2까지 반복
  puts "Looping: #{i}"
end

# 4. 함수 정의
def greet(person : String) : String
  "Hello, #{person}!"
end

# 함수 호출
message = greet(name)
puts message

# 5. 배열 (리스트와 비슷한 개념)
fruits = ["apple", "banana", "cherry"]
fruits << "orange"  # 배열에 요소 추가
puts "Fruits: #{fruits.join(", ")}"

# 6. 해시 (딕셔너리와 유사)
person_info = {"name" => "Alice", "age" => 30, "city" => "Wonderland"}
puts "Person Info: Name: #{person_info["name"]}, Age: #{person_info["age"]}, City: #{person_info["city"]}"

# 7. 클래스와 객체지향 프로그래밍 (OOP)
class Person
  property name : String
  property age : Int32

  def initialize(name : String, age : Int32)
    @name = name
    @age = age
  end

  def introduce : String
    "Hi, I'm #{@name} and I'm #{@age} years old."
  end
end

# 객체 생성
person1 = Person.new("Alice", 30)
puts person1.introduce

# 8. 예외 처리 (try-except와 비슷한 구조)
begin
  result = 10 / x  # 0으로 나누기
rescue e : DivisionByZeroError
  puts "Error occurred: #{e.message}"
else
  puts "Result: #{result}"
end

# 9. 배열 컴프리헨션 (리스트 내포)
squares = (0..4).map { |x| x * x }
puts "Squares: #{squares.join(", ")}"

# 10. 수학 라이브러리 사용
puts "Pi value from math library: #{Math::PI}"
