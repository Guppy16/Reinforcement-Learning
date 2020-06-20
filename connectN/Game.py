from Board import Board
from Player import Player

# Create Game Obj
class Game:
    def __init__(self, dim = (3,3), win_num = 3, num_players = 2):
        self.board = Board(dim, win_num)
        self.players = [Player(i) for i in range(num_players)]
    
    def play_game(self):
        "iterate through player moves until game over"
        p_num = 0
        while not self.board.is_game_over():
            print(p_num)
            while True:
                print(self.board) # Display board
                p_move = self.players[p_num].get_move() # Get Move from player 
                print(p_move)
                print(p_move)
                if self.board.play_move(pos=p_move, player_num=p_num):
                    break
            p_num += 1
            p_num %= len(self.players)

