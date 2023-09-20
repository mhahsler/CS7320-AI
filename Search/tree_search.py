# +
import numpy as np

from maze_helper import *

# randomize the order in which availabe_directions checks the neighbors. 
# Try different orders cheking them in a random order.

DIR2POS = {
    'N' : (-1, 0),
    'E' : ( 0, 1),
    'S' : ( 1, 0),
    'W' : ( 0,-1)
}

ORDER = None
RANDOMIZATION = None
DIRS = None 

# The order matters if RANDOMIZATION = False
# Note that: DFS works takes elements from the frontier in reverse order!


def set_order(order = "NESW", random = False, verbose = True):
    global RANDOMIZATION, DIR2POS, ORDER, DIRS
    
    RANDOMIZATION = random
    ORDER = [pos for pos in order]
    DIRS = [DIR2POS[dir] for dir in ORDER]
    
    if verbose:
        if RANDOMIZATION:
            print("Directions are checked at every step in random order.")
        else:
            print(f"Directions are checked in the order {ORDER}")
        
set_order("NESW", verbose = True)


# +
def add_path_to_maze(maze, path = {}, verbose = False):
    """add a path, frontier and reached to a maze"""
    maze = np.copy(maze)
    
    if "path" in path and not path["path"] is None:
        if verbose:
            print(f"Path length: {len(path['path'])-1}")
        for pos in path["path"]:
            if maze[pos[0], pos[1]] == " ":
                maze[pos[0], pos[1]] = "P"
    
    if "frontier" in path:
        for pos in path["frontier"]:
            if maze[pos[0], pos[1]] == " ":
                maze[pos[0], pos[1]] = "F"
            
    if "reached" in path:
        if verbose:
            print(f"Reached squares: {len(path['reached'])}")
        for pos in path["reached"]:
            if maze[pos[0], pos[1]] == " ":
                maze[pos[0], pos[1]] = "."
    
    return(maze)
 
def show_path(maze, path = {}, verbose = True): 
    show_maze(add_path_to_maze(maze, path, verbose = verbose))
    
def min_index(x):
    """find index of minimum. for ties the index of the most recently added result is returned."""
    return(np.where(x == np.amin(x))[0][-1])


# +
# Heuristics
    
# heuristics h(n)
def manhattan(pos1, pos2):
    """returns the Manhattan distance between two positions"""
    return(np.sum(np.abs(np.subtract(pos1, pos2))))
    
#print(manhattan([0,0], [1,1]))

def euclidean(pos1, pos2):
    """returns the Euclidean distance between two positions"""
    return(np.sqrt(np.sum(np.square(np.subtract(pos1, pos2)))))

#print(euclidean([0,0], [1,1]))

def heuristic(pos1, pos2): pass
heuristic = manhattan


# -

def expand(maze, pos):
    """find available directions as a list of lists with elements [dir, (pos)]."""
    global RANDOMIZATION, DIRS, ORDER
       
    available = [[dir, pos] for dir, pos in zip(ORDER, np.add(pos, DIRS)) if look(maze, pos) != "X"]
    if RANDOMIZATION: np.random.shuffle(available)
        
    return available


# +
# Basic Node structure (see Fig 3.7 on page 73)
# A* will add h and DFS will add a frontier field.

class Node:
    def __init__(self, pos, parent, action, cost):
        self.pos = tuple(pos)    # the state; positions are (row,col)
        self.parent = parent     # reference to parent node to get the path. None means root node
        self.action = action     # action used in the transition function
        self.cost = cost         # for uniform cost this is the depth. is also g(n) for A* search

    def __str__(self):
        return f"Node({self.action}, {self.pos})"
    
    def get_path_from_root(self):
        """returns the path from the root to the current node.""" 

        node = self
        path = [node]
    
        while not node.parent is None:
            node = node.parent
            path.append(node)
        
        path.reverse()     
        
        return(path)


# -

