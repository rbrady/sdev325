package main

import (
    "fmt"
    "time"
)
	
func main() {
    popcorn := time.Now()
	fmt.Println("Hello, World!  Today is ", popcorn.Format("2006-01-02"))
}