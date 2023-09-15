# data definition
# 1. class board: i * j grids
# [i-1,j-1]     [i-1,j]     [i-1,j+1]
# [i,j-1]       [i,j]        [i, j+1]
# [i+1, j-1]    [i+1,j]      [i+1,j+1]

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
from typing import Any 
import math

# use list of list of str for the visible board (init: None)
# use another list of list of boolean for the minefield_map 
# always keep the two boards sync
class board:
    def __init__(self, i, j, x) -> None:
        self.length = i
        self.width = j
        self.board = self.make_board(i, j)
        self.mine_map = self.plant_mine(i, j, x)
                    
    def make_board(self, i, j):
        # initiate the board with all clear grids
        board = [['_' for jj in range(j)] for ii in range(i)]
        
        return board
    def plant_mine(self, i, j, x):
        if x > j * i:
            raise Exception("There must be more grids than mines!")
        
        mine_map = [[False for jj in range(j)] for ii in range(i)]
        
        # add x number of mines to unique random positions on the board
        mine_i = random.sample(range(0, i), x)
        mine_j = random.sample(range(0, j), x)
        counter = 0
        for ii in mine_i:
            jj = mine_j[counter]
            counter+=1
            mine_map[ii][jj] = True
            
        return mine_map
              
    # print_board: remember to update
    def print_board(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.mine_map[i][j] == True:
                    print(' | ' + '* ', end = " ")
                else:
                    print(' | ' + self.board[i][j], end = " ")
            print('\n')
        
    # click
    def click(self, i, j):
        # base case 1
        if self.is_mine(i, j):
            print("Booooooooooom")
            return math.inf
        
        num_mine = 0
        return num_mine
    
    # is_mine? 
    def is_mine(self, i, j):
        if self.mine_map[i][j] == True:
            return True
        return False
    
    # check_clear: if all the grids in boolean map is true, then win
    def check_win(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.board[i][j] == '_':
                    return False
        return True
    
    # update the visible board: all clear = 0? or number of neighboring mines? 
    # update the boolean map: if a grid is updated, mark it as true
    def update_state(self, i, j):
        pass
    
# body of the game
def play(i, j, x):
    game = board(i, j, x)
    game.print_board()
    game.check_win()
    while True:
        
        if board.check_win:
            return 
        
    
# launch the game
if __name__ == '__main__':
    i = 8
    j = 8
    x = 4
    
    play(i, j, x)
    
    
    print("You passed the test!!")
    
    
    
        

        