def best_first_search(maze, strategy = "BFS", W = 1, limit = None, debug = False, vis = False, animation = False):
    """
    See Algorithm in Fig. 3.9 on page 77 in the textbook and 3.7 on page Fig. 3.7 on page 73 (best-first)
    
    strategy can be currently "BFS", "DFS", "GBFS" , "A*"
    
    Notes: 
    * DFS should not be implemented this way. Implement it without storing all reached states.
    * GBFS and A* search use Best-first search (Fig. 3.7 on page 73) which is almost identical to BFS 
    """
    
    if animation:
        maze_anim = []
    else:
        maze_anim = None
    
    def add_vis():
        if vis: 
            show_path(maze, { 
                "path" : [n.pos for n in node.get_path_from_root()], 
                "reached" : reached.keys(), 
                "frontier" : [n.pos for n in frontier] 
            })
            
        if animation:
            maze_anim.append(add_path_to_maze(maze, { 
                "path" : [n.pos for n in node.get_path_from_root()], 
                "reached" : reached.keys(), 
                "frontier" : [n.pos for n in frontier]
            }))
        
    
    start_pos = find_pos(maze, "S")
    goal_pos = find_pos(maze, "G")

    node = Node(start_pos, parent = None, action = None, cost = 0)
    if strategy in ["GBFS", "A*"]: 
        node.h = heuristic(node.pos, goal_pos)
    
    # our initial node cannot be the goal, but I still check
    if look(maze, node.pos) == "G": 
        path = node.get_path_from_root()
        return({ "path" : [n.pos for n in path] })
        
    # frontier is a list with node references. 
    # This could be implemented with a priority queue (a heap). Initialize with the root node.
    frontier = [ node ]

    
    # reached for avoiding visiting nodes more than once. 
    # Key is a position and the value is a reference to the node in the tree 
    reached = { node.pos : node }
    
    while not len(frontier) < 1:
        
        if debug: 
            print("Frontier:", [n.pos for n in frontier])
        
        # expand frontier
        if strategy == "BFS": 
            node = frontier.pop(0)
        
        elif strategy == "DFS":
            # NOTE: DFS does not need the reached structure! This has a memory complexity of O(b^m)!  
            node = frontier.pop(-1)
        
        elif strategy == "GBFS":
            # choose node with smallest heuristic value h(n)
            # TODO: we could store the value in the frontier and use a priority queue or min heap.
            hs = [ n.h for n in frontier ]
            node = frontier.pop(min_index(hs))
        
        elif strategy == "A*":
            # use smallest f(n) = g(n) + W * h(n)
            fs = [ n.cost + W * n.h for n in frontier ]
            node = frontier.pop(min_index(fs))
        
        else:
            print(f"Unknown search strategy: {strategy}!")
            return(None)
        
        # expand frontier
        if debug: 
            print("Expanding:", node.pos)       
        
        for action, pos in expand(maze, node.pos):       
            
            child = Node(pos, node, action = action, cost = node.cost + 1) 
            if strategy in ["GBFS", "A*"]: 
                child.h = heuristic(child.pos, goal_pos)
        
            # check if the new reached node is the goal
            if look(maze, child.pos) == "G": 
                add_vis()
                
                path = child.get_path_from_root()
                return({ 
                    "path" : [n.pos for n in path], 
                    "actions" : [n.action for n in path[1:]], 
                    "reached" : reached.keys(), 
                    "frontier" : [n.pos for n in frontier],
                    "reached_full" : reached,
                     "maze_anim" : maze_anim 
                    })
            
            # break cycles 
            
            # for DFS, A* and GBFS, we also need reexamine these nodes that can be reached cheaper
            if strategy in ["DFS", "A*", "GBFS"]:
            #and not limit is None:
                if child.pos in reached.keys() and child.cost >= reached[child.pos].cost: 
                    continue   
            else:    
                if child.pos in reached.keys(): 
                    continue
            
            # add node
            reached[child.pos] = child          
            
            # check depth limit before adding node to the frontier
            if limit is None or child.cost < limit: 
                if debug: print(f"Adding to frontier: {child.pos}")
                frontier.append(child)
                                
        # show progress
        add_vis()
            
    # failure (frontier is empty)
    if debug: 
        print("Could not reach the goal!")
    
    return({ "path" : None, "actions" : None, "reached" : reached.keys(), "frontier" : [], "reached_full" : reached, "maze_anim" : maze_anim }) 


# +
# DFS: Space complexity of O(b*m) with simple cycle checking

# * frontier is stored in nodes inside the branch structure.

# cycle only checks cycles in the current branch!
def is_cycle(node):
    """check if the node is in the current branch."""
    path = node.get_path_from_root()[:-1]
    in_path = node.pos in [ n.pos for n in path ]

    return in_path 

