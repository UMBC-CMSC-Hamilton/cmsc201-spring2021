import tkinter as tk
import tkinter.ttk as ttk
import random
import time
from threading import Thread


class PathFindingGridDisplay(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Grid .. Grid .. Grid")
        self.geometry('1200x800')

        self.the_grid_canvas = tk.Canvas(self)
        self.the_grid_canvas.pack(fill=tk.BOTH, expand=True)
        self.the_grid = []
        self.size = 750
        self.the_grid_lines = []
        self.the_squares = []
        right_frame = tk.Frame(self)
        self.message_label = tk.Label(right_frame, text="Pick Starting Point")
        self.message_label.pack(side=tk.TOP)
        # self.the_path_tree = ttk.Treeview(self)
        self.the_grid_canvas.bind("<Button-1>", self.register_click)
        self.starting = None
        self.destination = None
        self.the_path = []
        self.construct_random_grid(10, 10)
        self.draw_grid()
        self.visited = [[False for _ in range(len(self.the_grid[0]))] for _ in range(len(self.the_grid))]
        # adjust this for speed of drawing and searching
        self.sleep_time = 0.25
        self.find_thread = None
        self.bind('<r>', self.reset)
        self.bind('<g>', self.generate_new_grid)

    def register_click(self, event):
        """ event.x and event.y contain the position, compute the x, y location and then check if something needs to be done """
        if self.the_grid and self.the_grid[0]:
            ratio = self.size // (max(len(self.the_grid), len(self.the_grid[0])) + 1)
            if 0 <= event.y // ratio - 1 < len(self.the_grid[0]) and 0 <= event.x // ratio - 1 < len(self.the_grid):
                x_coord = event.y // ratio - 1
                y_coord = event.x // ratio - 1
                self.walk_path((y_coord, x_coord))

    def draw_grid(self):
        if self.the_grid:
            # draw lines
            ratio = self.size // (max(len(self.the_grid), len(self.the_grid[0])) + 1)
            for j in range(len(self.the_grid) + 1):
                self.the_grid_canvas.create_line(ratio, ratio * (j + 1), ratio * (len(self.the_grid) + 1), ratio * (j + 1), fill="black", width=2)
            for j in range(len(self.the_grid[0]) + 1):
                self.the_grid_canvas.create_line(ratio * (j + 1), ratio, ratio * (j + 1), ratio * (len(self.the_grid) + 1), fill="black", width=2)
            # fill default grid
            for i in range(len(self.the_grid)):
                for j in range(len(self.the_grid[0])):
                    if self.the_grid[i][j]:
                        self.the_squares[i][j] = self.the_grid_canvas.create_rectangle(ratio * (i + 1), ratio * (j + 1), ratio * (i + 2), ratio * (j + 2), fill='white')
                    else:
                        self.the_squares[i][j] = self.the_grid_canvas.create_rectangle(ratio * (i + 1), ratio * (j + 1), ratio * (i + 2), ratio * (j + 2), fill='black')

    def construct_random_grid(self, n, m):
        options = [True] * 6 + [False] * 3
        self.the_grid = [[random.choice(options) for _ in range(m)] for _ in range(n)]
        self.the_grid_lines = [[None for _ in range(m + 1)] for _ in range(n + 1)]
        self.the_squares = [[None for _ in range(m)] for _ in range(n)]

    def load_grid_from_file(self):
        pass

    def save_grid_to_file(self):
        pass

    def generate_new_grid(self, the_event):
        print('generating new grid')
        if self.find_thread is None or not self.find_thread.is_alive():
            options = [True] * 6 + [False] * 3
            n = len(self.the_grid)
            m = len(self.the_grid[0])
            self.the_grid = [[random.choice(options) for _ in range(m)] for _ in range(n)]

            for i in range(len(self.the_grid)):
                for j in range(len(self.the_grid[0])):
                    self.the_grid_canvas.itemconfigure(self.the_squares[i][j], fill='white' if self.the_grid[i][j] else 'black')

            self.reset(None)

    def search_for_path(self, current):
        """
            Does a "depth first search"
            finds the answer quickest, but the answer that it finds isn't the best usually.
        """

        # here's my base case, if we're at the destination then we return [current]
        if current == self.destination:
            return [current]
        # current is a tuple with two elements (x, y)
        x = current[0]
        y = current[1]

        """ ignore the man behind the curtain """

        self.visited[x][y] = True
        if (x, y) not in [self.starting, self.destination]:
            self.the_grid_canvas.itemconfigure(self.the_squares[x][y], fill='yellow')
        time.sleep(self.sleep_time)
        """ let's look here """

        if 0 <= x - 1 and self.the_grid[x - 1][y] and not self.visited[x - 1][y]:
            # moving "left"
            # if self.the_grid[x - 1][y] comes back as True then we're good to go there
            # false means forbidden
            path = self.search_for_path((x - 1, y))
            # if path means that the path wasn't just returned as None, []
            if path:
                return [current] + path
        if 0 <= y - 1 and self.the_grid[x][y - 1] and not self.visited[x][y - 1]:
            # moving up
            path = self.search_for_path((x, y - 1))
            if path:
                return [current] + path
        if x + 1 < len(self.the_grid) and self.the_grid[x + 1][y] and not self.visited[x + 1][y]:
            # moving right
            path = self.search_for_path((x + 1, y))
            if path:
                return [current] + path
        if y + 1 < len(self.the_grid[0]) and self.the_grid[x][y + 1] and not self.visited[x][y + 1]:
            # moving down.
            path = self.search_for_path((x, y + 1))
            if path:
                return [current] + path
        #
        return []

    def set_path(self, path):
        self.the_path = path
        print('displaying path')
        print(self.the_path)
        for p in self.the_path[1:-1]:
            self.the_grid_canvas.itemconfigure(self.the_squares[p[0]][p[1]], fill='lightskyblue')
            time.sleep(self.sleep_time)

    def walk_path(self, coordinate):
        if self.starting is None and self.the_grid[coordinate[0]][coordinate[1]]:
            self.the_grid_canvas.itemconfigure(self.the_squares[coordinate[0]][coordinate[1]], fill='blue')
            self.starting = coordinate
        elif self.destination is None and self.the_grid[coordinate[0]][coordinate[1]]:
            self.destination = coordinate
            self.the_grid_canvas.itemconfigure(self.the_squares[coordinate[0]][coordinate[1]], fill='green')
            self.find_thread = Thread(target=lambda: self.set_path(self.search_for_path(self.starting)), daemon=True)
            self.find_thread.start()
        else:
            print('Invalid Choice, perhaps')

    def reset(self, the_event):
        if self.find_thread is not None and not self.find_thread.is_alive():
            self.starting = None
            self.destination = None
            self.visited = [[False for _ in range(len(self.the_grid[0]))] for _ in range(len(self.the_grid))]
            for i in range(len(self.the_grid)):
                for j in range(len(self.the_grid[0])):
                    self.the_grid_canvas.itemconfigure(self.the_squares[i][j], fill='white' if self.the_grid[i][j] else 'black')


if __name__ == "__main__":
    pathfinder = PathFindingGridDisplay()
    pathfinder.mainloop()
