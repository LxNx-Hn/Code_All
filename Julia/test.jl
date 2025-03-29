# Julia 언어의 기본 예제

# 1. 변수 선언
x = 10

# 2. 함수 정의
function greet(name)
    return "Hello, $name"
end

# 3. 조건문
age = 20
if age < 18
    println("미성년자입니다.")
elseif age < 65
    println("성인입니다.")
else
    println("노인입니다.")
end

# 4. 루프
for i in 1:5
    println(i)
end

# 5. 배열
fruits = ["사과", "바나나", "체리"]
println(fruits[1])  # 사과

# 6. 딕셔너리
person = Dict("name" => "John", "age" => 30)
println(person["name"])  # John
println(person["age"])   # 30

# 7. 모듈화 예시 (가상의 모듈)
# using MyModule

# 8. 사용 예
println(greet("Alice"))  # Hello, Alice
