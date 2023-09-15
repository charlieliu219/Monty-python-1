# data definition
# 1. class board: i * j grids
# [i-1,j-1]     [i-1,j]     [i-1,j+1]
# [i,j-1]       [i,j]        [i, j+1]
# [i+1, j-1]    [i+1,j]      [i+1,j+1]

# 2. class grid: 
# 1. grid_state = 'x' (mine), ' '(init); 
# true, int(number of x in the nearby 8 grids)(marked) 
# 2. grid position (int i, j) 
# 3. is_mine?

# logic (function play):
# 1. start the game: initiate the board with certain number of x in ramdom board positions, the rest is ' '; 
# 1.5 check user input: if it's a mine, then end game.
# 2. click a grid:
    # 1. grid is mine -> return 1?
    # 2. grid has no mine in the nearby 8 grids -> mark the grid as 'true' and then call click on all its neighbors; then add return value up (sum += num_mine); when the for loop is over, update the grid_state with the sum?
    # each grid must be a class with grid_state?
    # 3. grid has a neighboring mine -> (base case) marked the grid with int (number of mines), return num_mine
# 3. check if there are remaining grids(' '), if it's 0 then winning, break the for loop

# function wish list:
# board methods:
# __init__(self, i, j, x(number of mines)) -> board[i * j] & marked_board[i * j] (all false except the minefields)
# click function(grid_self) -> num_mine in neighboring 8 grids
# check_remaining_grid(board_self) -> number of grids
# 

import random 

class grid:
    def __init__(self, i, j, state, is_mine) -> None:
        self.pos_i = i
        self.pos_j = j
        self.grid_state = state 
        self.is_mine = is_mine

class board:
    def __init__(self, i, j, x) -> None:
        # initiate the board with all clear grids
        for ii in range(i):
            for jj in range(j):
                board[ii][jj] =  grid(ii, jj, ' ', False) 
        
        # add x number of mines to unique random positions on the board
        if x > j * i:
            raise Exception("There must be more grids than mines!")
        
        mine_i = random.sample(range(0, i), x)
        mine_j = random.sample(range(0, j), x)
        for ii in mine_i:
            for jj in mine_j:  
                board[ii][jj] = grid(ii, jj, 'x', True)
            
    # get the grid with its coordinates
    def get_grid(self, i, j):
        return board[i][j] # class grid
        
    # print_board
    def print_board(self):
        
        pass
        
    # click
    def click(self, i, j):
        num_mine = 0
        return num_mine
    
    
    # is_mine? 
    def is_mine(self, i, j):
        return False
    
    # number of remaining_grid
    def get_remaining_grids(self):
        
        remaining_grids = 0
        print("You have cleared the minefiled!")
        return remaining_grids
    
    # update grid_state: what should the datatype of state be?
    def update_state(self, i, j, state):
        self[i][j].grid_state = state
        return grid
    
# body of the game
def play(i, j, x):
    board = board(i, j, x)
    while True:
        
        if board.get_remaining_grids() == 0:
            return 
        
    
# launch the game
if __name__ == '__main__':
    i = 8
    j = 8
    x = 8
    play(i, j, x)
    print("You have won the game!")
    
    
    
        

        