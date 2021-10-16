class Guesser:
    def __init__(self):
        self.health = 4
        self.guessed_letters = []
    
    def can_play(self):
        if self.health > 0:
            return True
        return False