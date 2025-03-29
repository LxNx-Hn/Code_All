-- Lua 언어의 기본 예제

-- 1. 변수 선언
local x = 10

-- 2. 함수 정의
function greet(name)
    return "Hello, " .. name
end

-- 3. 조건문
local age = 20
if age < 18 then
    print("미성년자입니다.")
elseif age < 65 then
    print("성인입니다.")
else
    print("노인입니다.")
end

-- 4. 루프
for i = 1, 5 do
    print(i)
end

-- 5. 테이블
local person = {
    name = "John",
    age = 30
}
print(person.name)  -- John
print(person["age"]) -- 30

-- 6. 모듈화 예시 (가상의 모듈)
-- local myModule = require("myModule")

-- 7. 사용 예
-- 게임 개발, 임베디드 시스템, 데이터 처리 등에 사용됩니다.
print(greet("Alice"))  -- Hello, Alice
