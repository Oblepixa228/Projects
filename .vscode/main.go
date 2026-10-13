package main

import "fmt"

func main(){
	var firstname, lastname string
	var age int
	fmt.Print("Введите ваше имя и фамилию: ")
	fmt.Scan(&firstname, &lastname)
	fmt.Print("Введите ваш возраст: ")
	fmt.Scan(&age)
	lowAge := age - 5
	fmt.Printf("Приятно познакомиться, %s. Я 5 лет назад познакомился с человеком, у которого тоже фамилия %s, вам тогда было %d. Как молоды мы были!", firstname, lastname, lowAge)
}