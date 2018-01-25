#!/usr/bin/env python3
def getslope(direction): #converts angle turned into slope
    if direction > 0 and direction <= 45:
        slope = (45/direction)
    elif direction > 45 and direction < 90:
        slope = (90-direction)/45
    elif direction > 90 and direction <= 135:
        slope = (90-direction)/45
    elif direction > 135 and direction < 180:
        slope = 0-(45/(180-direction))
    elif direction > 180 and direction <= 225:
        slope = 0-(45/(180-direction))
    elif direction > 225 and direction < 270:
        slope = (270-direction)/45
    elif direction > 270 and direction <= 315:
        slope = 0-(45/(direction-270))
    elif direction > 315 and direction < 360:
        slope = 0-((360-direction)/45)
    else:
        slope = 'depends on program'
    return slope

def reallengths(length, slope, direction): #pythagorean theorem along with terminal character widths, determines length needed to be drawn
    if 0 < direction < 90:
        mult = (length**2/(slope**2 + 1))
        yln = abs((slope**2 * mult)**0.5)
        xln = abs(mult**0.5)
    if 90 < direction < 180:
        mult = (length**2/(slope**2 + 1))
        yln = 0-(abs((slope**2 * mult)**0.5))
        xln = abs(mult**0.5)
    if 180 < direction < 270:
        mult = (length**2/(slope**2 + 1))
        yln = 0-(abs((slope**2 * mult)**0.5))
        xln = 0-(abs(mult**0.5))
    if 270 < direction < 360:
        mult = (length**2/(slope**2 + 1))
        yln = abs((slope**2 * mult)**0.5)
        xln = 0-(abs(mult**0.5))
    return yln*0.45, xln
