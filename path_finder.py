

def path_finder(maze):
    maze = maze.split()
    array_maze = []
    locations = {}

    for i in range(len(maze)):
        new_line = []
        for j in range(len(maze[i])):
            new_line.append(maze[i][j])
            if maze[i][j] == '0':
                locations[0] = [[i,j]]
        array_maze.append(new_line)

    n = len(array_maze)
    if not locations:
        locations[0] = [[0,0]]
        array_maze[0][0] = 0

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

    # up
    if loc[0] > 0:
        up = maze[loc[0]-1][loc[1]]
        if up == 'F':
            return ['F']
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
        if left == 'F':
            return ['F']
        if left == '.':
            r_locs.append([loc[0], loc[1]-1])

    return r_locs

def print_maze(maze):
    for line in maze:
        print(line)
    print("\n")

d = "\n".join([
  ".W.F.." + ".W...." * 5,
  ".W...." * 6,
  ".W.WW." * 6,
  "....W." * 6,
  "....W." * 6,
  "....W." * 5 + "....W0"
])


print(path_finder(d))
