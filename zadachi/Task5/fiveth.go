package main

import "fmt"

type Student struct {
	Name string
	Grade int
}

func newStudent(name string, grade int) *Student {
	return &Student{name, grade}
}

func (s *Student) Promote() {
	if s.Grade < 10 {
		s.Grade++
	}
}

func (s Student) Status() string {
	if s.Grade >= 9 {
		return "Отличник"
	} else if s.Grade >= 7 {
		return "Хорошист"
	} else if s.Grade >= 5 {
		return "Троечник"
	} else {
		return "Неуспевающий"
	}
}

func main() {
	student := newStudent("Артем", 8)
	student1 := newStudent("Петя", 7)
	student.Promote()
	fmt.Println(student.Name + " " + student.Status())
	fmt.Println(student1.Name + " " + student1.Status())
}