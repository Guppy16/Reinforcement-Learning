# Create player object
class Player:
    def __init__(self, name):
        self.name = name
        self.wld = [0,0,0] # win/loss/draw
    
    def get_move(self):
        '''Get move from player'''
        inp = input("Which square?")
        return inp.split()
    
    def get_games_played(self):
        'Get total number of games played'
        return sum(self.wld)
    
    def __repr__(self):
        return str(self.name)
