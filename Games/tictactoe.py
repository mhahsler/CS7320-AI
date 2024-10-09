# Tic Tac Toe Game functions 

# Games are defined by (see Chapter 5):
# * Actions(s) Legal moves in state s.
# * Result(s, a) Transition model.
# * Terminal(s) Test for terminal states.
# * Utility(s) Utility for player Max for terminal states.

# I represent the state (board) as a vector of length 9. 
# The values are ' ', 'x', 'o'. 

import numpy as np

def empty_board():
    """create and empty board"""
    return [' '] * 9

def actions(board):
    """return possible actions as a vector of indices"""
    return np.where(np.array(board) == ' ')[0].tolist()

    # randomize the action order
    # return np.random.shuffle(np.where(np.array(board) == ' ')[0]).tolist()

def result(state, player, action):
    """Add a single symbol to the board."""
    if state[action] != ' ':
        raise Exception(f"Illegal action {action} by player {player}!")
    
    state = state.copy()
    state[action] = player
  
    return state

def terminal(state):
    """is the state terminal?"""
    return check_board(state) != 'n'

def utility(state, player = 'x'):
    """utility of state. None defined for non-terminal states."""
    goal = check_board(state)        
    if goal == player: return +1         # win
    if goal == 'd': return 0             # draw
    if goal == other(player): return -1  # loss
    return None                          # utility is not defined 


## helper functions
def check_board(state):
    """check the board and return one of x, o, d (draw), or n (for next move)"""
    
    state = np.array(state).reshape((3,3))
    
    diagonals = np.array([[state[i][i] for i in range(len(state))], 
                          [state[i][len(state)-i-1] for i in range(len(state))]])
    
    for a_board in [state, np.transpose(state), diagonals]:
        for row in a_board:
            if len(set(row)) == 1 and row[0] != ' ':
                return row[0]
    
    # check for draw
    if(np.sum(state == ' ') < 1):
        return 'd'
    
    return 'n'

def other(player):
    if player == 'x': return 'o'
    else: return 'x'

def show_board_text(board):
    """display the board"""
    b = np.array(board).reshape((3,3))
    print(b)

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def show_board(board, help = True, dpi = 40, colors = {' ': 'white', 'x': 'red', 'o': 'black'}):
    """Show the tic-tac-toe-board. help adds the array index, dpi changes the size and
    colors sets the colors"""

    b = np.array(board).reshape((3,3))

    with plt.rc_context({'figure.dpi': dpi}):
        fig = plt.matshow(np.zeros((3, 3)), cmap = ListedColormap(['w']))
    fig.axes.axis('off')

    plt.hlines([.5, 1.5], -.5, 2.5)
    plt.vlines([.5, 1.5], -.5, 2.5)

    for row in range(3):
        for col in range(3):
            plt.text(row, col, b[col, row],
                 fontsize = 64,
                 color = colors[b[col, row]],
                 horizontalalignment = 'center',
                 verticalalignment = 'center')

    if help:
        for row in range(3):
            for col in range(3):
                plt.text(col, row - .35, col + 3 * row,
                     fontsize = 12,
                     color = 'gray',
                     horizontalalignment = 'center',
                     verticalalignment = 'center')

    plt.show()


# Random Baseline player
def random_player(board, player = None):
    """Simple player that chooses a random empty square (equal probability of all permissible actions). 
    player is unused."""
    return np.random.choice(actions(board))

# Simple Environment
def play(x, o, N = 100, show_final_board = False):
    """Let two agents play each other N times. x starts. x and y are agent functions that 
    get the board as the percept and return their next action."""
    results = {'x': 0, 'o': 0, 'd': 0}
    
    for i in range(N):
        board = empty_board()
        
        while True:
            # x moves
            a = x(board, 'x')
            board = result(board, 'x', a)
            
            win = check_board(board)   # returns the 'n' if the game is not done.
            if win != 'n':
                results[win] += 1
                break
            
            # o moves
            a = o(board, 'o')
            board = result(board, 'o', a)
            
            win = check_board(board)   # returns the 'n' if the game is not done.
            if win != 'n':
                results[win] += 1
                break
    
        if show_final_board:
            show_board(board)   

    return results