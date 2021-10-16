class Guesser:
    """ A code template for the person that guesses a letter and if they can continue playing.
    The responsibility of this class object is to set the game up and give the player 4 lives 
    and determine if they can keep playing. 
    
    Attributes:
        health(number): The number of guesses the player has left
        guessed_letters(list): A list of guessed letters the player made
    """
    
    def __init__(self):
        """ The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.health = 4
        self.guessed_letters = []
    
    def can_play(self):
        """ Determines if the payer can keep playing the game.
        
        Args:
            self(Guesser): An instance of Guesser
        """
        if self.health > 0:
            return True
        return False