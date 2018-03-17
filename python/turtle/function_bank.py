#!/usr/bin/env python3
import math
def getslope(direction): #converts angle turned into slope
    if direction in [0, 90, 180, 270, 360]:
        slope = 'depends on program'
    else:
        slope = 0-math.tan((math.pi*(direction-90))/180)
    return slope

def reallengths(length, slope, direction): #pythagorean theorem along with terminal character widths, determines length needed to be drawn
    mult = (length**2/(slope**2 + 1))
    if 0 < direction < 90:
        yln = (slope**2 * mult)**0.5
        xln = mult**0.5
    if 90 < direction < 180:
        yln = 0-((slope**2 * mult)**0.5)
        xln = mult**0.5
    if 180 < direction < 270:
        yln = 0-((slope**2 * mult)**0.5)
        xln = 0-(mult**0.5)
    if 270 < direction < 360:
        yln = (slope**2 * mult)**0.5
        xln = 0-(mult**0.5)
    return yln*0.5, xln
