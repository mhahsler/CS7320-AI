# +
# Code by Nicholas Crothers modified and expanded by M. Hahsler

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors


# -

def parse_maze(maze_str):
    """Convert a maze as a string into a 2d numpy array"""
    maze = maze_str.split('\n')
    maze = np.array([[tile for tile in row] for row in maze if len(row) > 0])
        
    return maze

# This is modified code I found on StackOverflow, at this link
# https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values
def show_maze(maze, fontsize = 10):  
    """display a maze (numpy array)"""
   
    cmap = colors.ListedColormap(['white', 'black', 'blue', 'green', 'red', 'gray', 'orange'])
    
    # make a deep copy first so the original maze is not changed
    maze = np.copy(maze)
    
    goal = find_pos(maze, 'G')
    start = find_pos(maze, 'S')
    
    # Converts all tile types to integers
    maze[maze == ' '] = 0
    maze[maze == 'X'] = 1 # wall
    maze[maze == 'S'] = 2 # start
    maze[maze == 'G'] = 3 # goal
    maze[maze == 'P'] = 4 # position/final path
    maze[maze == '.'] = 5 # visited squares
    maze[maze == 'F'] = 6 # frontier
    # Converts all string values to integers
    maze = maze.astype(np.int)
    
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap = cmap, norm = colors.BoundaryNorm(list(range(cmap.N + 1)), cmap.N))
    
    plt.text(start[1], start[0], "S", fontsize = fontsize, color = "white",
                 horizontalalignment = 'center',
                 verticalalignment = 'center')
    
    plt.text(goal[1], goal[0], "G", fontsize = fontsize, color = "white",
                 horizontalalignment = 'center',
                 verticalalignment = 'center')
    
    plt.show()

# +
# Example: Display all mazes

def run_example():
    for type in ['small', 'medium', 'large', 'open']:
        f = open(f"{type}_maze.txt", "r")    
        maze_str = f.read()
        print(maze_str)
            
        maze = parse_maze(maze_str)
        print(maze)
    
        show_maze(maze)
        
#run_example()


# -

def find_pos(maze, what = "S"):
    """
    Find start/goal in a maze. Caution: there is no error checking
    
    Parameters:
    maze: a array with characters
    what: the letter to be found ('S' for start and 'G' for goal)
    
    Returns:
    a tupple (x, y) for the found position.
    """
    
    pos = np.where(maze == what)
    return(tuple([pos[0][0], pos[1][0]]))


def look(maze, pos):
    """look at the label of a square with the position as an array of the form [x, y]."""
    
    return(maze[pos[0], pos[1]])
