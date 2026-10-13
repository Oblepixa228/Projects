package main

import (
	"fmt"
)

func main() {
	var time int
	fmt.Print("Введите время: ")
	fmt.Scan(&time)

	switch {
	case time >= 6 && time < 12:
		fmt.Printf("Сейчас %dч. - утро", time)
	case time >= 12 && time < 18:
		fmt.Printf("Сейчас %dч. - день", time)
	case time >= 18 && time < 23:
		fmt.Printf("Сейчас %dч. - вечер", time)
	case (time >= 23 && time <= 24) || (time >= 1 && time < 6):
		fmt.Printf("Сейчас %dч. - ночь", time)
	default:
		fmt.Println("Некорректное время")
	}
}
