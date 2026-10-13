package main

import "fmt"

type Rectangle struct {
	Width  float64
	Height float64
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
	return (r.Width + r.Height) * 2
}

func describe(r Rectangle) string {
	return fmt.Sprintf("Площадь: %.2f, Периметр: %.2f", r.Area(), r.Perimeter())
}

func main() {
	rectangle := Rectangle{16, 25}
	fmt.Println(describe(rectangle))
}