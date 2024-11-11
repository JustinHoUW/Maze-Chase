import pymaze as maze, random

# Group related data
class GameSearch:
    def _init_(self, maze, start, goal) :
            self.maze = maze
            self.start = start
            self.goal = goal
            gameTree = [] # Initialize gameTree as list of list representation
            self.depth = depth
            

# game tree checks for open spaces vs. closed wall
def openDoor (maze, gameTree, position):
      if maze.maze_map(position) == 1: # Open space
        return true
      else:
           return false
