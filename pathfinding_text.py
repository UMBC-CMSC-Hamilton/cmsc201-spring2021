import random


def generate_grid(x, y):
    # accessible, forbidden
    grid = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(random.choices(['.', 'X'], weights=[0.8, 0.2])[0])
        grid.append(row)
    return grid


def draw_grid(the_grid):
    for i in range(len(the_grid)):
        print(' '.join(the_grid[i]))


def path_find(the_grid, current, destination, visited):
    """
    :param current: (x,y)
    :param destination: (x_dest, y_dest)
    :param visited: dictionary of visited tuples
    :return: [] if no path, else [(x_0, y_0), ..., (x_n, y_n)]
     which is a path from the start to the destination.
    """

    # base case of our recursion.
    if current == destination:
        return [destination]

    """
        Four places to look:
        (x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)
        
        the_grid[y][x]
    """

    y = current[1]
    x = current[0]

    # this takes care of forbidden spaces.
    if the_grid[x][y] == 'X':
        return []

    # visited is a dictionary.. here is where we add the tuple into the visited dictionary
    # now the dictionary remembers the tuples where we've been and we won't go there again
    visited[(x, y)] = True
    # print('We are at ({}, {})'.format(x, y))
    # up
    if 0 <= y - 1 and (x, y - 1) not in visited:
        possible_path = path_find(the_grid, (x, y - 1), destination, visited)
        if possible_path:
            the_grid[x][y] = 'p'
            return [(x, y)] + possible_path

    # right
    if x + 1 < len(the_grid) and (x + 1, y) not in visited:
        possible_path = path_find(the_grid, (x + 1, y), destination, visited)
        if possible_path:
            the_grid[x][y] = 'p'
            return [(x, y)] + possible_path

    # down
    if y + 1 < len(the_grid[x]) and (x, y + 1) not in visited:
        possible_path = path_find(the_grid, (x, y + 1), destination, visited)
        if possible_path:
            the_grid[x][y] = 'p'
            return [(x, y)] + possible_path

    # left
    if 0 <= x - 1 and (x - 1, y) not in visited:
        possible_path = path_find(the_grid, (x - 1, y), destination, visited)
        if possible_path:
            the_grid[x][y] = 'p'
            return [(x, y)] + possible_path
            # instead of:
            # return [(x, y)] + possible_path

    # none of them returned, we didn't find a path
    return []


if __name__ == '__main__':
    the_grid = generate_grid(5, 5)
    draw_grid(the_grid)
    print(path_find(the_grid, (0, 0), (4, 4), {}))
    draw_grid(the_grid)
