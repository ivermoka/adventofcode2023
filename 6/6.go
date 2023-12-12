package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}

func main() {
	part1()
	part2()
}

func part1() {
	content, err := os.ReadFile("input.txt")
	check(err)

	text := strings.SplitAfter(string((content)), "\n")
	timeStr := strings.Fields(text[0])[1:]
	distanceStr := strings.Fields(text[1])[1:]
	var allWaysToBeat []int
	for i := 0; i < len(timeStr); i++ {
		time, err := strconv.Atoi(timeStr[i])
		check(err)
		distance, err := strconv.Atoi(distanceStr[i])
		check(err)
		waysToBeat := 0
		timePressed := 0
		for j := 0; j < time; j ++ {
			timePressed ++
			distanceTravelled := timePressed * (time - timePressed)
			if (distanceTravelled > distance) {
				waysToBeat ++
			}
		}
		allWaysToBeat = append(allWaysToBeat, waysToBeat)
	}
	result := 1
	for _, val := range allWaysToBeat {
		result *= val
	}
	fmt.Println(result)
}

func part2() {
	content, err := os.ReadFile("input.txt")
	check(err)

	text := strings.SplitAfter(string((content)), "\n")
	timeStr := strings.Fields(text[0])[1:]
	distanceStr := strings.Fields(text[1])[1:]

	time, err := strconv.Atoi(strings.Join(timeStr, ""))
	check(err)
	distance, err := strconv.Atoi(strings.Join(distanceStr, ""))
	check(err)

	waysToBeat := 0
	timePressed := 0
	for j := 0; j < time; j ++ {
		timePressed ++
		distanceTravelled := timePressed * (time - timePressed)
		if (distanceTravelled > distance) {
			waysToBeat ++
		}
	}
	fmt.Println(waysToBeat)
}