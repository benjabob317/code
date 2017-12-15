#!/usr/bin/env/python3
def welcome():
    print("Hello, and welcome to the story game.")
def name():
    return input("What is your name? ")

def weather():
    import sys
    import skilstak.colors as c
    import json
    from urllib.request import urlopen
    cityname = input("What is your city? ")
    temptype = "imperial"
    if temptype == "fahrenheit":
        temptype = "imperial"
    elif temptype == "celsius":
        temptype = "metric"
    elif temptype == "imperial":
        vtemp = "Fahrenheit"
    elif temptype == "metric":
        vtemp = "Celsius"
    elif temptype == "kelvin":
        vtemp = "Kelvin"
    request = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" + cityname + "&appid=89ac5df152df034d1ca9d081f065a2e2&units=" + temptype)
    raw = request.read().decode("utf-8")
    data = json.loads(raw)
    print("The temperature in " + c.blue + data['name'] + c.x + " is " + c.r + str(data['main']['temp']) + c.x + " degrees " + vtemp)
welcome()
print("Have fun, " + name() + ".")
weather()
