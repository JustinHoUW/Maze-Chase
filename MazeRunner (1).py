import pymaze as maze, random
import sys
from pymaze import COLOR  # Ensure COLOR is correctly imported
from GameSearch import GameSearch  # Import Game Search class


eCount = 0
nCount = 0
sCount = 0
wCount = 0
path = ""  # Use String to trace path

# Capture command-line inputs with ChatGPT
print(f"Arguments received: {sys.argv}")

if len(sys.argv) < 3:
    print("Usage: MazeRunner.py [player] [searchmethod] [size]")
    sys.exit(1)

player = int(sys.argv[1])  # player
search_method = (sys.argv[2])  # searchmethod
size = int(sys.argv[3])  # size

print("MazeRunner.py", player, search_method, size)


if size == 20: # Create maze size of 20 x 30
    x = random.randint(1, size) 
    y = random.randint(1, 30)
    m = maze.maze(size, 30)  
    m.CreateMaze(x, y, theme=maze.COLOR.dark, loopPercent=100)  # Random goal, dark theme
    randrow1 = random.randint(1, size) 
    randcoll1 = random.randint(1, 30)
    # Player 1
    min = maze.agent(m, 1, 1, shape='square', footprints=True, color=COLOR.red)  # Agent at (xagent, yagent)
    # Player 2
    max = maze.agent(m, shape='arrow', footprints=True, color=COLOR.green)  # Agent at (xagent, yagent)

else: # Create maze size of 10 x 10
    x = random.randint(1, size) 
    y = random.randint(1, size)
    m = maze.maze(size, size)  
    m.CreateMaze(x, y, theme=maze.COLOR.dark, loopPercent=100)  # Random goal, dark theme
    randrow1 = random.randint(10, 10) 
    randcoll1 = random.randint(10, 10)
    # Player 1
    min = maze.agent(m, 1, 1, shape='square', footprints=True, color=COLOR.red)  # Agent at (xagent, yagent)
    # Player 2
    max = maze.agent(m, shape='arrow', footprints=True, color=COLOR.green)  # Agent at (xagent, yagent)

if (player == 1):
    # Enable keyboard move for min (human)
    m.enableArrowKey(min)
else:
    # Enable keyboard move for max (human)
    m.enableArrowKey(max)


# Trace the final path of the second agent
# m.tracePath({b: path}, delay=2100, showMarked=True)

m.run()
print(m.maze_map)

# Capture command-line inputs with ChatGPT
# print(f"Max move: {sys.argv}")
