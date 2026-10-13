package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	var name string
	keyboard := "Клавиатура JZ9"
	headphones := "Наушники N45"
	smartphone := "Смартфон S10"

	scanner := bufio.NewScanner(os.Stdin)
	fmt.Print("Введите название товара или его часть: ")
	var lowerText string
	if scanner.Scan() {
		name = scanner.Text()

		lowerText = strings.ToLower(name)
	}

	switch {
	case strings.Contains(strings.ToLower(keyboard), lowerText):
		fmt.Printf("%s: 19200 ", keyboard)
	case strings.Contains(strings.ToLower(headphones), lowerText):
		fmt.Printf("%s: 9600 ", headphones)
	case strings.Contains(strings.ToLower(smartphone), lowerText):
		fmt.Printf("%s: 55000 ", smartphone)
	default:
		fmt.Printf("Товар %s не найден.", name)
	}
}
