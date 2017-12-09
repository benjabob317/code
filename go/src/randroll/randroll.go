package main
import (
	"fmt"
	"math"
	"math/rand"
	"time"
	"os"
	"strconv"
	"log"
)

func randroll(dice int, sides int) int { //random integer from 1 to max
	rand.Seed(time.Now().UnixNano())
	final := 0
	for x := 0; x < dice; x ++ {
		final = final + int(math.Floor(rand.Float64()*float64(sides)) + 1)
	}
	return final
}

func main() {
	arg1, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	arg2, err := strconv.Atoi(os.Args[2])
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(randroll(arg1, arg2))
}