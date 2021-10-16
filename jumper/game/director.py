from game.guesser import Guesser
import random

class Director:
    def __init__(self):
        self.keep_playing = True
        self.guesser = Guesser()
        self.answer = ""
        with open('dictionary.txt', 'r') as dictionaryFile:
            listOfWords = dictionaryFile.readlines()
            self.answer = listOfWords[random.randint(0, len(listOfWords) - 1)].strip()

    def start_game(self):
        self.do_outputs()

        while self.keep_playing and self.guesser.can_play():
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            

    def get_inputs(self):
        guessed_letter = self.get_letter()
        self.guesser.guessed_letters.append(guessed_letter)

    def do_updates(self):
        if not str(self.guesser.guessed_letters[-1]) in self.answer:
            self.guesser.health -= 1
        if all(x in self.guesser.guessed_letters for x in self.answer):
            self.keep_playing = False

    def do_outputs(self):
        self.draw_jumper()
        self.draw_word()
        print()
        if self.keep_playing == False:
            print("You won!")
        elif not self.guesser.can_play():
            print("You lost. Sorry!")
            print(f"The word was: {self.answer.upper()}")

    def get_letter(self):
        guess = input("Guess a letter [a-z]: ")
        if guess in self.guesser.guessed_letters:
            print("You already guessed that letter, please try a different one.")
            return self.get_letter()
        elif len(guess) == 1 and guess.isalpha():
            return guess.lower()
        print("Invalid input.")
        return self.get_letter()

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
            print()
            print(" /___\ ")
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")
        elif self.guesser.health == 2:
            print()
            print(" \   / ")
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")
        elif self.guesser.health == 1:
            print()
            print("  \ /  ")
            print("   0   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")
        elif self.guesser.health == 0:
            print()
            print("   X   ")
            print("  /|\  ")
            print("  / \  ")
            print("       ")
            print("^^^^^^^")

    def draw_word(self):
        hint = ""
        for letter in self.answer:
            if letter in self.guesser.guessed_letters:
                hint += f"{letter.upper()} "
            else:
                hint += "_ "
        print(hint)
        

