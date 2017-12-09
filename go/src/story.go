package main

import (
	"fmt"
	"github.com/skilstak/go-input"
	"strings"
)

var data = map[string]interface{} {
	"name": "",
	"hasletter": false,
	"hasbox": false,
	"lettercontents": "unknown",
	"boxcontents": "unknown",
}

var handle func ()
var line string

func tell(text string) {
	fmt.Println(text)
}

//seperator thing

func Welcome(){
	tell("Welcome to the story game!")
	handle = func () {
		Name()
	}
}

func Name(){
	tell("What is your name?")
	handle = func () {
		data["name"] = line
		tell("Well nice to meet you, " + line)
		Field()
	}
}

func Field(){ 
	tell("You find yourself in an open field, " + data["name"].(string) + ".")
	tell("You see a white house in the distance.")
	tell("You see a mailbox on a lonely dirt road.")
	handle = func () {
		if line == "mailbox" {
			Mailbox()
		} else if line == "house" {
			FrontYard()
		} else if line == "help" {
			tell("acceptable response are mailbox and house")
		} else {
			tell("Sayyyy whatnow whatnow")
			}
		}
	}

func Mailbox() {
	tell("You stand beside a rusty mailbox and see a letter inside.")
	tell("You see a box at the foot of the mailbox.")
	handle = func () {
		if strings.HasPrefix(line, "open") {
			if strings.Contains(line, "box") {
				fmt.Println("The box is sealed well, you do not have the means to open it yet.")
			} else if strings.Contains(line, "letter") {
				fmt.Println("You open the letter and see some text in a writing system you do not understand.")
			}
		} else if strings.HasPrefix(line, "take") {
			if strings.Contains(line, "box") {
				data["hasletter"] = true
				tell("You put the box into your backpack.")
			} else if strings.Contains(line, "letter") {
				data["hasletter"] = true
				tell("You put the letter into your backpack.")
			}
		}
	}
}

func FrontYard() {
	tell("You approach a run down abandoned house with a tree growing out of it.")
	handle = func () {
		tell("TODO")
	}
}

//seperator thing

func main() {
	Welcome()
	for {
		line = input.Ask("> ")
		handle()
	}
}