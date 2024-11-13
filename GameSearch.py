import pymaze as maze, random

# Group related data
class GameTree:
    
    def _init_(self, player1_position, player2_position) :
        # Store game tree
        self.game_tree = None
        self.player1_start = player1_position
        self.player2_start = player2_position
        self.maze = maze
            
    def build_game_tree(self, player1_position, player2_position, depth, is_player1_turn = True):
        current = player1_position
        current2 = player2_position
        self.game_tree = [player1_position, player2_position]
        utility = 0

        # List store children
        children = []

        # Store current position of players
        current_node = [(player1_position, player2_position)]


        # Possible moves: up, down, left, right
        possible_moves = [(- 1, 0), (1, 0), (0, -1), (0, 1)]

        if is_player1_turn:
          # Generate child nodes based on possible moves for Player 1
          for move in possible_moves:
            # Calculate new position for each direction in the maze
            new_position1 = (player1_position[0] + move[0], player1_position[1] + move[1])
            # Check if position is open (door)
            if self.is_open(new_position1):
                # Switch Turns
                is_player1_turn = False
                child_node = self.build_game_tree(new_position1, player2_position, depth - 1)
                children.append(child_node)
              
        else:
          # Generate child nodes based on possible moves for Player 1
          for move in possible_moves:
            # Calculate new position for each direction in the maze
            new_position2 = (player2_position[0] + move[0], player2_position[1] + move[1])
            # Check if position is open (door)
            if self.is_open(new_position2):
                # Switch Turns 
                is_player1_turn = True
                child_node = self.build_game_tree(player1_position, new_position2, depth - 1)
                children.append(child_node)

          # Store all paths and future moves of game state
          current_node.append(children)
          return current_node

    def minimax (self, node, depth, is_maximizing):
       
       player1_position, player2_position = node[0]

       # Check for terminal state or depth limit
       if depth == 0 or self.is_terminal(node):
          # Return utlity value at leaf nodes
          return self.evaluate(player1_position, player2_position)
       
       if is_maximizing:
          max_eval = float('-inf') # initalize max_eval to -infinte
          for child in node[1]: # node[1] contains children of current node
             eval = self.minimax(child, depth - 1, is_maximizing=False)
             max_eval = max(max_eval, eval)
          return max_eval # Return final utility value for Player 1
       else:
          min_eval = float('inf') # initialze min_eval to infinite
          for child in node[1]: # node[1] contains children of current node
             eval = self.minimax(child, depth - 1, is_maximizing=True)
             min_eval = min(min_eval, eval)
          return min_eval # Return final utility value for Player 2
                
    def alphabeta (self, node, depth, alpha, beta, is_maximizing):
       
       player1_position, player2_position = node[0]
       
       # Check for terminal state or depth limit
       if depth == 0 or self.is_terminal(node):
          # Return utlity value at leaf nodes
          return self.evaluate(player1_position, player2_position)
       
       if is_maximizing:
          max_eval = float('-inf') # initalize max_eval to -infinte
          for child in node[1]: # node[1] contains children of current node
             eval = self.alphabeta(child, depth - 1, alpha, beta, is_maximizing=False)
             max_eval = max(max_eval, eval)
             alpha = max(alpha, eval) # Update alpha
             if beta <= alpha:
                break #prune
          return max_eval # Return final utility value for Player 1
       else:
          min_eval = float('inf') # initialze min_eval to infinite
          for child in node[1]: # node[1] contains children of current node
             eval = self.alphabeta(child, depth - 1, alpha, beta, is_maximizing=True)
             min_eval = min(min_eval, eval)
             beta = min(beta, eval) # Update beta
             if beta <= alpha:
                break #prune
          return min_eval # Return final utility value for Player 2

       

    # game tree checks for open spaces vs. closed wall
    def is_open (self, position):
      x, y = position
      if 0 <= x < len(self.maze_map) and 0 <= y < len(self.maze_map[0]):
          return self.maze_map[x][y] == 1
      return False

    # Function to calcualte utility value of positions for players
    def evaluate (self, player1_position, player2_position):
       # Target point in maze for both players
       goal_position = (len(self.maze_map) - 1, len(self.maze_map[0]) - 1)
       
       # Calculate Manhattan distance 
       player1_distance = abs(player1_position[0] - goal_position[0]) + abs(player1_position[1] - goal_position[1])
       player2_distance = abs(player1_position[0] - goal_position[0]) + abs(player2_position[1] - goal_position[1])
       
       # Winning conditions for player 1 and player 2 (+100 and -100)
       return 100 if player1_distance == 0 else -100 if player2_distance == 0 else player2_distance - player1_distance