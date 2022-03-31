<!-- #region -->
# Chapter 5: Adversarial Search and Games

## Contents

### Connection to search with nondeterministic actions (from Chapter 4.3)
* Example: [Solving Tic-Tac-Toe with And-Or-Tree Search](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/tictactoe_and_or_tree_search.ipynb). Here the opponent is seen as part of the environment, i.e.,
each action by the player is folloed by an unknown action of the opponent which, from the viewpoint of the player makes the outcomes of actions nondeterministic.

### Solving games using adversarial search
* Example: [Solving Tic-Tac-Toe with Minimax Search and Alpha-Beta Pruning](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/tictactoe_alpha_beta_tree_search.ipynb)
* Example: [Solving Tic-Tac-Toe with Heuristic Alpha-Beta Tree Search](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/tictactoe_heuristic_alpha_beta_tree_search.ipynb)
* Example: [Solving Tic-Tac-Toe with Pure Monte Carlo Search](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/tictactoe_pure_monte_carlo_search.ipynb)
* Example: [Solving Tic-Tac-Toe with Pure Monte Carlo Search + UCB1 Selection Policy](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/tictactoe_monte_carlo_tree_search_restricted.ipynb)

### Interactive game play
* Example: [Play Tic-Tac-Toe Interactively (Simple Implementation)](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/tictactoe_interactive.ipynb)


### Assignments
* Assignment: [Adversarial Search: Playing Connect 4](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/assignment_connect4.ipynb)
* Assignment: [Adversarial Search: Playing "Mean" Connect 4](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/assignment_mean_connect4.ipynb)
* Assignment: [Adversarial Search: Playing Dots and Boxes](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/Games/assignment_dots_and_boxes.ipynb)


### Connection to Machine Learning (more in Chapter 19)
* The example [Learn to Score a Tic-Tac-Toe Board by Example](https://colab.research.google.com/github/mhahsler/CS7320-AI/blob/master/ML/ML_for_tictactoe.ipynb) uses a neural network trained on self-play data to lean an evaluation function that can be used as a heuristic in Heuristic Minimax Search or as a playout policy for Monte Carlo Search.


## License
All code and documents in this repository is provided under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License](https://creativecommons.org/licenses/by-sa/4.0/)

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/3.0/88x31.png)
<!-- #endregion -->