# This follows the texbook    
def DFS(maze, limit = None, check_cycle = True, max_tries = None, debug_reached = False,
         vis = False, animation = False):
    
    # variables/functions for debugging and visualization
    DSF_TRIES = 0
    DSF_DEBUG_REACHED = {}  
    
    if animation:
        maze_anim = []
    else:
        maze_anim = None
    
    def add_vis():
        if vis: 
            show_path(maze, { 
                "path" : [n.pos for n in node.get_path_from_root()], 
                "reached" : [], 
                "frontier" : [n.pos for n in frontier] 
            })
            
        if animation:
            maze_anim.append(add_path_to_maze(maze, { 
                "path" : [n.pos for n in node.get_path_from_root()], 
                "reached" : [], 
                "frontier" : [n.pos for n in frontier]
            }))
    
    
    # DFS starts here
    start_pos = find_pos(maze, "S")
    goal_pos = find_pos(maze, "G")

    # frontier and root node
    frontier = [Node(start_pos, parent = None, action = None, cost = 0)] 
    
    while len(frontier)>0:
        node = frontier.pop()
        
        # goal check
        if look(maze, node.pos) == "G": 
            add_vis()  
            
            path = node.get_path_from_root()
            return({ 
                "path" : [n.pos for n in path],
                "actions" : [n.action for n in path[1:]],
                "frontier" : [n.pos for n in frontier],
                "reached" : DSF_DEBUG_REACHED.keys(),
                "maze_anim" : maze_anim 
             })    
        
        # return fail if max tries is exceeded (this is not in the textbook)
        if not max_tries is None:
            DSF_TRIES += 1
            if DSF_TRIES >= max_tries:
                break
        
        # check depth limit
        if not limit is None and node.cost >= limit: 
            continue
        
        # cycle checking
        if check_cycle and is_cycle(node): 
            continue
            
        # expand node
        expand_nodes = [Node(pos, node, action = action, cost = node.cost + 1) 
                     for action, pos in expand(maze, node.pos)]        
        
        # Note: We need to make sure that nodes are not twice in the frontier!    
        # I remove previous nodes with the same pos
        expand_pos = [n.pos for n in expand_nodes]
        frontier = [n for n in frontier if n.pos not in expand_pos] + expand_nodes  
        
        if debug_reached or vis:
                for n in expand_nodes:
                    DSF_DEBUG_REACHED[n.pos] = 1             
        
        add_vis()         
    
    # no solution found!
    return({ "path" : None, 'actions' : None, 'frontier' : [], 'reached' : DSF_DEBUG_REACHED.keys(), "maze_anim" : maze_anim  })


# -

def IDS(maze, max_limit = np.inf, max_tries = None, debug = False, vis = False):
    
    # Not used for DFS
    #reached = [] ### keep track of nodes reached in all iterations
    
    limit = 1
    while True:
        if debug: print(f"IDS depth = {limit}") 
        
        #Tree Search can return reached
        #result = TreeSearch(maze, strategy = "DFS", limit = limit, debug = False, vis = False)
        #reached = list(set().union(reached, result["reached"]))
        #result["reached"] = reached
           
        # DFS does not have reached!
        result = DFS(maze, limit = limit, max_tries = max_tries, vis = False)
        
        # DFS gets really slow for large problems (cycle detection is less effective than reached)
        # result = DFS(maze, limit = limit, debug = False, vis = False)
        
        result["limit"] = limit
        
        
        if(result["path"] != None): break
        
        # goal not found at limit
        if(limit > max_limit): return(result)
            
        limit += 1
    
    if debug: print(f"Solution found at depth = {limit}") 
    result["frontier"] = [] # this is jsut an artifact
    return(result)


def IDS_reached(maze, max_limit = np.inf, debug = False, vis = False):
    
    # Not used for DFS
    reached = [] ### keep track of nodes reached in all iterations
    
    limit = 1
    while True:
        if debug: print(f"IDS depth = {limit}") 
        
        #Tree Search can return reached
        result = best_first_search(maze, strategy = "DFS", limit = limit, debug = False, vis = False)
        reached = list(set().union(reached, result["reached"]))
        result["reached"] = reached
           
        # DFS does not have reached!
        #result = DFS(maze, limit = limit, debug = False, vis = False)
        
        # DFS gets really slow for large problems (cycle detection is less effective than reached)
        # result = DFS(maze, limit = limit, debug = False, vis = False)
        
        result["limit"] = limit
        
        
        if(result["path"] != None): 
            break
        
        # goal not found at limit
        if(limit > max_limit): 
            return(result)
            
        limit += 1
    
    if debug: 
        print(f"Solution found at depth = {limit}") 

    result["frontier"] = [] # this is jsut an artifact
    return(result)

