package main

import (
	"fmt"
)

type Task struct {
	Title string
	Done bool
}

func (t *Task) Complete() {
	t.Done = true
}

func (t Task) String() string {
	if t.Done {
		return "[✓] " + t.Title	
	} else {
		return "[ ] " + t.Title
	}
}

type TodoList struct {
	Tasks []Task
}

func (l *TodoList) Add(title string) {
	l.Tasks = append(l.Tasks, Task{Title: title})
}

func (l *TodoList) Complete(index int) {
	if index < 0 || index >= len(l.Tasks) {
		return 
	}
	l.Tasks[index].Complete()
}

func (l TodoList) Print() {
	if len(l.Tasks) == 0 {
		fmt.Println("Список задач пуст")
		return
	}
	for i, task := range l.Tasks {
		fmt.Printf("%d. %s\n", i+1, task)
	}
}

func main() {
	list := TodoList{}
	
	for {
		fmt.Println("\n1. Добавить задачу")
		fmt.Println("2. Отметить задачу выполненной")
		fmt.Println("3. Показать все задачи")
		fmt.Println("4. Выход")
		fmt.Print("Выберите действие: ")
		
		var choice int
		fmt.Scanln(&choice)
		
		switch choice {
		case 1:
			fmt.Print("Введите название задачи: ")
			var title string
			fmt.Scanln(&title)
			list.Add(title)
			fmt.Println("Задача добавлена!")
		case 2:
			list.Print()
			fmt.Print("Введите номер задачи: ")
			var index int
			fmt.Scanln(&index)
			list.Complete(index - 1)
			fmt.Println("Задача отмечена как выполненная!")
		case 3:
			list.Print()
		case 4:
			fmt.Println("До свидания!")
			return
		default:
			fmt.Println("Неверный выбор. Попробуйте снова.")
		}
	}
}