package main
import (
	"fmt"
	"math/rand"
	"time"
	"math"
	"os"
	"strconv"
	"log"
)

func yahtzee() ([]int, int) {
	x := 0
	s := []int{}
	counter := 0
	for x < 1 {
		s = s[:0]
		for y := 1; y <= 5; y++ {
			rand.Seed(time.Now().UnixNano())
			s = append(s, int(math.Floor((rand.Float64()*6)+1))) //floor of random*6 + 1
		}
		//fmt.Println(s)
		counter = counter + 1
		if s[0] == s[1] && s[0] == s[2] && s[0] == s[3] && s[0] == s[4]{
			x = 1
		}
	}
	return s, counter
}

func multiple(reps int) {
	amounts := []int{0, 0, 0, 0, 0, 0}
	rolls := []int{}
	for trial := 1; trial <= reps; trial++ {
		s, counter := yahtzee()
		if s[0] == 1 {
			amounts[0] = amounts[0]+1
		} else if s[0] == 2 {
			amounts[1] = amounts[1]+1
		} else if s[0] == 3 {
			amounts[2] = amounts[2]+1
		} else if s[0] == 4 {
			amounts[3] = amounts[3]+1
		} else if s[0] == 5 {
			amounts[4] = amounts[4]+1
		} else if s[0] == 6 {
			amounts[5] = amounts[5]+1
		}
		rolls = append(rolls, counter)
		fmt.Println("Trial number " + strconv.Itoa(trial) + " of " + strconv.Itoa(reps) + " took " + strconv.Itoa(counter) + " rolls, a yahtzee of " + strconv.Itoa(s[0]) + "'s")
	}
	fmt.Println(rolls)
	fmt.Println(amounts)
}

func main() {
	t, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	multiple(t)
}