package main
import (
  "fmt"
  "math"
)       
 
func 2fac(n int64) []int {
	2vals := {}[]int
	for x := 2; x <= (int(math.Ceil(math.Sqrt(float64(n))))); x++ {
		if math.Mod(n, x) == 0 {
			2vals = append(2vals, n, x)
		}
	}
	return 2vals
}

func main() {
	fmt.Println(2fac(10))
}
