var name = ""

function getWeather(){
  fetch("http://api.openweathermap.org/data/2.5/weather?q=mooresville,nc,us&appid=89ac5df152df034d1ca9d081f065a2e2&units=fahrenheit",
    {mode:'no-cors'})
  .then( (response) => {console.log(reponse)})
  .then()
}
function Hello() {
  tell("Hello and welcome to the story game.")
  handle = function(input) {
    Name()
  }
}

function Name() {
  tell("What is your name?")
  handle = function(input) {
    name = input
    tell("Well nice to meet you, " + name)
    Field()
  }
}

function Field() {
  tell("You find yourself in an open field.")
  tell("You see a house in the distance to the north.")
  tell("You see a mailbox on a lonely dirt road to the South.")
  handle = function(input) {
    input = input.toLowerCase()
    if (input == "north" || input == "n" || input == "house") {
      House()
    }
    else if (input == "south" || input == "s" || input.startsWith("mail")) {
      Mailbox()
    }
  }
}

function House() {
  tell("After walking through the field you come to the house with a weather station on top.")
  handle = function(i) {
    tell("You open the door and hear a creaking sound. You see a ladder and climb up to the roof")
  }
}

var mailboxOpen = false
var stuff = {}

function readLeaflet() {
  if (stuff.leaflet) {
    tell("3-4-5-1")
  }
  else if (!stuff.leaflet) {
    tell("You do not have a leaflet to read.")
  }
}

function Mailbox() {
  tell("You stand beside a mailbox nailed to a board with rusty nails.")
  handle = function(i) {
    if (i.startsWith("open")) {
      mailboxOpen = true
      tell("You open the mailbox and find a leaflet.")
    }
    else if (i.startsWith("read")) {
      readLeaflet()
    }
    else if (i.startsWith("take")) {
      tell("you put the leaflet in your backpack.")
      stuff.leaflet = true
    }
  }
}


Hello()
