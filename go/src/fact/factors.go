package main
import "math"     
 
func Factors(n int) []int {
	vals := []int{}
	for x := 2; x < int(math.Ceil(math.Sqrt(float64(n)))); x++ {
		if math.Mod(float64(n), float64(x)) == 0 {
			vals = append(vals, int(float64(n)/float64(x)), int(x))
		}
	}
	if math.Mod(float64(n), math.Sqrt(float64(n))) == 0 {
		vals = append(vals, int(math.Sqrt(float64(n))))
	}
	return vals
}