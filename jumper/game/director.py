from game.guesser import Guesser
import random

class Director:
    def __init__(self):
        self.keep_playing = True
        self.guesser = Guesser()
        self.answer = ""
        with open('dictionary.txt', 'r') as listOfWords:
            self.answer = listOfWords[random.randint(0, len(listOfWords) - 1)]

    def start_game(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass # This is where the Guess a letter code needs to go

    def do_updates(self):
        pass # This is when we add the letter to the guessed letters, update the health by subtracting one point if the guess was incorrect, etc.

    def do_outputs(self):
        self.draw_word()
        self.draw_jumper()

    def draw_jumper(self):
        if self.guesser.health == 4:
            print("  ___  ")
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("")
            print("^^^^^^^")
        elif self.guesser.health == 3:
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")
        elif self.guesser.health == 2:
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")
        elif self.guesser.health == 1:
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")
        elif self.guesser.health == 0:
            print("   X   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")

    def draw_word(self):
        hint = ""
        for letter in self.answer:
            if letter in self.guesser.guessed_letters:
                hint += f"{letter} "
            else:
                hint += "_ "
        print(hint)
        

