# Author : Junth Basnet

from AStarAlgo import a_star_algorithm
from time import time
from Puzzle import Puzzle

initial_state = [
    2, 8, 3,
    1, 6, 4,
    7, 0, 5]

star = "****************************************************************************************"
dashed = '--------------------------------------------------------------------------------------'

print("\n", star)
print("                 8-Puzzle State Space Search using A* Algorithm")
print("", star)

Puzzle.num_of_instances = 0

# Time Complexity

t0 = time()
solution = a_star_algorithm(initial_state)
t1 = time()
astar_time = t1 - t0

print("\n", dashed)
print("                     Time Complexity and Space Complexity")
print("", dashed)

print("Time Complexity using A* Algorithm (8-Puzzle Game): {0} Seconds".format(astar_time))

# Space Complexity
print("Space Complexity using A* Algorithm (8-Puzzle Game): {0} (i.e. {0} States are explored before finding Goal "
      "State)".format(Puzzle.num_of_instances))
