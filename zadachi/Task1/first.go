package main

import "fmt"

func isAdult(age int) bool {
	if age >= 18 {
		return true
	}
	return false
}

func greet(name string, age int) string {
	if isAdult(age) {
		return "Привет, " + name + "! Ты совершеннолетний(ая)"
	}
	return "Привет, " + name + "! Ты несовершеннолетний(ая)"
}

func main() {
	adult := greet("Коля", 20)
	fmt.Println(adult)
}
