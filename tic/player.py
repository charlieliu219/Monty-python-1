#data definition
#player class: get letter; get move (and current game state); 
#computer and human inherit from player: make move (random or from command line)
#game board is updated by player.make_move

import random
import math

class player:
    def __init__(self, letter):
        self.letter = letter
        
    # player makes a move based on the available spots on board 
    # self, game -> self, game? 
    def get_move(self, game):
        print("get move")
        #pass the game instance so player knows the available moves
        return game

    
class computer(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        # #make a ramdom move
        move = random.choice(game.get_available_moves())
        
        # game.board[move] = self.letter        
        return move
    
class human(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #read a number from user input 
        while True:
            move = int(input("Please select your move!"))
            available_moves = game.get_available_moves()
            if move in available_moves:
                break
        # game.board[move] = self.letter
        return move


class perfectplayer(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #use minimax() to make the best move each time 
        #initiative score[]
        if game.get_num_available_moves() == 9:
            move = random.choice(range(9))
        else:
            move = self.minimax(self.letter, game)["position"]
        return move
  
    # takes player_letter and game_state: str, tictactoe instance -> int
    def minimax(self, current_player, state):
        max_player = self.letter # this is the letter for the perfect player
        other_player = 'x' if current_player == 'o' else 'o'
        # 1. base case: 
        # if there's a winner after the last move: calculate score for both cases; otherwise if there's no available moves anymore: score = 0 return best{} with only score upadted
        
        if state.winner == other_player:
            return {"position": None, "score": 1 * (state.get_num_available_moves() + 1) if other_player == max_player else -1 * (state.get_num_available_moves() + 1)}
            
        elif state.check_tie():
            return {"position": None, "score": 0}
             
        # initiate best(position and score)
        if current_player == max_player:
            # try to find the move with the highest score
            best = {"position": None, "score": -math.inf}
        else:
            best = {"position": None, "score": math.inf}
            
        # interate through all available moves and call minimax
        for possible_move in state.get_available_moves():
            # try this move
            state.board[possible_move] = current_player
            winning_state = state.check_winner(possible_move, current_player)
            # check what happens after making the move
            next_player = 'x' if current_player == 'o' else 'o'
            sim_state = self.minimax(next_player, state)
            
            # undo the moves from previous call and update best{}
            state.board[possible_move] = '_'
            state.winner = None
            sim_state["position"] = possible_move
            
            # compare the best with the sim_state
            if current_player == max_player and sim_state["score"] > best["score"]:
                best = sim_state
            if current_player != max_player and sim_state["score"] < best["score"]:
                best = sim_state
                        
        # return best with chosen move and its score
        return best
        
                
                
                
                

            
            
            
        