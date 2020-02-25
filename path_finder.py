# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
#
# Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.
#
# Path Finder Series:
# #1: can you reach the exit?
# #2: shortest path
# #3: the Alpinist
# #4: where are you?
# #5: there's someone here


def path_finder(maze):
    maze = maze.split()

    array_maze = []
    for line in maze:
        new_line = []
        for s in line:
            new_line.append(s)
        array_maze.append(new_line)

    n = len(array_maze)

    locations={0:[[0,0]]}

    #array_maze[n-1][n-1]='F'
    array_maze[0][0]=0

    i = 0
    while True:
        if not locations[i]:
            return False
        for loc in locations[i]:
            if not i+1 in locations.keys():
                locations[i+1] = []
            for step in find_steps(array_maze, loc, n):
                if step == 'F':
                    return True
                array_maze[step[0]][step[1]] = i+1
                locations[i+1].append(step)

        print_maze(array_maze)
        i+=1

def find_steps(maze, loc, n):
    r_locs = []
    num = maze[loc[0]][loc[1]]
    # up
    if loc[0] > 0:
        up = maze[loc[0]-1][loc[1]]
        if up == '.':
            r_locs.append([loc[0]-1, loc[1]])

    #right
    if loc[1] < n-1:
        right = maze[loc[0]][loc[1]+1]
        if right == 'F':
            return ['F']
        if right == '.':
            r_locs.append([loc[0], loc[1]+1])

    # down
    if loc[0] < n-1:
        down = maze[loc[0]+1][loc[1]]
        if down == 'F':
            return ['F']
        if down == '.':
            r_locs.append([loc[0]+1, loc[1]])

    #left
    if loc[1] > 0:
        left = maze[loc[0]][loc[1]-1]
        if left == '.':
            r_locs.append([loc[0], loc[1]-1])

    return r_locs

def print_maze(maze):
    for line in maze:
        print(line)
    print("\n")

d = "\n".join([
  ".W.F..",
  ".W....",
  ".W.WW.",
  "....W.",
  "....W.",
  "....W."
])


print(path_finder(d))
