#!/usr/bin/env python3
import skilstak.colors as c
lightarray = [[[" === ", c.x], [" === ", c.x], [" === ", c.x], [" === ", c.x]], [["/   \\", c.x], ["/   \\", c.x], ["/   \\", c.x], ["/   \\", c.x]], [["|   |", c.x], ["|   |", c.x], ["|   |", c.x], ["|   |", c.x]], [["\\   /", c.x], ["\\   /", c.x], ["\\   /", c.x], ["\\   /", c.x]], [[" === ", c.x], [" === ", c.x], [" === ", c.x], [" === ", c.x]]]
#example array with 4 lights, for tests
array = [[[" === ", c.x]], [["/   \\", c.x]], [["|   |", c.x]], [["\\   /", c.x]], [[" === ", c.x]]]
#example array with one light, used to make larger arrays. a list representing screen output, with each list inside representing each of the 5 lines. each list inside of the 5 lists represents each individual light.
light = [[" === ", c.x], ["/   \\", c.x], ["|   |", c.x], ["\\   /", c.x], [" === ", c.x]] #new formatting method
secondarray = []
def change_light_amount(n): #sets light amount to n
    global secondarray
    if n <= 0:
        secondarray = []
    elif n >= len(secondarray):
        while n >= len(secondarray):
            secondarray.append(light)
    elif n <= len(secondarray):
        while n >= len(secondarray):
            secondarray.remove(secondarray[-1])
def update(): #interprets, prints light list to screen
    print(c.clear)
    output = ""
    for x in range(0, len(secondarray)+1):
        for y in secondarray: #scans through each line
            output += y[x][1] + y[x][0] + "   "
        output += "\n"
    print(output)

def change_light(light, color): #changes light arg1 to color arg2
    for scan in secondarray[light]:
        scan.remove(scan[1])
change_light_amount(3)
change_light(1, c.r)
update()