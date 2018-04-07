package main
import (
	"math"
	"fmt"
)
 
func Primefac(n int) []int {
	primetree := []int{}
	for i := 2; i < int(math.Ceil(math.Sqrt(float64(n)))); i = i + 0 {
		if math.Mod(float64(n), float64(i)) == 0 {
			i++
		} else {
			n = n/i
			primetree = append(primetree, i)
		}
	}
	if n > 1 {
		primetree = append(primetree, n)
	}
	return primetree
}

func main() {
	fmt.Println(Primefac(6))
}