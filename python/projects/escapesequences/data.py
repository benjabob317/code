#!/usr/bin/env python3
black = '\x1b[30m'
red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
magenta = '\x1b[35m'
cyan = '\x1b[36m'
white = '\x1b[37m'
defcl = '\x1b[39m'

blackbg = '\x1b[40m'
redbg = '\x1b[41m'
greenbg = '\x1b[42m'
yellowbg = '\x1b[43m'
bluebg = '\x1b[44m'
magentabg = '\x1b[45m'
cyanbg = '\x1b[46m'
whitebg = '\x1b[47m'
defbg = '\x1b[49m'

clear = '\x1b[0;0m'

bold = '\x1b[1m'
italic = '\x1b[3m'
uline = '\x1b[4m'
sblink = '\x1b[5m'
fblink = '\x1b[6m'
inverse = '\x1b[7m'
hide = '\x1b[8m'
strike = '\x1b[9m'

unbold = '\x1b[22m'
unitalic = '\x1b[23m'
unline = '\x1b[24m'
unblink = '\x1b[25m'
uninverse = '\x1b[27m'
unhide = '\x1b[28m'
unstrike = '\x1b[29m'

#rgb(4, 17, 21) is the vscode terminal color, rgb(6, 21, 25) on the terminal

def text255(r, g, b): #rgb text colors, 0-255 for each color, only works on VScode and incorrectly
    return f'\033[38;2;{r};{g};{b}m'
def background255(r, g, b): #rgb background colors, 0-255 for each color, only works on VScode and incorrectly
    return f'\033[48;2;{r};{g};{b}m'
def text5(r, g, b): #rgb text colors, 0-5 for each color
    return f'\033[38;5;{16+(r*36)+(g*6)+b}m'
def background5(r, g, b): #rgb background colors, 0-5 for each color
    return f'\033[48;5;{16+(r*36)+(g*6)+b}m'