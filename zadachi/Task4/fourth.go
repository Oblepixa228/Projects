package main

import "fmt"

func multiTable(n int) string {

	result := ""

	for i := 1; i < 10; i++ {
		tabl := n * i
		result += fmt.Sprintf("%d * %d = %d\n", n, i, tabl)
	}

	return result
}

func main() {
	fmt.Println(multiTable(9))
}
