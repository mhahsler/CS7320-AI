# run with: `python tictactoe_data_random.py` 

from tictactoe import empty_board, actions, result, terminal, utility, other, show_board
from tictactoe import random_player, play 

import numpy as np
import pandas as pd
import math

tr = {' ': 0, 'x': 1, 'o': -1} # I translate the board into numbers

def encode_state(state):
    """Represent the board as a vector of numbers."""
    return [tr[s] for s in state]

def playout_policy_random(state, player = 'x'):
    return np.random.choice(actions(state))
    
playout_policy = playout_policy_random

def playout_record(player = 'x'):
    """Run a playout and record the boards after the player's move."""
    state = empty_board()
    current_player = 'x'
    
    boards = []
    
    while(True):
        # reached terminal state?
        u = utility(state, player)
        if u is not None: return(boards, [u] * len(boards))
  
        a = playout_policy(state, current_player)
        state = result(state, current_player, a)   
  
        if current_player == player:
            boards.append(encode_state(state))

        # switch between players
        current_player = other(current_player)

def create_data(N = 100, record = 'x'):
    board = []
    utility = []
    
    for i in range(N):
        b, u = playout_record(record)
        board.extend(b)
        utility.extend(u)
        
    return [pd.DataFrame(board), np.array(utility)]


print("Creating data.")
np.random.seed(1234)
X, y = create_data(5000)

print("Saving data to tictactoe_data.csv")
X['y'] = y
X.to_csv('tictactoe_data.csv', index = False)


