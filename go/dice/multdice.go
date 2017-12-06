package main
import (
	"fmt"
	"time"
	"math/rand"
	"math"
	"strconv"
	"os"
	"log"
)

func rolls(amount int, sides int) []int {
	rand.Seed(time.Now().UnixNano())
	results := []int{}
	for x := 1; x <= amount; x++ {
		results = append(results, int(math.Floor((rand.Float64()*float64(sides))+1)))
	}
	return results
}

func main() {
	arg1, err := strconv.Atoi(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	arg2, err2 := strconv.Atoi(os.Args[2])
	if err2 != nil {
		log.Fatal(err2)
	}
	fmt.Println(rolls(arg1, arg2))
}