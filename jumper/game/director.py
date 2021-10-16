from game.guesser import Guesser
import random

class Director:
    """ A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.

    Attributes:
        answer (string): A blank answer to inialize the game.
        keep_playing (boolean): Whether or not the game can continue.
        guesser (Guesser): An instance of the class of objects known as Guesser.
        
    """
    def __init__(self):
        """ The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.guesser = Guesser()
        self.answer = ""
        with open('jumper\dictionary.txt', 'r') as dictionaryFile:
            listOfWords = dictionaryFile.readlines()
            self.answer = listOfWords[random.randint(0, len(listOfWords) - 1)].strip()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        self.do_outputs()

        while self.keep_playing and self.guesser.can_play():
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting a new letter.

        Args:
            self (Director): An instance of Director.
        """
        guessed_letter = self.get_letter()
        self.guesser.guessed_letters.append(guessed_letter)

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the if the guesser was right or wrong.

        Args:
            self (Director): An instance of Director.
        """
        if not str(self.guesser.guessed_letters[-1]) in self.answer:
            self.guesser.health -= 1
        if all(x in self.guesser.guessed_letters for x in self.answer):
            self.keep_playing = False

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the jumper is drawn and the guesser guesses a word.

        Args:
            self (Director): An instance of Director.
        """
        self.draw_jumper()
        self.draw_word()
        print()
        if self.keep_playing == False:
            print("You won!")
        elif not self.guesser.can_play():
            print("You lost. Sorry!")
            print(f"The word was: {self.answer.upper()}")

    def get_letter(self):
        """Gets a letter for the guesser.

        Args:
            self (Director): An instance of Director.
        
        Returns:
            string: A letter for the guesser.
        """
        guess = input("Guess a letter [a-z]: ")
        if guess in self.guesser.guessed_letters:
            print("You already guessed that letter, please try a different one.")
            return self.get_letter()
        elif len(guess) == 1 and guess.isalpha():
            return guess.lower()
        print("Invalid input.")
        return self.get_letter()

    def draw_jumper(self):
        """ Draws the jumper in the console
        
        Args: 
            self (Director): An instance of Director 
        """
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
        """Checks the answer that the player guesses to previous attempts and
        tells the guesser if the letter was already guessed.
        
        Args:
            self(Director): An instance of Director
        """
        hint = ""
        for letter in self.answer:
            if letter in self.guesser.guessed_letters:
                hint += f"{letter.upper()} "
            else:
                hint += "_ "
        print(hint)
        

