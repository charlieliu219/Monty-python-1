#this is the main program 

#game definition:
#keeps a board; available moves; check if there are any moves left; check winner; check tie 

#function play(game, player_x, player_o, print_game=True) :
#next_player


from player import human, computer, perfectplayer
import math

class tictactoe:
    # initiate the members
    def __init__(self):
        #initialize a board of 9 spaces
        self.board = ['_' for _ in range(9)]
        self.current = 'x'
        self.winner = None

    def print_game(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # / -> list (of available moves(int))
    def get_available_moves(self):
        #use enumerate to check tuples i,x
        available = [i for i, x in enumerate(self.board) if x == '_']

        return available
    
    # / -> integer of list size
    def get_num_available_moves(self):
        available = self.get_available_moves()
        return len(available)
    
    
    # / -> self.current (x/o)
    def next(self):
        if self.current == 'x':
            self.current = 'o'
        else:
            self.current = 'x'
        return self.current
            

    # / -> boolean
    def check_winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            self.winner = letter
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            self.winner = letter
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                self.winner = letter
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                self.winner = letter
                return True
        return False
    # / -> boolean
    def check_tie(self):
        if self.get_num_available_moves == 0 and self.winner == None:
            return True
        return False
        
# integer -> player class    
def choose_player(num):
    print(f"Choose your player{num}! Format: human/computer x/o")
    choice = str(input()).split()
    print(f"choice[0] = {choice[0]}, choice[1] = {choice[1]}")
    if choice[0] == "human":
        player = human(choice[1])
    elif choice[0] == "computer":
        player = computer(choice[1])
    else:
        print("Wrongful input! Format: human/computer x/o")
    return player

#return winner letter
def play(player1, player2, t, print_game = False):
    while True:
        if player1.letter == t.current:
            if print_game == True:
                print(f"player {player1.letter} make the move!")
                
                t.print_game()
            move = player1.get_move(t)
            t.board[move] = player1.letter
# t's state shouldn't be changed through the game_temp, but it actually was 
            
            #check winner state
            if t.check_winner(move, player1.letter):
                t.winner = "player1"
                # print(f"{t.winner} wins!")
                return t.winner
            
            t.next()
        else:
            # print(f"player {player2.letter} make the move!")
            move = player2.get_move(t)
            t.board[move] = player2.letter
            # t.print_game()   
            #check winner state
            if t.check_winner(move, player2.letter):
                t.winner = "player2"
                # print(f"{t.winner} wins!")
                return t.winner
            t.next()

        #check if it's a tie
        if t.get_num_available_moves() == 0:
            # print(f"All moves are used. It's a tie!")
            return None
        

    
if __name__=="__main__":
    #toggle print game or not
    print_game = False
    
    player1_wins = 0
    player2_wins = 0
    ties = 0
    for i in range(1000):
        #choose player1 and player2
        # player1 = choose_player(1)
        # player2 = choose_player(2)
        player1 = perfectplayer('x')
        player2 = computer('o')
        
        t = tictactoe()
        result = play(player1, player2, t)
        
        if result == 'player1':
            player1_wins+=1
        elif result == 'player2':
            player2_wins+=1
        else:
            ties+=1
        
    print(f"{player1_wins} times player1 wins, {player2_wins} times player2 wins, and {ties} times ties")


        
    
    
    
    
    
    
        