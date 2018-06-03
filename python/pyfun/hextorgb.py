#!/usr/bin/env python3
rh = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
hr = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
def expform16(n): #splits n in into a multiple of 16 and a remainder
    y = (n%16)
    x = n - y
    return [(n - n%16), n%16]
def rgbtohex(r, g, b):
    final = ''
    for x in [expform16(r), expform16(g), expform16(b)]:
        final += rh[x[0]/16] + rh[x[1]]
    return final
def hextorgb(string):
    str = string.lower()
    final = []
    for x in [str[0]+str[1], str[2]+str[3], str[4]+str[5]]:
        final.append((16*hr[x[0]]) + hr[x[1]])
    return final
print(input("what is this lol > "))
print(hextorgb(input(" > ")))