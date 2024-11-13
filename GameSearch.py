import pymaze as maze, random

# Group related data
class GameTree:
    
    def _init_(self, player1_position, player2_position) :
        # Store game tree
        self.game_tree = None
        self.player1_start = player1_position
        self.player2_start = player2_position
        self.maze = maze
            
    def build_game_tree(self, player1_position, player2_position, depth):
        current = player1_position
        current2 = player2_position
        self.game_tree = [player1_position, player2_position]
        utility = 0

        # List store children
        children = []

        # Possible moves: up, down, left, right
        possible_moves = [(- 1, 0), (1, 0), (0, -1), (0, 1)]

        for move in possible_moves:
            # Calculate new position for each direction in the maze
            new_position1 = (player1_position[0] + move[0], player1_position[1] + move[1])
            # Check if position is open (door)
            if self.is_open(new_position1):
                
                
    # game tree checks for open spaces vs. closed wall
    def is_open (self, position):
      x, y = position
      if 0 <= x < len(self.maze_map) and 0 <= y < len(self.maze_map[0]):
          return self.maze_map[x][y] == 1
      return False

