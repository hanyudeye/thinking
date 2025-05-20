package main

import "fmt"

func main()  {
	fmt.Println("Hello, World!")
	defer fmt.Println("Goodbye, World!")
	defer fmt.Println("Hello, Universe!")
}


