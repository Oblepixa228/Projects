package main

import (
	"fmt"
	"math"
)

func main() {

	var weight float64
	var haight float64
	var imt float64

	fmt.Print("Введите ваш вес (кг): ")
	fmt.Scan(&weight)

	fmt.Print("Введите ва рост (см): ")
	fmt.Scan(&haight)

	imt = weight / math.Pow((haight/100), 2)

	var okWeight string

	switch {
	case imt < 18.5:
		okWeight = "Недостаточный вес"
	case imt >= 18.5 && imt < 25:
		okWeight = "Нормальный вес"
	case imt >= 25 && imt < 30:
		okWeight = "Избыточный вес"
	case imt >= 30:
		okWeight = "Ожирение"
	}

	fmt.Printf("Ваш ИМТ: %0.2f\nКатегория: %s", imt, okWeight)
}
