import numpy as np

# Create Board Obj
class Board:
    def __init__(self, dimension = (3,3), win_num = 3):
        self.board = np.zeros(dimension) # setup board
        self.board -= 1 # initialise all values to -1
        self.board = np.int0(self.board) # set values to integer
        self.win_num = win_num
    
    def validate_move(self, pos):
        # Expect pos to be an array
        '''Check if there isn't already a piece there'''
        if self.board[pos[0]][pos[1]] == -1: # Note: needs to be expanded to n-dimensional case
            print("Already a piece there")
            return False
        print("Move is fine")
        return True
    
    def play_move(self, pos, player_num):
        if self.validate_move(pos):
            self.board[pos[0]][pos[1]] == player_num # Note: needs to be expanded to n-dimensional case
            return True
        return False
    
    def check_diagonal(self):
        return False # Default
    
    def check_horizontal(self):
        board_shape = np.shape(self.board)
        consecutive = 0 # Keep track of the number of consecutive pieces
        player_num = -1 # Keep track of the player_num with consecutives
        j = 0
        for i in range(board_shape[0]):
            consecutive = 0 # Reset counter
            player_num = self.board[i,j] # Set player num to index
            for j in range(board_shape[1]):
                if self.board[i,j] == player_num:
                    consecutive += 1
                else:
                    consecutive = 1 # Reset to 1, cos 1 counter already found
                    player_num = self.board[i,j]
                if consecutive >= self.win_num and player_num != -1:
                    print("{} has won!".format(player_num))
                    return player_num
        return False # No one won by default
    
    def check_vertical(self):
        return False # Default

    def is_game_over(self):
        'Return True if someone has got win_num-in-a-row'
        if self.check_horizontal() or self.check_vertical() or self.check_diagonal():
            return True
        return False # Default

    def __repr__(self):
        return str(self.board)