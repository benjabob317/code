package main
import (
	"fmt"
	"math/rand"
	"time"
	"math"
)

func main() {
	sides := 6.0
	rand.Seed(time.Now().UnixNano())
	r := rand.Float64()
	rolled := math.Floor((r*sides)+1)
	fmt.Println(rolled)
	fmt.Println(r)
	fmt.Println(sides)
	fmt.Println("hello world")
}