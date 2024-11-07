import pymaze as maze, random
from pymaze import COLOR  # Ensure COLOR is correctly imported

x = random.randint(1, 20) 
y = random.randint(1, 30)

m = maze.maze(20, 30)  # Create a light-themed maze of size 20x30
m.CreateMaze(x, y, theme=maze.COLOR.light)  # Random goal, light theme

xagent = random.randint(1, 20) 
yagent = random.randint(1, 30)
a = maze.agent(m, xagent, yagent, shape='arrow', footprints=True, color=COLOR.yellow)  # Agent at (xagent, yagent)

# Generate a random start point for a second agent
x1 = random.randint(1, 20)
y1 = random.randint(1, 30)

# Regenerate random numbers to avoid overlap with goal and first agent
while (x1 == x and y1 == y) or (x1 == xagent and y1 == yagent):
    x1 = random.randint(1, 20)
    y1 = random.randint(1, 30)

b = maze.agent(m, x1, y1, shape='square', footprints=True, color=COLOR.red)  # Second agent

eCount = 0
nCount = 0
sCount = 0
wCount = 0
path = ""  # Use String to trace path

# Ensure agent moves 2-3 steps in every direction
while eCount < 1 or nCount < 1 or sCount < 1 or wCount < 1:
    getRandom = random.randint(1, 4)

    # Move East
    if getRandom == 1 and eCount == 0:
        steps = random.randint(2, 3)  # Randomize steps between 2 and 3
        for _ in range(steps):
            if x1 + 1 < 20:  # Check boundary to avoid moving outside maze
                x1 += 1  # Move east
                path += 'E'
        eCount += 1

    # Move North
    elif getRandom == 2 and nCount == 0:
        steps = random.randint(2, 3)  # Randomize steps between 2 and 3
        for _ in range(steps):
            if y1 + 1 < 30:  # Check boundary to avoid moving outside maze
                y1 += 1  # Move north
                path += 'N'
        nCount += 1

    # Move South
    elif getRandom == 3 and sCount == 0:
        steps = random.randint(2, 3)  # Randomize steps between 2 and 3
        for _ in range(steps):
            if y1 - 1 > 0:  # Check boundary to avoid moving outside maze
                y1 -= 1  # Move south
                path += 'S'
        sCount += 1

    # Move West
    elif getRandom == 4 and wCount == 0:
        steps = random.randint(2, 3)  # Randomize steps between 2 and 3
        for _ in range(steps):
            if x1 - 1 > 0:  # Check boundary to avoid moving outside maze
                x1 -= 1  # Move west
                path += 'W'
        wCount += 1

# Trace the final path of the second agent
m.tracePath({b: path}, delay=2100, showMarked=True)

m.run()
print(m.maze_map)
