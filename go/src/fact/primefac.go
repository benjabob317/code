package main
import "math"  
 
func Primefac(n int) []int {
	num := n
	vals := []int{}
	z := 0
	for z < 1 {
		if factors(num) == [] {
			z = 1
		} else {
			vals = append(vals, factors(num)[1])
			num = factors(num)[0]
		}
	return vals
}