# Hello, World!
puts "Hello, World!"

# 함수 정의
def greet(name)
  puts "Hello, #{name}!"
end

greet("Ruby")

# 조건문 예제
number = 10
if number > 5
  puts "Number is greater than 5"
else
  puts "Number is 5 or less"
end

# 반복문 예제
3.times do |i|
  puts "This is loop iteration #{i + 1}"
end

# 클래스 및 구조체
class Person
  attr_accessor :name, :age

  def initialize(name, age)
    @name = name
    @age = age
  end

  def introduce
    puts "Hi, my name is #{@name} and I am #{@age} years old."
  end
end

person = Person.new("Alice", 25)
person.introduce
