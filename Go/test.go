package main

import (
	"fmt"
)

// main function
func main() {
	fmt.Println("Hello, World!")

	// Call greet function
	greet("Go")

	// Conditional statement example
	number := 10
	if number > 5 {
		fmt.Println("The number is greater than 5.")
	} else {
		fmt.Println("The number is 5 or less.")
	}

	// Loop example
	for i := 1; i <= 3; i++ {
		fmt.Printf("Loop iteration: %d\n", i)
	}

	// Struct and method example
	person := Person{Name: "Alice", Age: 25}
	person.Introduce()
}

// greet function
func greet(name string) {
	fmt.Printf("Hello, %s!\n", name)
}

// Person struct definition
type Person struct {
	Name string
	Age  int
}

// Introduce method for Person struct
func (p Person) Introduce() {
	fmt.Printf("Hi, my name is %s and I am %d years old.\n", p.Name, p.Age)
}
