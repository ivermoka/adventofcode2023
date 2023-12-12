package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
	file, err := os.Open("input.txt")
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var lines []string
	var x int
	var y int

	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
		x = strings.Index(line, "S")
		if (x != -1) {
			fmt.Println(x, line)
			break
		}
		y ++
	}

	running := true
	for running {
		switch {
			case lines[y][x + 1] ==   
		}

	}

	if scanner.Err() != nil {
		fmt.Println(scanner.Err())
	}
}