# data definition
# 1. class board: i * j grids


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
import queue
import re

# use list of list of str for the visible board (init: None)
# use another list of list of boolean for the minefield_map 
# always keep the two boards sync
class board:
    def __init__(self, i, j, x) -> None:
        self.length = i
        self.width = j
        self.board = self.make_board(i, j)
        self.mine_map = self.plant_mine(i, j, x)
        self.marked_board = [[False for jj in range(j)] for ii in range(i)]
        
                    
    def make_board(self, i, j):
        # initiate the board with all clear grids
        board = [[0 for jj in range(j)] for ii in range(i)]
        
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
            self.mark_mine(ii, jj)
            
        return mine_map
    
    # takes the coordinate of a mine and mark all of its neighbors
    def mark_mine(self, i, j):
        for ii in [i-1, i, i+1]:
                if ii < 0 or ii > self.length-1:
                    continue
                for jj in [j-1, j, j+1]:
                    if jj < 0 or jj > self.width-1:
                        continue
                    if ii == i and jj == j:
                        self.board[ii][jj] = -math.inf
                    self.board[ii][jj] += 1
        
              
    # print_board: remember to update to int
    def print_board(self):
        for i in range(self.length):
            for j in range(self.width):
                if self.mine_map[i][j] == True:
                    print(' | ' + '* ', end = " ")
                else:
                    print(f' | {self.board[i][j]}', end = " ")
            print('\n')
    
    def num_neighboring_mine(self, i, j):
        num = 0
        for ii in [i-1, i, i+1]:
                if ii < 0 or ii > self.length-1:
                    continue
                for jj in [j-1, j, j+1]:
                    if jj < 0 or jj > self.width-1:
                        continue
                    if ii == i and jj == j:
                       continue
                    if self.mine_map[ii][jj] == True: 
                        num += 1
        return num
    
    # recursively detect neighboring grids until [i,j] is mine  
            
# i = 0 - length; j = 0 - width         
# [i-1,j-1]     [i-1,j]     [i-1,j+1]
# [i,j-1]       [i,j]        [i, j+1]
# [i+1, j-1]    [i+1,j]      [i+1,j+1]      
     
    # push all i,j 's neighbors to queue
    def add_to_queue(self, i, j, q):
        for ii in [i-1, i, i+1]:
            if ii < 0 or ii > self.length-1:
                continue
            for jj in [j-1, j, j+1]:
                if jj < 0 or jj > self.width-1:
                    continue
                if ii == i and jj == j:
                    continue
                q.put((ii,jj))
        return q
           
    # takes a coordinate and keeps expanding the clear field. updates the marked_board for print_marked() and return nothing
    def detect(self, i, j):
        self.marked_board[i][j] = True 
        q = queue.Queue()
        # push all its neighbors to the queue
        q = self.add_to_queue(i, j, q)
        
        while not q.empty():
            coordinates = q.get()
            ii, jj = coordinates
            # skip the grid that has been visited already
            if self.marked_board[ii][jj] == True:
                continue
            # mark this grid as visited
            self.marked_board[ii][jj] = True 
            # if the grid is clear (no mines around), then push all its neighbors
            if self.board[ii][jj] == 0:
                self.add_to_queue(ii, jj, q)
            # if the grid has a number 

        return
    
    def print_marked(self):
        for i in range(self.length):
            for j in range(self.width):
                # if the grid is visited and the value >= 0 (mine has value of -inf)
                if self.marked_board[i][j] == True and self.board[i][j] >= 0:
                    print(f' | {self.board[i][j]}', end = " ")
                else:
                    print(" |  ", end = " ")
            print('\n')
        
        
           
    # is_mine? 
    def is_mine(self, i, j):
        if self.mine_map[i][j] == True:
            return True
        return False
    
    # check_clear: if all the grids in boolean map is true, then win
    def check_win(self):
        for i in range(self.length):
            for j in range(self.width):
                # there are still unmarked grids
                if not self.marked_board[i][j]:
                    return False
        return True
    
# body of the game
def play(i, j, x):
    
    game = board(i, j, x)
    
        # if i < 0 or i >= board.length or j < 0 or j >= game:
        #     print("Invalid location. Try again.")
        #     continue
        
    # game.print_board()
    
    while True:
        # prompt user for coordinates
        user_input = re.split(',(\\s)*', input("Choose a grid to dig: row, col "))  
        ii, jj= int(user_input[0]), int(user_input[-1])
        
        if game.mine_map[ii][jj] == True:
            print("Boom! Game over ")
            game.print_board()
            return 
        
        game.detect(ii, jj)
        print("now print the marked board!")
        game.print_marked()
        
        # num1 = game.num_neighboring_mine(1,1)
        
        # num2 = game.num_neighboring_mine(2,2)
        # print(f"num1 = {num1}, num2 = {num2}")
        
        if game.check_win():
            print("You won!")
            return
        
    
# launch the game
if __name__ == '__main__':
    
    user_input = re.split(',(\\s)*', input("Define your board: Input as row, col, number of mines: "))  # '8, 8'
    i, j= int(user_input[0]), int(user_input[-1])
    x = i
    play(i, j, x)

    
    
    
    
        

        