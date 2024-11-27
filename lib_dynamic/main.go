// main.go
package main

import "C"

func main() {}

//export add
func add(a int, b int) int {
    return a + b
}
