from random import seed, randrange
import sys

dim = 10


def display_grid():
    print('   ', '-' * (2 * dim + 1))
    for i in range(dim):
        print('   |', ' '.join('*' if grid[i][j] else ' '
                               for j in range(dim)
                               ), end=' |\n'
              )
    print('   ', '-' * (2 * dim + 1))


path = []


def connect(start, end, graphic, graphic1, move_order, path):
    def is_valid(x, y):
        return 0 <= x < len(graphic) and 0 <= y < len(graphic[0]) and graphic[x][y] == 1

    def dfs(x, y, move_order, path):
        if [x, y] == end:
            return True

        if is_valid(x, y):
            graphic[x][y] = 9  # 标记为已访问

            for move in move_order:
                dx, dy = move[0], move[1]  # 获取移动的坐标增量
                new_x, new_y = x + dx, y + dy

                if dfs(new_x, new_y, move_order, path):
                    path.append((x, y))  # 标记为路径
                    return True

        return False

    x, y = start
    if graphic[x][y] == 0:
        return None
    if dfs(x, y, move_order, path):
        path.insert(0, end)
        graph = rewrite(graphic1, path)
        return graph
    else:
        return None  # 没有可行的路径


# REPLACE PASS ABOVE WITH YOUR CODE ⬆⮕⬇⬅

# POSSIBLY DEFINE OTHER FUNCTIONS
def map_value_to_character(value):
    if value == 1:
        print('\u2b1b', end='')
    elif value == 2:
        print('\U0001F7E8', end='')
    elif value == 3:
        print('\U0001F7E9', end='')
    elif value == 4:
        print('\U0001F7EA', end='')
    elif value == 5:
        print('\U0001F7EB', end='')
    elif value == 6:
        print('\U0001F534', end='')
    else:
        print('\u2b1c', end='')


def display_gridco():
    grid_str = ''
    for i in range(dim):
        grid_str += ''.join('\u2b1b' if grid[i][j] else '\u2b1c'
                            for j in range(dim)) + '\n'
    return grid_str


def display_gridcoend(graphic):
    for i in range(dim):
        if i != 0:
            print('\n', end='')
        for j in range(dim):
            if j == 0:
                print('    ', end='')
            map_value_to_character(graphic[i][j])
    print('')


def display_num(graphic):
    num = 0
    for i in range(dim):
        for j in range(dim):
            if graphic[i][j] != 0 and graphic[i][j] != 1:
                num += 1
    return num


def rewrite(graph, path):
    x, y = end[0], end[1]
    graph[x][y] = 6
    for i in range(len(path) - 1, -1, -1):

        if path[i][0] == path[i - 1][0] and path[i][1] - 1 == path[i - 1][1]:
            graph[path[i][0]][path[i][1]] = 4

        elif path[i][0] == path[i - 1][0] and path[i][1] + 1 == path[i - 1][1]:
            graph[path[i][0]][path[i][1]] = 5

        elif path[i][0] + 1 == path[i - 1][0] and path[i][1] == path[i - 1][1]:
            graph[path[i][0]][path[i][1]] = 3

        elif path[i][0] - 1 == path[i - 1][0] and path[i][1] == path[i - 1][1]:
            graph[path[i][0]][path[i][1]] = 2
    return graph


def parse_text_to_graphic(text):
    lines = text.strip().split('\n')
    graphic = []
    for line in lines:
        row = []
        for char in line:
            if char == '\u2b1b':
                row.append(1)  # 黑色方块
            elif char == '\u2b1c':
                row.append(0)  # 白色方块
        graphic.append(row)
    return graphic


try:
    for_seed, density, dim = (int(x)
                              for x in input('Enter three integers, '
                                             'the second and third ones '
                                             'being strictly positive: '
                                             ).split()
                              )
    if density <= 0 or dim <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    start = [int(x) for x in input('Enter coordinates '
                                   'of start point:'
                                   ).split()
             ]
    if len(start) != 2 or not (0 <= start[0] < dim) \
            or not (0 <= start[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    end = [int(x) for x in input('Enter coordinates '
                                 'of end point:'
                                 ).split()
           ]
    if len(end) != 2 or not (0 <= end[0] < dim) \
            or not (0 <= end[1] < dim):
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
direction_preferences = input('Input the 4 directions, from most '
                              'preferred to least preferred:'
                              )
if set(direction_preferences) != {'⬆', '⮕', '⬇', '⬅'}:
    print('Incorrect input, giving up.')
    sys.exit()
dic_m = {'⬆': (-1, 0), '⮕': (0, 1), '⬇': (1, 0), '⬅': (0, -1)}
move_order = []
for i in direction_preferences:
    move_order.append(dic_m[i])
seed(for_seed)
grid = [[int(randrange(density) != 0) for _ in range(dim)]
        for _ in range(dim)
        ]

print('Here is the grid that has been generated:')
display_grid()
text = display_gridco()
graph = parse_text_to_graphic(text)
graph1 = parse_text_to_graphic(text)
graphic = connect(start, end, graph, graph1, move_order, path)
if graphic:
    print('\n', end='')
    graphic = rewrite(graph1, path)
    num = display_num(graphic)
    print('There is a path joining both points, of length ' + str(num) + ':')
    display_gridcoend(graphic)

else:
    print('There is no path joining both points.')
# ⬆⮕⬇⬅ ⬅⮕⬆⬇
